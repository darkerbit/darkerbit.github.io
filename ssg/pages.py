import json
import mistletoe
import subprocess
from datetime import datetime

from .pygments_renderer import PygmentsRenderer


generate_time = datetime.utcnow()
describe = subprocess.check_output("git describe --all --long", shell=True, encoding="utf-8").strip()

head = open("templates/head.html", "r").read().strip()


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
    template_no_update = "\n".join(x for x in template.split("\n") if not x.lstrip().startswith("{if_update}"))

    def generate(self):
        self.meta["datetime_create"] = datetime.fromisoformat(self.meta["creation_date"]).strftime("%B %d %Y at %H:%M")
        self.meta["datetime_update"] = datetime.fromisoformat(self.meta["update_date"]).strftime("%B %d %Y at %H:%M") if "update_date" in self.meta else ""

        template = self.template if "update_date" in self.meta else self.template_no_update

        return template.format(title=self.meta["title"], kind=self.kind, kind_url=f"/{self.group}/",
                               markdown=mistletoe.markdown(self.content, renderer=PygmentsRenderer).strip(),
                               timestamp_create=self.meta["creation_date"], datetime_create=self.meta["datetime_create"],
                               if_update="",
                               timestamp_update=self.meta["update_date"] if "update_date" in self.meta else "",
                               datetime_update=self.meta["datetime_update"],
                               timestamp_generate=generate_time.isoformat(), datetime_generate=generate_time.strftime("%B %d %Y at %H:%M"),
                               describe=describe, link=f"https://github.com/darkerbit/darkerbit.github.io/blob/main/{self.group}/{self.name}.md",
                               head=head)


class IndexPage(Page):
    template = open("templates/category.html", "r").read()
    page_template = open("templates/page.html", "r").read().strip()
    page_template_no_update = "\n".join(x for x in page_template.split("\n") if not x.lstrip().startswith("{if_update}"))

    def __init__(self, *args, files=[]):
        super().__init__(*args)

        self.files = files

    @classmethod
    def generate_page(cls, page):
        template = cls.page_template if "update_date" in page.meta else cls.page_template_no_update

        return template.format(link=f"/{page.group}/{page.name}.html", title=page.meta["title"], summary=page.meta["summary"],
                               timestamp_create=page.meta["creation_date"], datetime_create=page.meta["datetime_create"],
                               if_update="",
                               timestamp_update=page.meta["update_date"] if "update_date" in page.meta else "",
                               datetime_update=page.meta["datetime_update"])

    def generate(self):
        return self.template.format(title=self.kind, markdown=mistletoe.markdown(self.content, renderer=PygmentsRenderer).strip(),
                                    pages='\n'.join(self.generate_page(x) for x in self.files),
                                    timestamp_generate=generate_time.isoformat(), datetime_generate=generate_time.strftime("%B %d %Y at %H:%M"),
                                    describe=describe, link=f"https://github.com/darkerbit/darkerbit.github.io/blob/main/{self.group}/{self.name}.md",
                                    head=head)
