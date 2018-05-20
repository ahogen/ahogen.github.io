+++
title = "Install Guild Wars 2 in Linux Mint"

summary = """
Only N steps away from visiting Tyria on an open-source OS!
"""

draft = true
date = "2017-07-06"
lastmod = "2018-03-13"

tags = ["blog", "tutorial", "julia-lang"]
highlight = true
math = false

[header]
image = "https://d3b4yo2b5lbfy.cloudfront.net/wp-content/uploads/2016/11/502022016-04_SpringQ2Update_HomeBanner.jpg"
caption = "Image credit: [**ArenaNet Guild Wars 2 Concept Art**](https://www.guildwars2.com/en/media/concept-art/)"
preview = true
+++

Looking to play an awesome open-world [MMO](https://en.wikipedia.org/wiki/Massively_multiplayer_online_game) on your 
open-source machine? Well you most certianly can play Guild Wars 2 on Linux!

{{% toc %}}

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
of which the old Wine is a dependancy. Since I was starting with a clean Mint
install, I did not have anything to uninstall.

Once Wine has been fully removed from your system, run these commands.

I use the official Wine install instructions, avaliable here: [https://wiki.winehq.org/Ubuntu](https://wiki.winehq.org/Ubuntu)
but I have also duplicated then below for convenience.

```
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

- Download Windows 64-bit installer

- Run installer with Wine
- [Optional] After installed and GW2 starts downloading packages, close.
- [Optional] Copy existing install, with `GW2.dat` file (normally 35GB+)

For slightly better performance, turn off debugging messages with 

```
export WINEDEBUG=-all; export LOGFILE=/dev/null;
```
