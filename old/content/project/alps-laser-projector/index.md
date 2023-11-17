---
draft: false
date: "2016-06-04" 
title: "ALPS Laser Projector"
summary: "Signage from the Mountaintops"
tags:
  - cpp
  - microcontroller
authors: ["alex"]

# Featured image
# To use, place an image named `featured.jpg/png` in your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
# Set `preview_only` to `true` to just use the image for thumbnails.
image:
  placement: 1
  caption: ""
  focal_point: "Center"
  preview_only: false

gallery_item:
  - album: gallery
    image: /projects/alps-case-3.jpg
    caption: The ALPS projector 
  - album: gallery
    image: /projects/alps-case-1.jpg
    caption: The ALPS projector (2)
  - album: gallery
    image: /projects/alps-laser-chalk-dust.jpg
    caption: Laser with chalk dust in the air
  - album: gallery
    image: /projects/alps-laser-chalk-dust-clock.jpg
    caption: Laser with chalk dust in the air (2)
  - album: gallery
    image: /projects/alps-night-hill-projection.jpg
    caption: Nighttime distance projection test, onto the OIT hill
  - album: gallery
    image: /projects/alps-night-hill-hi-mom.jpg
    caption: Nighttime distance projection test, onto the OIT hill
  - album: gallery
    image: /projects/alps-laser-projector-distance-google-maps.png
    caption: Approximate projection distance measured with Google Maps


# Optional external URL for project (replaces project detail page).
external_link: ""

# Does the project detail page use math formatting?
math: false
---

{{% toc %}}

This was the junior project for my undergraduate degree. Four of us students 
designed and built this project. It was later used by OIT faculty in a few 
highschool recruiting sessions.

Below is some marketing-style documentation for our "product." 

----


### Background


The acronym ALPS stands for Amplified Light Projection System. ALPS is
built for long-distance, high-powered alphanumeric projection applications. The
system controller rotates two separate mirrors (see Figure 1) to direct a laser
beam rapidly across any projection surface. This rotation occurs quickly enough
to create lines and shapes with the laser dot. This phenomenon is known as
[persistence of vision](https://en.wikipedia.org/wiki/Persistence_of_vision)
(POV) and has been used for decades in things like flip books as a means to 
create motion pictures and animations.

### Features

ALPS has a number of key features which set it apart from other signage
systems on the market today. Some of these features are listed below.

- Visible at over 1000 feet [^A]
- Text is laser-thin so that your signage will always appear crisp and clean
- Adding custom logos and typefaces is quite simple
- Advanced, quiet cooling system ensures the hardware will never overheat
- Text is entered with an IR keyboard

With these features, this system is sure to meet many of your long distance
signage needs, including requirements you may not know you have yet.

[^A]: Long-distance test was performed after sunset. Projection may not be 
visable at this range during daylight hours.


### Hardware Architecture

Below is an overview of the hardware components used in this project:

- 100mW green laser (yes, this will burn your skin!)
- Laser galvanometer
- TI Tiva C Launchpad (EK-TM4C123GXL)
- Yamaha RCX IR remote 
- IR receiver
- MAX5322 dual bipolar output DAC for contolling the galvos
- (+/-)15V DC power supply, and various step-down linear voltage regulators
- Temperature sensors
- Plexiglass graciously donated by [Basin Glass and Aluminium](http://basinglassandaluminum.com)

### Images

{{< gallery >}}