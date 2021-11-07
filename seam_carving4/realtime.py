import cv2
import numpy as np

from seam_carving import SeamCarver
from Sketcher import Sketcher

import os, sys

MODE = 'remove' # 'remove', 'protect'
img_path = sys.argv[1]

def nothing(x):
  pass

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_masked = img.copy()
mask = np.zeros(img.shape[:2], np.uint8)

sketcher = Sketcher('image', [img_masked, mask], lambda : ((255, 255, 255), 255))

cv2.createTrackbar('width', 'image', img.shape[1], img.shape[1]*2, nothing)
cv2.createTrackbar('height', 'image', img.shape[0], img.shape[0]*2, nothing)

while True:
  key = cv2.waitKey()

  if key == ord('q'): # quit
    break
  if key == ord('r'): # reset
    print('reset')
    img_masked[:] = img
    mask[:] = 0
    sketcher.show()
  if key == 32: # hit spacebar
    new_width = int(cv2.getTrackbarPos(trackbarname='width', winname='image'))
    new_height = int(cv2.getTrackbarPos(trackbarname='height', winname='image'))

    if np.sum(mask) > 0: # object removal or protect mask
      if MODE == 'remove':
        carver = SeamCarver(img, 0, 0, object_mask=mask)
      elif MODE == 'protect':
        carver = SeamCarver(img, new_height, new_width, protect_mask=mask)
      else:
        carver = SeamCarver(img, new_height, new_width)
    else:
      carver = SeamCarver(img, new_height, new_width)

    cv2.imshow('resize', cv2.resize(img, dsize=(new_width, new_height)))
    cv2.imshow('input', carver.in_image.astype(np.uint8))
    cv2.imshow('output', carver.out_image.astype(np.uint8))
