# darkblue_qrcode.py

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "darkblue.png",
    scale=5,
    dark="darkblue",
    quiet_zone="lightgreen",
)