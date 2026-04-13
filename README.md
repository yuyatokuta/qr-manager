# qr-manager
Manage dynamic QR codes with GitHub Pages and simple redirect pages

## How it works

The QR code points to a fixed GitHub Pages URL such as:

`https://yuyatokuta.github.io/qr-manager/go/lab/`

This page immediately redirects visitors to the current destination URL.

To change the destination later, edit:

`docs/go/lab/index.html`

and update the URL in:

- the `meta refresh`
- the `window.location.replace(...)`
- the fallback link in the body

## Setup

1. Create this repository on GitHub.
2. Add the files in this repo.
3. Go to **Settings > Pages**.
4. Under **Build and deployment**, choose:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
5. Save.
6. Wait for GitHub Pages to publish.

Your redirect URL will be:

`https://yuyatokuta.github.io/qr-manager/go/lab/`

## Example use

Generate a QR code for:

`https://yuyatokuta.github.io/qr-manager/go/lab/`

Then print or share that QR code.

Later, if you want to change the destination, just edit:

`docs/go/lab/index.html`

## Notes

- The QR code itself stays the same.
- Only the redirect target changes.
- GitHub Pages updates may take a short time to go live.
