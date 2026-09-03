import cv2

image = cv2.imread("example.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(gray, (224, 224))

cv2.imshow("GrayScale Resized Image", resized)

print("Press 's' to save the image. Press any other key to quit!")

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("output_224x224_gray.jpg", resized)
    print("Image Succesfully Saved")