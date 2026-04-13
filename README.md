# qr-manager

Dynamic QR code manager using GitHub Pages redirects.

## Fixed QR URLs

- lab  
  `https://yuyatokuta.github.io/qr-manager/go/lab/`

- paper  
  `https://yuyatokuta.github.io/qr-manager/go/paper/`

- teaching/2026/lec0  
  `https://yuyatokuta.github.io/qr-manager/go/teaching/2026/lec0/`

- misc  
  `https://yuyatokuta.github.io/qr-manager/go/misc/`

## Current redirect targets

- lab → `https://yuyatokuta.github.io/`
- paper → `https://yuyatokuta.github.io/Species-OT/`
- teaching/2026/lec0 → `https://colab.research.google.com/drive/1bJr6XWOEqE2buuZOrfn2YNti3E1sgpDA?usp=sharing`
- misc → `https://yuyatokuta.github.io/`

## How to update a destination

Edit the corresponding `index.html` and update the same URL in:

- `meta refresh`
- `link rel="canonical"`
- `window.location.replace(...)`
- fallback `<a href="...">`

## GitHub Pages setup

1. Open this repository on GitHub.
2. Go to **Settings > Pages**.
3. Under **Build and deployment**:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
4. Save.
5. Wait for deployment.

## Notes

The QR code stays fixed.  
Only the redirect target changes later.
