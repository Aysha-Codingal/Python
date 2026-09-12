import cv2 
import numpy as np

def apply_color_filter(image, filter_type):
    cv2.namedWindow("Filtered Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Filtered Image", 800, 600)

    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0 # green channel to 0
        filtered_image[:, :, 0] = 0 # Blue channel to 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0 # green channel to 0
        filtered_image[:, :, 2] = 0 # Red channel to 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0 # Blue channel to 0
        filtered_image[:, :, 2] = 0 # Red channel to 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 100) # increase red channel

    elif filter_type == "decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 100) # decrease red channel

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 100) # decrease blue channel

    elif filter_type == "increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 100) # increase green channel

    return filtered_image

image_path = 'example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image Not Found")
else:
    filtered_type = "original" # Default image type 

    print("Press The Following Keys To See The Filters: ")
    print("r - Red Tint\nb - Blue Tint\ng - Green Tint\ni - Increase Red Intensity\nd - Decrease Blue Intensity")
    print("Up Arrow - Increase Green Intensity\nDown Arrow - Decrease Red Intensity\nq - Quit") 

    while True:
        filtered_image = apply_color_filter(image, filtered_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKeyEx(0)

        if key == ord('r'):
            filtered_type = "red_tint"
        elif key == ord('b'):
            filtered_type = "blue_tint"
        elif key == ord('g'):
            filtered_type = "green_tint"
        elif key == ord('i'):
            filtered_type = "increase_red"
        elif key == ord('d'):
            filtered_type = "decrease_blue"
        elif key == 2490368 or key == 65362 or key == 0:  # Up Arrow
            filtered_type = "increase_green"
        elif key == 2621440 or key == 65364 or key == 1:  # Down Arrow
            filtered_type = "decrease_red"
        elif key == ord('q'):
            print("Quitting...")
            break
        else:
            print("Invalid Key !!!")

    cv2.destroyAllWindows()

    filename = input("Enter a custom filename to save the image (e.g., output.jpg): ")
    filename = filename.replace(" ", "_").replace(":", "_").replace("/", "_")
    
    cv2.imwrite("images/" + filename, filtered_image)
    print("Image saved successfully to images/" + filename)