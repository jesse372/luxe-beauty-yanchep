# -*- coding: utf-8 -*-
"""Scans the finished review cards and fails unless every QR code reads as the review link.
Needs: pip install opencv-python-headless"""
import sys, cv2
WANT = "https://luxebeautyyanchep.com/review"
ok = True
for path, expect in (("review-card.png", 1), ("/tmp/review-cards-a4-check.png", 4)):
    img = cv2.imread(path)
    if img is None:
        print("  FAIL cannot open", path); ok = False; continue
    found, texts, _, _ = cv2.QRCodeDetector().detectAndDecodeMulti(img)
    texts = [t for t in (texts or []) if t]
    good = [t for t in texts if t == WANT]
    print("  %s: %d QR code(s) read, %d correct (need %d) %s" % (path, len(texts), len(good), expect, img.shape[1::-1]))
    if len(good) < expect: ok = False
sys.exit(0 if ok else 1)
