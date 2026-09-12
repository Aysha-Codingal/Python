import cv2
import matplotlib.pyplot as plt

image_path = ("example.jpg")
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape
print(height, width)

# rectangle code
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 10)

# circle code
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
cv2.circle(image_rgb, (center1_x, center1_y), 50, (255, 0, 0), -1)

cv2.line(image_rgb, (center1_x, center1_y), (width - 200, height - 200), (255, 0, 0), 5)

arrow_y = height - 50
arrow_start_left = (20, arrow_y)
arrow_end_right = (width - 20, arrow_y)

cv2.arrowedLine(image_rgb, arrow_start_left, arrow_end_right, (255, 255, 0), 3, tipLength=0.03)
cv2.arrowedLine(image_rgb, arrow_end_right, arrow_start_left, (0, 255, 255), 3, tipLength=0.03)

# 3. Annotate the Width:
font = cv2.FONT_HERSHEY_SIMPLEX
text = f"{width}px"
text_size = cv2.getTextSize(text, font, 1, 2)[0]
text_x = (width - text_size[0]) // 2
text_y = arrow_y - 10

cv2.putText(image_rgb, text, (text_x, text_y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

output_path = ("example.jpg")
image_bgr_output = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
cv2.imwrite(output_path, image_bgr_output)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis('off')
plt.show()