+++
title = "A Two-Column Spec Sheet Table in LaTeX"

summary = """
Writing a specifications section of a technical datasheet? This could help!
"""

draft = false
date = "2019-03-07"
tags = ["blog", "latex"]
authors = ["alex"]

highlight = true
math = false

[header]
image = "banners/default.png"
caption = "Image credit: [**elite001mm (Deviant Art)**](http://fav.me/d9qa7qz)"
preview = false
+++

- [LaTeX Code](#latex-code)

Many datasheets I've seen tend to use a two-column layout. I'm no professional
typesetter and I haven't looked into why this is (is it easier for our eyes to
read shorter lines?), but it does look nice.

Recently I was writing some documentation and needed to generate a section
for device specifications. Here's what I came up with. It's a nested table. 
I use the outer table simply to split the page into two columns. I then use two
separate tables, one in each column, for the content.

Here's an example of this layout:
{{< figure src="/img/post/latex_twocol_spec_table.jpg" title="LaTeX rendered output" >}}

## LaTeX Code

And here's how I made it.

Notice the `[t]` in both `tabularx` tables. This aligns the tables to the 
**t**op. Without this, I found that the tables would not be aligned, vertically,
with each other.

Got a better way of doing this? I'd love to know in the comments!

```latex
\documentclass[10pt, english, letterpaper]{article}
\usepackage[utf8]{inputenc}

\usepackage[%
    letterpaper,
    %includeheadfoot,
    head=\baselineskip,  % distance from bottom of header to block of
    % text aka \headsep e.g. \baselineskip
    foot=2.3cm,          % distance from top of footer to block of text aka \footskip
    headheight=13.7pt,   % height for the header block (no equivalent for footer)
    %heightrounded,      % ensure an integer number of lines
    marginparwidth=2cm,  % right marginal note width
    marginparsep=2mm,    % distance from text block to marginal note box
    %height=\textheight, % height of the text block
    %width=\textwidth,   % width of the text block
    top=2.0cm,           % distance of the text block from the top of the page
    bottom=1.5in,
    left=0.6in,
    right=0.6in,
    %showframe,          % show the main blocks
    %verbose,            % show the values of the parameters in the log file
]{geometry}

\usepackage{array}
%\usepackage{booktabs}    % Good/better tabular typography
\usepackage{multicol}    % Multi-column page layouts
\usepackage{tabularx}

% TABLE TWEAKS
\setlength\extrarowheight{2pt} % Extra padding in tables.
\newcommand{\tabindent}{\hspace{4.0mm}} % Horizontal space, often used in tables
                                        % as a <TAB> character

\begin{document}

\begin{tabular}[t]{|p{0.475\linewidth} p{0.475\linewidth}|}
\hline
\begin{tabularx}{1\linewidth}[t]{>{\raggedright}X r}

    \textbf{Spec a} & 1234 \\
    
    \textbf{Spec b} & 5678 [unit] \\
    
    \textbf{This was a good measurement} & 12.34 [unit] \\
    
    \textbf{We can do this} & \\
    \tabindent From 123, we get & 123 \\
    \tabindent From 456, we get & 456 \\
    
\end{tabularx}
&
\begin{tabularx}{1\linewidth}[t]{>{\raggedright}X r}
    
    \textbf{Options on New Line} & \\
    \multicolumn{2}{r}{A, B, C, D} \\
    \multicolumn{2}{r}{E, F, G, H, I} \\
    
    \multicolumn{2}{l}{\textbf{Many Options}} \\
    \multicolumn{2}{r}{1, 2, 3, 4, 5, 6, 7} \\
    
    \textbf{Standards Compliance} & \\
    \tabindent IEEE Std. 123.45 & Yes  \\
    & (we think) \\
    \tabindent UL safety stuff & Yes yes... \\
    
\end{tabularx} \\ \hline
\end{tabular}

\end{document}
```
