import ssg
import sys
import http.server
import socketserver


def build():
    pass


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
