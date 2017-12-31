+++
draft = false
date = "2017-12-30"
title = "Launch PuTTY in UART mode on Linux (Ubuntu)"
tags = ["blog", "tutorial"]
highlight = true
math = false
summary = """
Launch PuTTY in UART mode from command line on Linux.
"""

[header]
  caption = "Image credit: [**Material Snowcaps**](http://7bna.net/images/material-wallpaper/material-wallpaper-22.jpg)"
  image = "banners/default.png"
  preview = false

+++


I could not seem to remember the serial configuration string to start [PuTTY](http://www.putty.org/) with the correct baud rate and parity settings, so this is my way of jotting it down for myself and others like me. By default, PuTTY was ultra-tiny on my Linux Mint machine, so I change the font to a more normal 12pt font. I figured most people should have the "Ubuntu Mono" font, but maybe "Monospace Regular" would be better. 

```bash
putty /dev/ttyUSB0 -serial -sercfg 115200,8,n,1,N -fn "client:Ubuntu Mono 12" -geometry 90x100 -sl 500
```

(This command is all one long line.)

{{% alert note %}}
For this to work, either you must have root access or your user account has been added to the appropriate group(s) to access serial devices. On Debian/Ubuntu systems, this is normally the `dialout` group. To add yourself to `dialout`, run:

```
sudo usermod -a -G dialout ${USER}
```

You must log out of your account, then log back in for the new group permissions to take effect.
{{% /alert %}}

Let's break the PuTTY command (above) down. 

- `putty` name of the command
- `/dev/ttyUSB0` serial device, in my case a USB to UART adapter which was enumerated by my machine as USB0
- `-serial` use serial mode, not SSH or telnet modes
- `-sercfg` the serial configuration string (explained below)
- `-fn` specify the font (both typeface and pt size) of the PuTTY terminal
- `-geometry` specify the size (in number of character rows and columns) of the PuTTY terminal
- `-sl` number of scrollback lines PuTTY will remember


The `sercfg` string has the following meaning. The settings I've chosen should be the default for some common devices, like a [Raspberry Pi 3](https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/#Raspberry_Pi_3), however 9600 baud is also very common.

Setting Name  | Value
--------------|----------- 
Baud rate     | 115200
Data bits     | 8
Parity        | none
Stop bits     | 1 
Flow control  | none

Obviously I didn't make this stuff up. For more detailed information about launching PuTTY from the command line or any other PuTTY operation, check out the PuTTY documentation, available here: https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
