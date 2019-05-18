+++
# Date this page was created.
date = "2017-01-29"

# Project title.
title = "FFT IP Core Generator"

# Project summary to display on homepage.
summary = "A highly configurable FFT IP Core generator."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = "projects/icon-fft-ip-core-generator.jpg"

# Optional image to display on project detail page (relative to `static/img/` folder).
image = ""

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["ip-core", "cpp", "dsp", "system-verilog"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Does the project detail page use math formatting?
math = false

+++

![FFT IP Core banner image](/img/banners/fft-ip-core.png)

This project's goal is to make integrating a fast Fourier transform (FFT)
processing core into your project incredibly simple. If you are reading this,
then you are well aware of the many uses for an FFT in an FPGA. 

### Background ###

I was going to use an FFT core for my senior project, but I had a difficult time
integrating a proprietary FFT core. The User Guide for the core did not give me
enough detail for me to build a proper interface. Even if I could have gotten it
working, I didn't (and still don't) have the money to purchase a license for the
core, so it would be severely limited in its functionality.

My senior project research taught me a lot about FFT processing in a hardware 
platform, which got me thinking about how I could build my own core. However, I
didn't want to just make a single core for my own specific application, I wanted
the functionality of generating an FFT processor of any length and bit-width.
And that is how this FFT generator was born.

### Features ###

* Automatically calculates twiddle factors
* Uses a high-performance implementation of a Baugh-Wooley multiplier
    * Relatively new HPM reduction tree architecture [^A]
	* Good compromise between power usage and speed
	* Faster than conventional Baugh-Wooley multiplier [^B]
	* Faster than HPM Modified Booth multiplier [^B]
* Length and width can be (nearly) any number
* Generates clean, clear [SystemVerilog](https://en.wikipedia.org/wiki/SystemVerilog) code

[^A]: H. Eriksson, P. Larsson-Edefors, M. Sheeran, M. Själander, D. Johansson, M. Schölin. ["Multiplier Reduction Tree with Logarithmic Logic Depth and Regular Connectivity"](http://www.sjalander.com/research/pdf/sjalander-iscas2006.pdf). Proceedings of IEEE International Symposium on Circuits and Systems (ISCAS). Island of Kos, Greece, pp. 4-8, 21-24 May 2006.

[^B]: Jipsa Antony, Jyotirmoy Pathak. ["DESIGN AND IMPLEMENTATION OF HIGH SPEED BAUGH WOOLEY AND MODIFIED BOOTH MULTIPLIER USING CADENCE RTL"](http://doi.org/10.15623/ijret.2014.0308011). International Journal of Research in Engineering and Technology 03.08 (2014): 56-63. Web. 30 Jan. 2017.

### Architecture ###

With the guidance of [George Slade's paper](https://www.researchgate.net/publication/235995761_The_Fast_Fourier_Transform_in_Hardware_A_Tutorial_Based_on_an_FPGA_Implementation), along with some other internet resources, I have been working on an object-oriented, **C++** library to configure and generate **SystemVerilog** compatible modules for use in *any vendor's* FPGA.

The FFT core uses a custom-built multiplier. Specifically, a SystemVerilog implementation of the HPM-based Baugh-Wooley multiplier, as researched by H. Eriksson, P. Larsson-Edefors, M. Sheeran, M. Sjalander, D. Johansson, and M. Scholin. Refer to their paper [*Multiplier Reduction Tree with Logarithmic Logic Depth and Regular Connectivity*](http://www.sjalander.com/research/pdf/sjalander-iscas2006.pdf) for more information. I have contacted Mr. Sjalander and received permission to impliment their multiplier design.

### Status ###

| Component Name         | C++ Code Written | C++ Code Tested | SV Synthesizes | SV ModelSim Simulation Test |
|------------------------|------------------|-----------------|----------------|-----------------------------|
| ROM                    |![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/chk.png)| ![picture](/img/chk.png) |
| Twiddle ROM            |![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/chk.png)|
| Multiplier             |![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/chk.png)|
| RAM                    |![picture](/img/chk.png)|![picture](/img/chk.png)|![picture](/img/spinner.gif) |![picture](/img/x.png)|
| 2-port RAM             |![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|
| Butterfly Unit (BFU)   |![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|
| Top-level module       |![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|
| (op) Kogge-Stone Adder |![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|![picture](/img/x.png)|

### More Information ###

The project is developed in a GIT repository. Right now, the repository is
hidden/private, but when I make it public, you will be able to access it at the
following URL.

* [https://gitlab.com/ahogen/PLD-FFT-Gen](https://gitlab.com/ahogen/PLD-FFT-Gen)

------