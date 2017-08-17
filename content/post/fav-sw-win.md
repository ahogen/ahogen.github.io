+++
draft = false
date = "2017-08-17"
title = "Favorite Software: Windows"
tags = ["blog", "fav-sw"]
highlight = true
math = false
summary = """
Useful engineering-ish tools I use in Windows (7).
"""

[header]
  caption = "Image credit: [**Material Snowcaps**](http://7bna.net/images/material-wallpaper/material-wallpaper-22.jpg)"
  image = "banners/default.png"
  preview = false

+++

This is a (growing) list of some technical software I use on my Windows machines. I'm basically only using Windows 7, so I'm not sure how good or bad these programs are on a Windows 10 setup. 

## Text Editors

- **[Notepad++](https://notepad-plus-plus.org/download):** Great syntax-highlighting editor with lots of super helpful tools and plugins. Currently 32-bit handles plugins better than 64-bit for some reason.


- **[Atom](https://atom.io/):** A little heavy-weight and can be slow at times, but I still like how it looks. Having a folder/project view is very nice in some settings. Also, I'm not savvy enough with VIM and still prefer to click things if I need to.


- **[(g)VIM](http://www.vim.org/download.php):** If you use EMACS, you can just go pluck yourself. ;-)

## SSH/Serial Terminals

- **[RealTerm](https://sourceforge.net/projects/realterm/?source=navbar):** Awesome for dumping serial UART data to/from text files. I also really like the activity indicators.


- **[PuTTy](http://www.putty.org/):** Very basic interface, but interface with SSH, telnet, or serial (COM) ports. If you just need a simple SSH client or serial terminal emulator, this is my go-to.

## C/C++ Specific Tools

- **[Code::Blocks](http://www.codeblocks.org/):** Favorite C/C++ IDE. It wasn't too hard for me to get up and running with it after being taught C++ in college inside of Visual Studio. Free and open source. It also works great on Linux, so you can work on projects on both Windows and Linux platforms seamlessly, which is imperative for a lot of the work I do.


- **[clang (via LLVM Project)](https://clang.llvm.org/):** is actually a suite of (super) useful tools and utilities for C/C++ code. Two of the tools I use the most are:

    - **clang-format:** formats your code, allowing you to focus more on code implementation instead of formatting all the time.

    - **clang-tidy:** is a static-analysis [linter tool](https://en.wikipedia.org/wiki/Lint_(software)), checking for syntax errors or bugs in your code.

- **[Valgrind](http://valgrind.org/info/tools.html):** Is another suite of tools, like LLVM (clang). Most of them will run your pre-compiled program inside a sort of sandbox/container and monitor what it does. A few (not all!) of these tools are listed below.

    - **Memcheck:** Various memory-related analysis checks

    - **Cachegrind:** A cache (L1, L2, etc.) profiler

    - **Massif:** A heap profiler

    - **Helgrind:** A thread debugger, very useful in finding race conditions in multithreaded programs. I used it once and was a little overwhelmed, but I was probably not using it correctly, haha. I try to stay out of the multi-threaded/multi-process land as much as possible.

## Miscellaneous

- **[DoxyGen](http://www.doxygen.org/):** is a widely used code documentation tool. I had never used a documentation generator like this before (2016) and had always written documentation external to my code and code's comments. I found it pretty simple to get started with and it's saved me tons of time, keeping documentation close to the code implementation, so that the documentation tends to stay more up to date. Having export functionality to HTML and PDF (via LaTeX) is perfect for my needs.

- **[TeXstudio](http://www.texstudio.org/):** I use [MikTeX](https://miktex.org/) on Windows for the actual LaTeX backend. Works on Linux as well (I use [TeX Live](https://www.tug.org/texlive/) instead of MikTex on Linux).

- **[Spyder (in WinPython)](https://winpython.github.io/):** Super simple install. Spyder is a little heavy/slow, but when I was newer to Python, having an IDE with linter features and an embedded console was really helpful. Also, just having an install which includes most scientific packages I'll ever need is super nice. Being a portable install always makes me happy as well.
