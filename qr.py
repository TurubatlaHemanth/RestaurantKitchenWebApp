import qrcode as qr
image=qr.make("https://127.0.0.1:8000")
image.save("qr.png")