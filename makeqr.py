# save as makeqr.py
import sys, qrcode
img = qrcode.make(sys.argv[1])
img.save("qr.png")
