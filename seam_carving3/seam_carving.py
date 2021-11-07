# import the necessary libraries
from skimage import transform
from skimage import filters
import cv2

# read the input image
img = cv2.imread('image.jpg')

# convert image from BGR
# to GRAY scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# filter out the gradient representation
# image to further process for
# seam carving algorithm
# filters.sobel() is used to
# find edges in an image
filtered = filters.sobel(gray.astype("float"))


for i in range(20, 180, 20):

    # apply seam carve to the image,
    # iterating over the image for
    # multiple frames
    # transform.seam_carve() can transform
    # the seam of image vertically as
    # well as horizontally
    carved_image = transform.seam_carve(img, filtered, 'vertical', i)

# show the original image
cv2.imshow("original", img)

# show the carved image
cv2.imshow("carved", carved_image)

# print shape of both images
print("Shape of original image ",
      img.shape)
print("Shape of Carved image ",
      carved_image.shape)

# wait
cv2.waitKey(0)
