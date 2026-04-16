# qr-manager

Dynamic QR code manager using GitHub Pages redirects.

This repository provides stable QR URLs whose destinations can be updated later by editing redirect pages in `docs/`.

## Fixed QR URLs

- `lab`  
  `https://yuyatokuta.github.io/qr-manager/go/lab/`

- `paper`  
  `https://yuyatokuta.github.io/qr-manager/go/paper/`

- `teaching/2026/lec0`  
  `https://yuyatokuta.github.io/qr-manager/go/teaching/2026/lec0/`

- `teaching/2026/lec1`  
  `https://yuyatokuta.github.io/qr-manager/go/teaching/2026/lec1/`

- `misc`  
  `https://yuyatokuta.github.io/qr-manager/go/misc/`

## How it works

Each fixed URL points to a redirect page hosted on GitHub Pages.  
To change a destination later, update the corresponding `index.html` in `docs/` without changing the QR code itself.

## Repository structure

```text
qr-manager/
├─ README.md
├─ generate_qr.py
├─ qrs/
│  ├─ lab.png
│  ├─ paper.png
│  ├─ teaching_2026_lec0.png
│  ├─ teaching_2026_lec1.png
│  └─ misc.png
└─ docs/
   └─ go/
      ├─ lab/
      │  └─ index.html
      ├─ paper/
      │  └─ index.html
      ├─ misc/
      │  └─ index.html
      └─ teaching/
         └─ 2026/
            ├─ lec0/
            │  └─ index.html
            └─ lec1/
               └─ index.html