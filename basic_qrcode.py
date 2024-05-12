# basic_qrcode.py

import segno

qrcode = segno.make_qr("Scan Me")
qrcode.save("basic_qrcode.png")
