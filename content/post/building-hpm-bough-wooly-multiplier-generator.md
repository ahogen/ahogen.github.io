---
title: "Notes on Building HPM Baugh-Wooley Multiplier Generator"
date: 2019-05-01
draft: false

# Tags and categories
# For example, use `tags: []` for no tags, or the form `tags: ["A Tag", "Another Tag"]` for one or more tags.
tags: ["blog"]
categories: []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image: "example.jpg"`.
# Use `caption` to display an image caption.
#   Markdown linking is allowed, e.g. `caption: "[Image credit](http://example.org)"`.
# Set `preview` to `false` to disable the thumbnail in listings.
header:
  image: "projects/mult.jpg"
  caption: ""
  preview: true
---

This blog post may not make complete sense if read by itself. These are my notes
written while I was reading the HPM Baugh-Wooley Multiplier research papers and
figuring out how I would generate a multiplier in C++ code. So to make sense of
this, get a copy of the first paper in the list: "Multiplier Reduction Tree..."

Check out the [FFT Generator project](/project/fft-ip-core-generator/) where
this multiplier is intended to be used.

The papers:

- H. Eriksson, P. Larsson-Edefors, M. Sheeran, M. Själander, D. Johansson, M. Schölin. ["Multiplier Reduction Tree with Logarithmic Logic Depth and Regular Connectivity"](http://www.sjalander.com/research/pdf/sjalander-iscas2006.pdf). Proceedings of IEEE International Symposium on Circuits and Systems (ISCAS). Island of Kos, Greece, pp. 4-8, 21-24 May 2006.

- M. Själander and P. Larsson-Edefors. ["The Case for HPM-Based Baugh-Wooley Multipliers"](http://www.sjalander.com/research/pdf/sjalander-techreport-2008-08.pdf). Chalmers University of Technology, Sweden (2008).

- Jipsa Antony, Jyotirmoy Pathak. ["DESIGN AND IMPLEMENTATION OF HIGH SPEED BAUGH WOOLEY AND MODIFIED BOOTH MULTIPLIER USING CADENCE RTL"](http://doi.org/10.15623/ijret.2014.0308011). International Journal of Research in Engineering and Technology 03.08 (2014): 56-63. Web. 30 Jan. 2017.

--------------------------------------------------------------------------------

Note that the 2D array of partial products looks kind of like an inverted
pyramid. In the case of a 4-bit multiplier, where AAAA is the multiplicand
and BBBB is the multiplier, the partial product array is created like this:

```
                                 A3        A2        A1        A0
X                                B3        B2        B1        B0
--------------------------------------------------------------------
                              pp[0][3]  pp[0][2]  pp[0][1]  pp[0][0]
                    pp[1][3]  pp[1][2]  pp[1][1]  pp[1][0]
          pp[2][3]  pp[2][2]  pp[2][1]  pp[2][0]
pp[3][3]  pp[3][2]  pp[3][1]  pp[3][0]
```

But when we "flatten" the array, it looks like this:

```
   ^         ^         ^      pp[0][3]  pp[0][2]  pp[0][1]  pp[0][0]
   |         |      pp[1][3]  pp[1][2]  pp[1][1]  pp[1][0]
   |      pp[2][3]  pp[2][2]  pp[2][1]  pp[2][0]
pp[3][3]  pp[3][2]  pp[3][1]  pp[3][0]
```

```
pp[3][3]  pp[2][3]  pp[1][3]  pp[0][3]  pp[0][2]  pp[0][1]  pp[0][0]
          pp[3][2]  pp[2][2]  pp[1][2]  pp[1][1]  pp[1][0]
                    pp[3][1]  pp[2][1]  pp[2][0]
                              pp[3][0]
```

When we have an array of partial products to work with, we will group and
remove the elements which will be plugged into adders. The sum and carry
outputs of the adders will need to be appended to this array so that they may
be used in the next level of adders.

We start with the uppermost adder level, which always has two adders: one
half-adder and one full adder.

* Generate partial products (**PPs**) in inverted pyramid layout (as shown
  visually above)
* Determine how many levels of adders will be created
* Set `current_adder_level` to the total number of levels to be created
* Find tallest column. Call it `Cm`
* Set `col_left: Cm + 1`
* Set `col_right: Cm`
* Create two half-adders (**HAs**)
	* Inputs for first HA are in column `col_right` rows 0 and 1
	* Inputs for second HA are in column `col_left` rows 0 and 1
	* Change second HA to "FA1" adder. This is a modified full-adder which
      technically has 3 inputs but one of them is set to a constant '1' due to
      the Baugh-Wooley multiplier scheme. Because of this constant, some logic
      optimizations can be made, which is why the adder will be a separate,
      special module instead of a regular half or full adder.
* Remove the PPs just assigned to the adders from the array
* Flatten the array (slide the columns which now have empty elements "upwards")
* Insert sum of first HA at bottom of column `col_right`
* Insert carry of first HA at bottom of column `col_left`
* Insert sum of second HA at bottom of column `col_left`
* Insert carry of second HA at bottom of column `col_left + 1`>
* Decrement `current_adder_level`

Now that the top level half-adders have been created, we can begin to generate
the other full and half adders until there are only 2 levels in the
partial-product (PP) array.

* While number of PP rows is > 2
	* Increment ```col_left```
	* Decrement ```col_right```
	* Create HA with inputs at row 0 and 1 of ```col_right```
	* Remove the points at row 0 and 1 of ```col_right```
	* ```Flatten()```
	* Insert sum of HA at bottom of ```col_right```
	* Insert carry of HA at bottom of ```col_right + 1```
	* Set ```col_current: col_right```
	* While ```(col_current <= col_left)```
		* Create FA with inputs at row 0 and 1 of ```col_current```
		* Remove the points at row 0 and 1 of ```col_current```
		* ```Flatten()```
		* Insert sum of FA at bottom of ```col_current```
		* Insert carry of FA at bottom of ```col_current + 1```
		* Increment ```col_current```
	* Decrement ```current_adder_level```
