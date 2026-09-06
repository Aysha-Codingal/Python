import cv2

image = cv2.imread("example.jpg")

small_img = cv2.resize(image, (200, 200))
medium_img = cv2.resize(image, (400, 400))
large_img = cv2.resize(image, (600, 600))

cv2.imwrite("input_image_small.jpg", small_img)
cv2.imwrite("input_image_medium.jpg", medium_img)
cv2.imwrite("input_image_large.jpg", large_img)

cv2.imshow("Small Image", small_img)
cv2.imshow("Medium Image", medium_img)
cv2.imshow("Large Image", large_img)

cv2.waitKey(0)
cv2.destroyAllWindows()