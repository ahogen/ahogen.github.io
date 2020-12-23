---
title: "Remotely Debug ARM Cortex with Segger Tools"
date: 2020-08-13
draft: false

#summary: """I recently discovered that Segger tools can be used remotely!"""

tags: ["blog", "tutorial"]
authors: ["alex"]

highlight: true
math: false

header:
  image: "banners/default.png"
  caption: "Image credit: [**elite001mm (Deviant Art)**](http://fav.me/d9qa7qz)"
  preview: false

# Featured image
# To use, place an image named `featured.jpg/png` in your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
# Set `preview_only` to `true` to just use the image for thumbnails.
image:
  placement: 1
  caption: "Workstation -> Host/Server -> JLink -> Target"
  focal_point: "Center"
  preview_only: false

---

- JLink v682b

- Connect your JLink debugger to the target microcontroller.
- Connect your JLink debugger to the server computer, via USB.
- Open port 19020/tcp on you server's firewall.
- Start `JLinkRemoteServer` 



- Open Ozone
- Choose chip model and core type
- Choose connection settings. In this example, I'm connecting to the server
  I just set up, so I'm going to use that server's IP address.
- Select your compiled binary.
- Use as normal! 


### SEGGER SWO Viewer with Remote Debugger


```shell
JLinkSWOViewer.exe -ip 192.168.1.123 -device MIMXRT1021DAG5A -swofreq 921600
```

