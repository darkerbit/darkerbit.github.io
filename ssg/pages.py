import json
import mistletoe

from .pygments_renderer import PygmentsRenderer


class Page:
    def __init__(self, source, name, kind, group):
        self.source = source
        self.name = name
        self.kind = kind
        self.group = group
        self.dest = ""

        with open(source, "r") as f:
            self.meta = json.loads(f.readline())
            self.content = f.read().strip()

    @staticmethod
    def read(file):
        with open(file, "r") as f:
            content = f.read().strip()

        return content

    def save(self, dest):
        self.dest = dest

        with open(dest, "w") as f:
            f.write(self.generate())

    def generate(self):
        raise NotImplementedError


class MdPage(Page):
    template = open("templates/markdown.html", "r").read()

    def generate(self):
        return self.template.format(title=self.meta["title"], kind=self.kind, kind_url=f"/{self.group}/", markdown=mistletoe.markdown(self.content, renderer=PygmentsRenderer).strip())


class IndexPage(Page):
    def __init__(self, *args, files=[]):
        super().__init__(*args)

        self.files = files

    def generate(self):
        newline = '\n'

        return f'''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{self.kind}</title>
    </head>
    <body>
        <a href="/">Return home</a>
        <h1>{self.kind}</h1>
        {mistletoe.markdown(self.content, renderer=PygmentsRenderer).strip()}
        {newline.join([f'<a href="/{self.group}/{x.name}.html">{x.meta["title"]}</a>' for x in self.files])}
    </body>
</html>
'''
