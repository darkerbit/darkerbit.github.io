# darkerbit's website

Hello, you've found the repository for [my website](https://darkerbit.github.io).

It's basically just a Python script that generates html files based on Markdown files.

The script is licensed under Zlib. The content of the web page is licensed under CC0.

## How do build and run?

First, [install Poetry](https://python-poetry.org/docs/), then install the dependencies with `poetry install`.

After that:

- `poetry run ssg build`: Build the website.
- `poetry run ssg timestamp`: Produce an UTC timestamp to use for article creation and update times.
