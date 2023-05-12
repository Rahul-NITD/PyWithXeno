import cv2
import numpy as np
import os


BLOG_NUMBER = 4


destination_folder = f"./Blog {BLOG_NUMBER}/outputs/"
if not os.path.exists(destination_folder):
  os.makedirs(destination_folder)

#random array
dimensions = (600,1000)
pixels = dimensions[0] * dimensions[1]
bytes_required = pixels * 3
array = np.random.randint(low=0, high=255, size=bytes_required, dtype='uint8')
# this creates a 'pixels' length long array
# to make the array into our desired shape
array.shape = (*dimensions, 3)

cv2.imshow("random grey image", array)
cv2.waitKey()
cv2.imwrite(f"{destination_folder}output1.png", array)
cv2.destroyAllWindows()
