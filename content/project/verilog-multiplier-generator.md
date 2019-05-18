+++
# Date this page was created.
date = "2019-03-17"

draft = true

# Project title.
title = "Verilog HPM-BW Multiplier Generator"

# Project summary to display on homepage.
summary = "Command-line utility to create custom-bitwidth multipliers."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = "projects/mult.jpg"

# Optional image to display on project detail page (relative to `static/img/` folder).
image = "projects/mult.jpg"

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["ip-core", "cpp", "system-verilog", "verilog"]

# Optional external URL for project (replaces project detail page).
#external_link = ""

# Does the project detail page use math formatting?
math = false

+++

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
