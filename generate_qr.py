from pathlib import Path

import qrcode


URLS = {
    "lab": "https://yuyatokuta.github.io/qr-manager/go/lab/",
    "paper": "https://yuyatokuta.github.io/qr-manager/go/paper/",
    "teaching_2026_lec0": "https://yuyatokuta.github.io/qr-manager/go/teaching/2026/lec0/",
    "misc": "https://yuyatokuta.github.io/qr-manager/go/misc/",
}


def url_to_qrcode(
    url: str,
    output_path: Path,
    box_size: int = 10,
    border: int = 4,
) -> Path:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return output_path


def main() -> None:
    output_dir = Path("qrs")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating QR codes...")
    for name, url in URLS.items():
        output_path = output_dir / f"{name}.png"
        saved_path = url_to_qrcode(url=url, output_path=output_path)
        print(f"{name}: {saved_path.resolve()}")

    print("Done.")


if __name__ == "__main__":
    main()
