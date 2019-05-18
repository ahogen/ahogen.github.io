+++
draft = true
date = "2017-07-06"
title = "Include PWD in Julia Script"
tags = ["blog", "tutorial", "julia-lang"]
highlight = true
math = false
summary = """
You too can include modules from your present working directory
"""
[header]
image = "banners/default.png"
caption = "Image credit: [**elite001mm (Deviant Art)**](http://fav.me/d9qa7qz)"
preview = false
+++

I've been writing a little code in Julia lately and had an issue where I needed to include some modules I wrote, which were sitting in the same directory as my "main" script. You would think that Julia would search the current directory as well as any of it's normal include paths for the requested module, but it seems to only do the latter right now (as of release v0.6.0). This means any installed packages/modules, probably imported using `Pkg.add()` will work fine, but modules in your present working directory won't be found.

The fix is obvious: Have some way to append the pwd to the Julia module/package search path at runtime. There are two ways to do this.

1. Put some command in your `juliarc.jl` file
2. Put some command at the top of your main Julia script

While I have only used the latter, the former should work just the same, from what I understand.

The specific command I have been using is very simple, shown below.

```python
push!(LOAD_PATH, pwd())
```

Have a look at the Julia documentation for the elements in the above command.

- [push()](https://docs.julialang.org/en/stable/stdlib/collections/#Base.push!)
- [LOAD_PATH](https://docs.julialang.org/en/stable/manual/environment-variables/#JULIA_LOAD_PATH-1)
- [pwd()](https://docs.julialang.org/en/stable/stdlib/file/#Base.Filesystem.pwd)

Pop that onto the top of your script (or your `juliarc.jl` file) and you'll be on your way! All `using <module name here>` statements should work just fine, provided your modules are set up correctly. Don't forget to `export`!
