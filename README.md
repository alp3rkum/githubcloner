<img width="1110" height="624" alt="Ekran görüntüsü 2025-10-19 133030" src="https://github.com/user-attachments/assets/bc3b941f-0cb6-4d6b-92b2-3630c47f9af6" />

# Python Textual GitHub Cloner

A *user-friendly* terminal application to clone GitHub repos and branches.

## What Is This?

This application is a terminal user interface (TUI) application that automatizes the act of cloning a repo/branch from GitHub with the power of [Textual](https://textual.textualize.io/), a TUI framework made in Python to combine the featherweight architecture of a CLI (Command Line Interface) application with the visual beauty and easy usage of a GUI (Graphical User Interface), with the ease of Webpage styling (via Textual's own CSS) on top of it to result in simpler yet beautiful looking and functional terminal applications.

## How It Works?

This program takes one task, which is cloning a GitHub repo/branch, and makes it a very intuitive task that is as easy as a copy-paste & click. That's its whole purpose. You don't have to type it out character by character in a terminal (or ask AI how to do so), or go through a tab-bar and multiple menus of GitHub Desktop. Open the repo on GitHub, copy its link, paste it to the application, and click the "Clone" button.

If you want to clone a specific repo, you can just copy-paste the repo's full link (with /tree/branchname), and it will clone that specific branch too.

## What Do You Need?

* Python (this application was coded with 3.12.2)
* Textual library (pip install textual)
* Windows new Terminal (comes standard in Win11), or any terminal that is specified in Textual docs
* Pyinstaller (if you want to compile this application)

## What Does It Include?

The main application is a single module written in main.py. The module is about 100 lines, which is enough for all the functionalities it offers. There's also an app.tcss file for the style, colors, and general interface layout. All in all, this GitHub Cloner is an application with about 150 lines of code.
