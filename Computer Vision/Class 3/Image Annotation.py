import cv2
import matplotlib.pyplot as plt

image_path = "example.jpg"
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape
print(height, width)
# rectangle code

rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb,top_left1, bottom_right1,(0, 255, 255), 10)

# circle code

center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
cv2.circle(image_rgb, (center1_x, center1_y), 50, (255, 0, 0), -1)

cv2.line(image_rgb, (center1_x, center1_y), (width - 200, height - 200), (255, 0, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Scenery', (width // 2, height // 2), font, 2, (0, 0, 255), 2, cv2.LINE_4)

arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3,  tipLength = 0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 0, 255), 3, tipLength = 0.05)


plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis('off')
plt.show()