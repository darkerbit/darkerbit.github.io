import ssg

import sys

import os
import shutil
from tqdm import tqdm

import http.server
import socketserver


def build_group(group, kind, clazz=ssg.MdPage):
    if not os.path.exists(f"out/{group}/"):
        os.mkdir(f"out/{group}/")

    out = []

    files = list(os.scandir(group))

    for f in tqdm(files, group):
        name = os.path.splitext(f.name)[0]

        if name == "index":
            # Skip for now, we do this manually later
            continue

        page = clazz(f, name, kind, group)
        page.save(f"out/{group}/{name}.html")
        out.append(page)

    ssg.IndexPage(f"{group}/index.md", "index", kind, group, files=out).save(f"out/{group}/index.html")

    return out


def build():
    # Remake out/
    if os.path.exists("out/"):
        shutil.rmtree("out/")

    os.mkdir("out/")

    # Copy assets/
    shutil.copytree("assets/", "out/assets/")

    # Page groups
    tech = build_group("tech", "Technology")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="out/", **kwargs)


def serve():
    build()

    port = 8000

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"serving at port {port}")
        httpd.serve_forever()


commands = {
    "build": build,
    "serve": serve,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print(f"Usage: {sys.argv[0]} <command>\nCommands: {', '.join(commands)}")
        return

    commands[sys.argv[1]]()


if __name__ == '__main__':
    main()
