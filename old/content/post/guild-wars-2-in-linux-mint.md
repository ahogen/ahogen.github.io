+++
title = "Install Guild Wars 2 on Linux Mint"

summary = """
Only a few steps away from visiting [Tyria](https://wiki.guildwars2.com/wiki/Tyria_(world)) on an open-source OS!
"""

draft = false
date = "2018-04-30"
tags = ["blog", "tutorial"]
authors = ["alex"]

highlight = true
math = false
toc = true

[header]
image = "https://d3b4yo2b5lbfy.cloudfront.net/wp-content/uploads/2016/11/502022016-04_SpringQ2Update_HomeBanner.jpg"
caption = "Image credit: [**ArenaNet Guild Wars 2 Concept Art**](https://www.guildwars2.com/en/media/concept-art/)"
preview = true
+++

Looking to play an awesome open-world [MMO](https://en.wikipedia.org/wiki/Massively_multiplayer_online_game) on your 
open-source machine? Well you most certianly can play Guild Wars 2 on Linux!

Here are my system specs. Note that I did not have to install or configure
any special graphics drivers. If you have an Nvidea or AMD/Radeon graphics
card, you may want to set up those 3rd party drivers before attempting this.

| -              | -                                        |
|----------------|------------------------------------------|
| **OS**         | [Linux Mint 18.3 "Sylvia"](https://www.linuxmint.com/rel_sylvia_cinnamon.php) (based on [Ubuntu 16.04](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes)) |
| **Processor:** | [Intel i7-4790K](https://ark.intel.com/products/80807/Intel-Core-i7-4790K-Processor-8M-Cache-up-to-4_40-GHz) |
| **Graphics:**  | (internal) Intel HD Graphics 4600 |


# Step 1: Get and install Wine

**IMPORTANT:** Remove any previous Wine install, including any package
of which the old Wine is a dependency. Since I was starting with a clean Mint
install, I did not have anything to un-install.

Once Wine has been fully removed from your system, run these commands.

I used the official Wine install instructions, available here: [https://wiki.winehq.org/Ubuntu](https://wiki.winehq.org/Ubuntu)
but I have also duplicated them below for convenience.

```bash
# If your system is 64-bit, like mine, enable 32-bit architecture
sudo dpkg --add-architecture i386

# Add Wine repository key
wget -nc https://dl.winehq.org/wine-builds/Release.key
sudo apt-key add Release.key

# Add Wine repository
# On Linux Mint 18.x, use this line. It is different for Mint 17.x.
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'

# Update your packages list
sudo apt-get update

# Install Stable branch of Wine
sudo apt-get install --install-recommends winehq-stable
```

# Step 2: Get and install Guild Wars 2

- [Download the Guild Wars 2 Windows installer](https://account.arena.net/welcome) ("Gw2Setup(-64).exe") from the ArenaNet website. If you don't have an account yet, you'll want to [create one](https://account.arena.net/register?alt=gw2) there on the website as well.
- Run installer with Wine (e.g. `wine64 "~/Downloads/Gw2Setup-64.exe"`)
- Follow the installer's instructions.


{{< figure src="/img/post/gw2-client-downloading-dat-file.jpg" title="GW2 client downloading data file(s)" >}}

If you've already downloaded and installed GW2 on another machine, you can **save
time** by using that large (~35GB) data file from the old install, in the new
installation. Otherwise, the client will download this file for you.

- After the game is installed and starts downloading packages (shown above), **close it**.
- From the old/existing install **find the `Gw2.dat` file** (again, normally about 35GB). You'll find this in the GW2 install directory, such as "C:/Program Files/Guild Wars 2/".
- **Copy** that file into the new install directory, right next to the "Gw2-64.exe" file. If there is an existing `Gw2.dat` file which is rather small, copy over (replace) it with our larger one. It was the file being downloaded before we closed the application.
- Now **launch GW2** (e.g. `wine64 "/home/username/bin/Guild Wars 2/Gw2-64.exe"`). After a few moments, and possibly downloading any updates, it should open to the login screen!


This is all I had to do to get started. However, you can improve performance
a little bit by turning off debugging messages in wine. I made a launch 
script to do this for me.

```bash
#!/bin/bash

# https://us.download.nvidia.com/XFree86/Linux-x86/319.32/README/openglenvvariables.html
#export LD_PRELOAD="libpthread.so.0 libGL.so.1";
#export __GL_THREADED_OPTIMIZATIONS=1;

# Disable all Wine debug output, both to the terminal and to any log files
# https://wiki.winehq.org/Debug_Channels
export WINEDEBUG=-all;
export LOGFILE=/dev/null;

# GW2 Client cmdline args are documented here:
# https://wiki.guildwars2.com/wiki/Command_line_arguments
# "-dx9single" is common for Wine
# I find "-mapLoadInfo" to be kind of nice as well.
wine64 "/home/username/bin/Guild Wars 2/Gw2-64.exe" -dx9single -mapLoadInfo
```

From here, it's up to you to try out settings that may or may not improve
performance on your system. I don't have a gaming setup at all. Heck, the
embedded graphics in my CPU uses shared RAM even. Even so, I get a solid
30 FPS. This is about 10 FPS less than running GW2 on Windows on the same
machine. I find the game very playable nonetheless.

You may find lots of helpful info on the Guild Wars 2 Wiki pages.

- https://wiki.guildwars2.com/wiki/Guild_Wars_2_on_Wine

I hope this was useful! Feel free to let me know in the comments if I missed
something.

Cheers!
