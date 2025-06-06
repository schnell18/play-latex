# Introduction

This document explores methods to convert LaTeX document to HTML with the aim
of publication on web. Both the [Engrafo][1] and [pdf2htmlex][2] is explored.
Engrafo doesn't convert two-colum layout properly. Converted table wrapped in
adjustbox doesn't display correctly. pdf2htmlex is a high fedility converter,
the HTML output reproduces the same display quanity of its PDF counterpart.
However, the pdf2htmlex is challenging to build on unsupported platform as it
depends on the internal APIs of its dependencies.

## Convert the TAI paper using Engrafo

~~~~bash
cd ~/study/aut/master-thesis/srs/ieee-tai
podman run \
    -v "$(pwd)":/workdir \
    -w /workdir \
    arxivvanity/engrafo engrafo \
    paper.tex html/
~~~~

## Convert the TAI paper using pdf2htmlex

~~~~bash
cd ~/study/aut/master-thesis/srs/ieee-tai
podman run \
    -it \
    --rm \
    -v $(shell pwd):/html \
    -w /html \
    pdf2htmlex/pdf2htmlex:0.18.8.rc2-master-20200820-alpine-3.12.0-x86_64 \
    --zoom 2.0 \
    paper.pdf
~~~~

[1]: https://github.com/arxiv-vanity/engrafo
[2]: https://github.com/pdf2htmlex/pdf2htmlex
