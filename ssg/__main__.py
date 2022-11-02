import ssg

import sys

import os
import shutil
from tqdm import tqdm

import http.server
import socketserver


def build_group(group, clazz=ssg.MdPage):
    if not os.path.exists(f"out/{group}/"):
        os.mkdir(f"out/{group}/")

    out = []

    for f in tqdm(os.scandir(group)):
        page = clazz(f)
        page.save(f"out/{group}/{os.path.splitext(f.name)[0]}.html")
        out.append(page)

    return out


def build():
    # Remake out/
    if os.path.exists("out/"):
        shutil.rmtree("out/")

    os.mkdir("out/")

    # Copy assets/
    shutil.copytree("assets/", "out/assets/")

    # Page groups
    writeups = build_group("writeups")


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
