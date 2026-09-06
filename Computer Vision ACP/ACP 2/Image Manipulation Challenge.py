import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("example.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.show()

cropped = image[100:300, 200:400]

(h, w) = image.shape[:2]
M = cv2.getRotationMatrix2D((w // 2, h // 2), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

brighter = cv2.add(image, np.ones(image.shape, dtype="uint8") * 50)

cv2.imwrite("example.jpg", gray)
cv2.imwrite("example.jpg", cropped)
cv2.imwrite("example.jpg", rotated)
cv2.imwrite("example.jpg", brighter)