+++
draft = false
date = "2013-09-22"
title = "PICAXE Microcontroller with Parallax Serial LCD Display"
tags = ["blog", "tutorial", "uc-picaxe"]
highlight = true
math = false
summary = """
Use the Parallax LCD display with a PICAXE microcontroller.
"""

[header]
  caption = "Image credit: [**Material Snowcaps**](http://7bna.net/images/material-wallpaper/material-wallpaper-22.jpg)"
  image = "banners/default.png"
  preview = false

+++

{{% alert note %}}
This tutorial originally appeared on my (Alex's) blog on Northwest Tech Experience (nwteche.com). That website has been removed. I have moved some of the content I wrote, including this page, to this website of mine. I may have edited the original content for clarity.
{{% /alert %}}

Do you want to add an LCD display to your [PICAXE](http://www.picaxe.com/) project? Do you have a limited number of output pins on your microcontroller? The [**Parallax 2x16 Serial LCD** (Backlit)](https://www.parallax.com/product/27977) display is a great solution!

The Parallax 2×16 serial LCD display has only 3 pins. Only one of those pins connects to the microcontroller. The other two are for power connections.

It turns out, Parallax has made it very easy to communicate with the LCD display with simple serial commands. You can test your display by using or modifying the [PICAXE](http://www.picaxe.com/) program I have written below.

{{% alert note %}}
To use the LCD display at the [PICAXE](http://www.picaxe.com/)’s default 4 MHz, the LCD will need to be set for a 2400 baud rate and the program will change from:

```basic
setfreq m16
symbol tx = c.4
symbol baud = T9600_16
```

…to…

```basic
setfreq m4
symbol tx = c.4
symbol baud = T2400_
```
{{% /alert %}}

The code below will test the serial communication, the display back-lighting (if applicable), and the on-board speaker/sound controls.

I hope this proves useful to somebody!

### Resources:

- [Parallax Serial LCD Display PDF manual](https://www.parallax.com/sites/default/files/downloads/27979-Parallax-Serial-LCDs-Product-Guide-v3.1.pdf)

--------
## Code

```basic
' ------------
'|  LCD Test  |
' ------------

'by Alexander Hogen

'Started: 9-16-2013
'Finished: 9-16-2013

'See "Command Set" in this PDF for
'more information.
'http://www.parallax.com/sites/default/files/downloads/27979-Parallax-Serial-LCDs-Product-Guide-v3.1.pdf

setfreq m16

'9600 baud only works in 16MHz or higher

'Multiply desired millisecond (ms) timing
'by 4 to get desired result.
'i.e. "Pause 5" becomes "Pause 20"

symbol tx = c.4
symbol baud = T9600_16

pause 400

main:
serout tx, baud,(22) 'Turn display on
pause 40
gosub clearLCD
serout tx, baud,(17) 'Turn backlight on

serout tx, baud,("Hello")

pause 4000

gosub clearLCD
serout tx, baud,("LCD works great!")

gosub beeps

end

clearLCD:

serout tx, baud, (12)
pause 40
return

beeps:

serout tx, baud,(216) 'Select the 4th scale (A=440Hz)
pause 40
serout tx, baud,(210) 'Set note length to 1/16 note
pause 40

serout tx, baud,(220,221,222,223,224,225,226,227)
pause 4000

return
```
