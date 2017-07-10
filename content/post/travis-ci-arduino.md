+++
date = "2017-01-29T16:30:00"
draft = true
image = "banners/default.png"
hide_banner_in_list = true
tags = ["blog", "tutorial", "fpga", "system-verilog"]
title = "Build and test Arduino Code with Travis-CI"
math = true
summary = """

"""

[header]
image = "banners/default.png"
caption = "Image credit: [**elite001mm (Deviant Art)**](http://fav.me/d9qa7qz)"
preview = false

+++

If you aren't familiar with Travis CI from the Github team, go check it out here: https://travis-ci.org. It's completely free for open source projects, which is awesome! I won't bother telling you what Travis or a continuous integration tool is used for if you don't already know. That topic is covered very well by some other fine folks at Thought Works. Check out [their article on CI here](https://www.thoughtworks.com/continuous-integration).

Even if you don't **need** CI right now, it could be a good idea to play with it now, in a very simple project, just so you get used the concept. That's what I did with a rather simple Arduino library I built and I wanted to share my Travis CI integration experience with you.

## What you need

- A working Arduino project, checked into a Github repository
- A Travis CI account (just sign in with your Github account)
- If your Arduino code is a library, like mine was, you should really have a couple example projects that use your library. At least one of them should use **all** methods, functions, and features of the library.

## Getting started

Assuming you have 