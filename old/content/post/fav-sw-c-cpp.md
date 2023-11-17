+++
draft = true
date = "2017-08-18"
title = "Favorite Software: C/C++ Tools"
tags = ["blog", "fav-sw"]
authors = ["alex"]

highlight = true
math = false
summary = """
Useful tools I use when developing or debugging C/C++ code.
"""

[header]
  caption = "Image credit: [**Material Snowcaps** by elite001mm](https://www.deviantart.com/elite001mm)"
  image = "banners/default.png"
  preview = false

+++

- **[Code::Blocks](http://www.codeblocks.org/):** Favorite C/C++ IDE. It wasn't too hard for me to get up and running with it after being taught C++ in college inside of Visual Studio. Free and open source. It also works great on Linux, so you can work on projects on both Windows and Linux platforms seamlessly, which is imperative for a lot of the work I do.


- **[clang (via LLVM Project)](https://clang.llvm.org/):** is actually a suite of (super) useful tools and utilities for C/C++ code. Two of the tools I use the most are:

    - **clang-format:** formats your code, allowing you to focus more on code implementation instead of formatting all the time.

    - **clang-tidy:** is a static-analysis [linter tool](https://en.wikipedia.org/wiki/Lint_(software)), checking for syntax errors or bugs in your code.

- **[Valgrind](http://valgrind.org/info/tools.html):** Is another suite of tools, like LLVM (clang). Most of them will run your pre-compiled program inside a sort of sandbox/container and monitor what it does. A few (not all!) of these tools are listed below.

    - **Memcheck:** Various memory-related analysis checks

    - **Cachegrind:** A cache (L1, L2, etc.) profiler

    - **Massif:** A heap profiler

    - **Helgrind:** A thread debugger, very useful in finding race conditions in multithreaded programs. I used it once and was a little overwhelmed, but I was probably not using it correctly, haha. I try to stay out of the multi-threaded/multi-process land as much as possible.

- **[DoxyGen](http://www.doxygen.org/):** is a widely used code documentation tool. I had never used a documentation generator like this before (2016) and had always written documentation external to my code and code's comments. I found it pretty simple to get started with and it's saved me tons of time, keeping documentation close to the code implementation, so that the documentation tends to stay more up to date. Having export functionality to HTML and PDF (via LaTeX) is perfect for my needs.
