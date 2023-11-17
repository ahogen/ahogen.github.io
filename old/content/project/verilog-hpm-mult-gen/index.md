---
draft: true
date: "2019-03-17"
title: "Verilog HPM-BW Multiplier Generator"
summary: "Command-line utility to create custom-bitwidth multipliers."
tags:
  - ip-core
  - cpp
  - system-verilog
  - verilog
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

# Optional external URL for project (replaces project detail page).
#external_link: ""

math: false
---

<!-- ![FFT IP Core banner image](/img/banners/fft-ip-core.png) -->
{{% alert note %}}
This tool was created while building the <a href="/project/fft-ip-core-generator/">FFT IP Core Generator</a>
project. Go look at that project as well!
{{% /alert %}}
-----

Baugh-Wooley

## TODO

- Warn that large-ish multipliers might take a minute to generate
- SystemVerilog support
- Output FPGA resources information, like number of AND/OR gates, and estimated
  delay (in LUTs).
