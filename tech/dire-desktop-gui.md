{"title": "(Draft) The dire state of desktop GUI and how to deal with it", "summary": "a.k.a. why using Electron for everything is a bad idea", "creation_date": "2022-11-17T12:34:07.736571"}

# WIP

Table of contents:
1. [What is Electron?](#electron)
2. [Problem 1: JavaScript](#javascript)

---

It's the year of our lord 2022.
[Discord](https://discord.com) and [WhatsApp](https://www.whatsapp.com/), two of the most popular internet messaging applications, are Electron-based.

[Visual Studio Code](https://code.visualstudio.com/), a very popular text editor, and [Atom](https://atom.io/), a less popular one are both Electron-based.

Hell, even stuff like [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) is Electron-based now.

How did we get here?

---

<h2 id="electron">What is Electron?</h2>

![Electron logo](/assets/article/dire-desktop-gui/Electron_Software_Framework_Logo.svg.png)

(Pictured: Electron's logo.)

[Electron](https://www.electronjs.org/) is a toolkit that allows you to build desktop applications with the
same workflow as frontend web development, so HTML, CSS and JavaScript.

If that sounds appealing to you, I advise you click off because I'm going to spend the rest of the article bashing it!

Electron is a essentially a web browser (more specifically, [Chromium](https://www.chromium.org/Home/)) without the UI.
An Electron app is a website that the Electron runtime runs.

This sounds fine on paper, until you realise just how complicated and
confusing web development actually is, even without the added complexity of desktop GUI code.

---

<h2 id="javascript">Problem 1: JavaScript</h2>

[JavaScript](https://en.wikipedia.org/wiki/JavaScript) is an interpreted programming language that runs in internet browsers
in order to do logic, animation, things like that on the frontend (on the user's computer).

JavaScript is also a confusing mess with odd legacy bits and bobs scattered all over the place, standards that aren't
perfectly followed across all environments (even if you limit yourself to only the popular ones), and a very fragmented ecosystem.

JavaScript is also only designed to do what I described above: front-end logic and animation.
JavaScript was first invented to animate buttons, after all!

Electron, meanwhile, encourages usage of JavaScript for more rigid and performance-intensive program logic,
which leads to developers naively assuming that JavaScript is the be-all end-all solution for desktop development,
which it very much isn't.

## ends here for now lol
