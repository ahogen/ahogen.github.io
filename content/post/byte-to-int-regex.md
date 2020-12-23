+++
draft = true
date = "2017-07-06"
title = "Convert Text Bytes to Ints"
tags = ["blog", "tutorial", "regex"]
authors = ["alex"]

highlight = true
math = false
summary = """
Stop manually converting text bytes to 32-bit ints. Find and replace with regex!
"""
[header]
image = "banners/default.png"
caption = "Image credit: [**Material Design Snowcap** by elite001mm (Deviant Art)](https://www.deviantart.com/elite001mm)"
preview = false
+++

This is another post written as a reminder for myself. The below
[regular expression (regex)](https://en.wikipedia.org/wiki/Regular_expression)
converts a space-separated list of hex bytes, like `0x01 0x02 0x03 0x04` into a 
32-bit hex word, like `0x01020304`.

Copy and paste the below snippets into a text editor supporting regex, such as 
[Atom](https://atom.io/), [VS Code](https://code.visualstudio.com/), 
[Notepad++](https://notepad-plus-plus.org/), or most other modern text editors.

#### "Find" regex

```text
(0x\w{1,2})\s+0x(\w{1,2})\s+0x(\w{1,2})\s+0x(\w{1,2})
```

#### "Replace" regex

```text
$1$2$3$4, 
```

# Explanation

This regex will capture 4 groups of byte strings. It assumes the
following:

- All byte strings have a "0x" prefix
- All byte strings are only separated by white space
- There are always two hex-digits in each byte string. Meaning a zero
  should always look like "0x00" and not "0x0".

Notice how each byte is in a capture group. This means you can 
concatenate the 4 capture groups, resulting in a 32-bit hex string.

### Example:

Here is some example text you can use to try this regex.

```
0x01 0x7d 0x3d 0x00 
0xff 0xff 0xff 0xff 
0xfe 0xbe 0x7d 0x00 
0xff 0xff 0xff 0xff 
0xf9 0x1b 0x4c 0x00
```


Put the regex statement above into the "Find" box, and the statement 
below into the "Replace" box.

In the [Atom](https://atom.io/) text editor, you can access capture
groups with a dollar sign and the capture group number (see [Atom issue #351](https://github.com/atom/find-and-replace/issues/351)). In some other
editors, you might need to replace the dollar sign `$` with a backslash
`\\` in the "replace" string, to proprly use the regex capture group.


Now, clicking "Replace All" should result in the following
output:

```
0x017d3d00, 
0xffffffff, 
0xfebe7d00, 
0xffffffff, 
0xf91b4c00,
```