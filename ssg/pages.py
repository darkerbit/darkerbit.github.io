import json
import mistletoe


class Page:
    def __init__(self, source):
        self.source = source

        with open(source, "r") as f:
            self.meta = json.loads(f.readline())
            self.content = f.read().strip()

    @staticmethod
    def read(file):
        with open(file, "r") as f:
            content = f.read().strip()

        return content

    def save(self, dest):
        with open(dest, "w") as f:
            f.write(self.generate())

    def generate(self):
        raise NotImplementedError


class MdPage(Page):
    def generate(self):
        return f'''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{self.meta["title"]}</title>
    </head>
    <body>
        <h1>{self.meta["title"]}</h1>
        {mistletoe.markdown(self.content).strip()}
    </body>
</html>
'''
