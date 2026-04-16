# qr-manager

Dynamic QR code manager using GitHub Pages redirects.

This repository provides fixed QR URLs whose destinations can be changed later by editing redirect pages in `docs/`.

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

## Current redirect targets

- `lab` → `https://yuyatokuta.github.io/`
- `paper` → `https://yuyatokuta.github.io/Species-OT/`
- `teaching/2026/lec0` → `https://colab.research.google.com/drive/1bJr6XWOEqE2buuZOrfn2YNti3E1sgpDA?usp=sharing`
- `misc` → temporary placeholder

## Repository structure

```text
qr-manager/
├─ README.md
├─ generate_qr.py
├─ qrs/
│  ├─ lab.png
│  ├─ paper.png
│  ├─ teaching_2026_lec0.png
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
            └─ lec0/
               └─ index.html
