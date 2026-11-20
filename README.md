# The Thursday Gazette — 19 November 2026 in one image

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261119-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

One image summing up the world's news of **Thursday 19 November 2026**,
entered in [make.fun](https://make.fun) competition `news-image-20261119`.

The broadsheet front page carries 35 verified stories: the first-ever
Trump–Xi–Putin trilateral summit in Shenzhen, Anthropic's $81.3bn IPO
(the largest ever by base deal), and the worldwide midnight launch of
GTA VI — plus a world-map band with 35 numbered pins and a two-column
ALSO list. The program is a one-line copier: it validates `entry.png`
(PNG, at most 1 MiB, at most 1024x1024) and copies it to `/output`.

## Run

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to override the default `/output`.

## Build

The image is drawn by a deterministic PIL generator; re-running it
produces a byte-identical `entry.png`.

## Referral

https://make.fun/r/nbgfvtz4
