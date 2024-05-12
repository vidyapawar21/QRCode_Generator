# borderless_qrcode.py

import segno

qrcode = segno.make_qr("Scan QR code here")
qrcode.save(
    "borderless_qrcode.png",
    scale=7,
    border=0,
)
