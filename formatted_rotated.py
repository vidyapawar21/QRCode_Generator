# formatted_rotated_qrcode.py

import segno

qrcode = segno.make_qr("Hello, World")
qrcode_rotated = qrcode.to_pil(
    scale=5,
    light="violet",
    dark="green",
).rotate(45, expand=True)
qrcode_rotated.save("formatted_rotated_qrcode.png")