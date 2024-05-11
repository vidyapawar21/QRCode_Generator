# borderless_qrcode.py

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "borderless_qrcode.png",
    scale=7,
    border=0,
)