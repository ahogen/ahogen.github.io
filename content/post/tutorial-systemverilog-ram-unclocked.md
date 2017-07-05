+++
draft = true
date = "2017-02-15T00:17:19-08:00"
title = "SystemVerilog RAM Module (un-clocked)"
tags = ["blog", "tutorial", "fpga", "system-verilog"]
highlight = true
math = false
summary = """
A brief tutorial on writing a SytemVerilog-compatible RAM module.
"""

[header]
  caption = ""
  image = "banners/default.png"
  preview = false

+++

A RAM module consists of a few different elements.

- Memory elements
- In/out data port to write and retrieve data
- Address input port to indicate which element we want to read/write
- Direction controls

I'll go through and explain each of these elements and we'll incrementally build a synthesizable RAM module.

{{% alert note %}}
A quick note before I get going: A lot of the SystemVerilog syntax I reference is pulled directly out of [*SystemVerilog for Design*](#sv-for-design) by Sutherland and friends. PLEASE go get this book if you intend to work with SystemVerilog at all. It's a fantastic reference. See footnote [[1]](#sv-for-design) for bibliographical information.
{{% /alert %}}

## Ports ##
----

Deciding what ports you're going to provide at the module interface means you have to decide how you want your RAM to work. First off, do you want synchronous or asynchronous RAM? This determines whether or not you need a clock input. We know we need an address input. Data input and output ports could be written as two separate ports, one in and one out, but this isn't common because it means you have more bus wires going through your design, which is unnecessary. Then of course you need a way to deal with switching between read and write operations...

We are going to build an un-clocked (combinational logic) RAM module. A common way to interface with RAM is with the following ports:

- CS -- chip select
- WE -- write enable
- OE -- output enable
- DAT -- tristate input/output port
- ADDR -- address

And then we would write our module ports one of two ways. The first declares only the names of the wires in the port list and then defines the port direction and width inside the module. The second defines direction, width, and name all in the module port list parenthesis. Here's the first one.

```verilog
// Older Verilog-1995 port declaration style

module ram(
	cs,
	we,
	oe,
	data,
	addr
	);
	
	input cs;
	input we;
	input oe;
	inout [X:0] data;
	input [Y:0] addr;
	
	// ... //
	
endmodule
```

And here's the second one.

```verilog
// Newer Verilog-2001 port declaration style

module ram(
	input cs,
	input we,
	input oe,
	inout [X:0] data,
	input [Y:0] addr
	);
	
	// ... //
	
endmodule
```

I normally prefer the second option because it keeps the port names and sizes in the same place, so I only have to look in one location to find out everything. Also if I decided to change a port name, I don't have to change it twice. It doesn't matter which one you choose. They both work the same.

*However*, for this tutorial, we are going to use the **first** (older) method, because of reasons you're about to see...

Don't worry, we'll fix the `X` and `Y` in a moment. I've put them there as placeholders for now.

## Parameterization ##
---

The idea here is to make our RAM module reusable. We can copy and paste this code, change only two numbers, and have a RAM module of a completely different size with very minimal effort. In C/C++ we might use global const variables for this purpose. In SystemVerilog, we're going to use something called a parameter.

If you didn't know, parameters are kind of like a global `const` variable in C languages. Parameters have to be declared *inside* of a SV module. A `parameter` can be redefined but a `localparam` cannot. See section 3.10 of [[1]](#sv-for-design). Treat them like you would a normal Verilog constant, such as `4'b0000`, except use the name instead of the number.

This is how you would create a parameter or localparam.

```verilog
parameter my_constant_a = 4'b0000;
localparam my_constant_b = 8'hF2;
```

For our purposes, I don't want to ever redefine the constants we declare, so I'm going to use a `localparam`. We are going to use constants to define the RAM width (word size) and address width. 

```verilog
module ram(
	cs,
	we,
	oe,
	data,
	addr
	);
	
	localparam RAM_WIDTH  = 7;
	localparam ADDR_WIDTH = 10;
	
	input cs;
	input we;
	input oe;
	inout [RAM_WIDTH:0]data;
	input [ADDR_WIDTH:0]addr;

	//** the rest of your module **//
	
endmodule
```

And now we've got parameters set up for a RAM module that has 1024 elements which are 8 bits wide. Notice that I replaced the `X` with RAM_WIDTH and `Y` with ADDR_WIDTH parameters. Again, this works similar to a `const` in C/C++, so the SV compiler will replace `RAM_WIDTH` with the number `7`.

The address bus width is not the same as the number of elements in the RAM (RAM length). However, the RAM `length can be computed by raising`  In this case, it should be wide enough for any number in the range 0 - 1024, which is 10 bits, as we put in the `ADDR_WIDTH`. 

Now we will need to compute that number for later use when we declare the RAM memory array. Remember that 2^n is equivalent to a binary number with a 1 at the nth place, and all other bits set to 0. This is pretty easy to compute using a left-shift operator. If we want 1024, then shift 1 to the left 10 times. Let's define a new parameter which will hold this number for us.

```verilog
localparam RAM_LENGTH = 1 << ADDR_WIDTH;
```
We will be using this parameter in the next step, so hang tight.

{{% alert note %}}
You may know about system tasks like `$clog2()` which would be the perfect tool for computing the number of bits required, given the RAM length. Unfortunately, to my knowledge many system tasks are not synthesizable. They will often work in a test bench, but they won't end up in any compiled design for real hardware. If your compiler does indeed support `$clog2()`, then fantastic! Include it here and let me know about it, because I'd love to be able to use it in synthesisable designs!
{{% /alert %}}

## Memory Array ##
----

Memory elements are easy to construct in SystemVerilog (SV) by using an array. There are two kinds of arrays we can create in SV. The difference between the two is in how they are physically created/stored in the target device. We can choose to use either *packed* arrays or *unpacked* arrays. Previous versions of Verilog support 1-dimensional packed arrays which were called vectors. SystemVerilog now allows for multi-dimensional vectors and refers to them as packed arrays, because the bits are stored as contiguous bits (section 5.3.2 in [[1]](#sv-for-design)).

Unpacked arrays have been multi-dimensional since the Verilog-2001 standard and, unlike packed arrays, each element of the array might be stored independent of other array elements. This does not add any complexity in the syntax you have to use to access array elements, it's just something to keep in mind when designing your module. However, if you intend to build a dual-port / two-port ROM module, then unpacked arrays may not be for you as Sutherland indicates that Verilog will (should) produce an error if more than one single array element is accessed at once (p. 144 of [[1]](#sv-for-design)). Since this tutorial only deals with single-port RAM, this isn't an issue for us.

For this tutorial, I'm going to use the more common, *unpacked* array type. The syntax for instantiating an unpacked array is as follows:

```verilog
logic [ bits_per_element ] name [ number_of_elements ];
```

So if I want 16 elements, each with 8 bits in them, I might write this....

```verilog
logic [7:0] ram_mem [0:15];
```

Note that it is always a good idea to initialize your memory. In SV, you put your initialization value(s) in curly braces preceded by an asterisk `'{<init_vals>}`. You must provide a value for every element unless you use some number replication tricks. I currently prefer using the SystemVerilog `default` keyword, but there are a few other ways to do it that are more C-like. Please read section 5.3.4 of *SystemVerilog for Design* for more info [[1]](#sv-for-design).

With that in mind, I'm going to initialize our RAM memory to all zeros like this...

```verilog
logic [7:0] ram_mem [0:15] = '{default:7'h0};
```

Great. Now we have a storage array to save and read information to/from. However, this brings me to parameterization.

As people who code, we tend to be inherently lazy, to some extend. I mean, we are in fact programming electrical logic to do things for us. So what if we wanted to change the size of our RAM module. Gee, wouldn't it be nice to copy and paste our code and only have to change a parameter or two? Hmm...

## Final Design ##
---

And here is our final design we put together! Not bad, eh? Like I said before, this is just *one* way of writing a RAM-like module. There are many different ways to build a RAM module, depending on how you want to interface with it. 


```verilog

module RAM_8_1024(
  CS,
  WE,
  OE,
  Data,
  Addr
  );

  localparam RAM_WIDTH = 7;     // Word size (RAM element width)
  localparam RAM_LENGTH = 1023; // Number of words (RAM length)

  input CS;                     // Chip select
  input WE;                     // Write enable
  input OE;                     // Output enable
  inout [RAM_WIDTH:0] Data;     // Data input and output lines
  input [______________:0] Addr;             // Address lines

  // Memory block
  logic [RAM_WIDTH:0] ram_mem [0:RAM_LENGTH] = '{default:RAM_WIDTH'h0};

  // Bi-directional data port direction control
  // including READ functionality
  assign data = (~CS && ~OE) ? ram_mem(Addr) : {RAM_WIDTH{1'bz}};

  // WRITE functionality
  always @ (CS or WE)
  begin
    if (!CS && !WE) 
    begin
      ram_mem[Addr] = Data;
    end
  end

  // Display error in simulation if control signal conflict
  always @ (WE or OE)
  begin
    if (!WE && !OE) 
    begin
      $error("Operational error in RAM module: OE and WE are both active at time %0t", current_time);
    end
  end
	
endmodule

```

I hope this was helpful to you. If you liked this tutorial or you have any questions, feel free to hit me up on Twitter or any of the other sites I listed on the [front page](/) of this site. 

Cheers!

## References ##
----

<a name="sv-for-design">
[1]</a>: S. Sutherland, S. Davidmann and P. Flake, [*SystemVerilog for Design*](https://books.google.com/books?id=EeIVYPd9iDAC&dq=systemverilog+for+design&source=gbs_navlinks_s), 2nd ed. Springer Science & Business Media, 2006. 418 pp., ISBN: 9780387364957

