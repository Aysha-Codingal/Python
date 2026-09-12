import cv2 
import numpy as np

def apply_color_filter(image, filter_type):
    cv2.namedWindow("Filtered Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Filtered Image", 800, 600)

    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0 #green channel to 0
        filtered_image[:, :, 0] = 0 #Blue channel to 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0 #green channel to 0
        filtered_image[:, :, 2] = 0 #Red channel to 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0 #Blue channel to 0
        filtered_image[:, :, 2] = 0 #Red channel to 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 100) #increase red channel

    elif filter_type == "decrease_red":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 100) #decrease red channel
    return filtered_image

image_path = 'example.jpg'
image = cv2.imread(image_path)


if image is None:
    print("Error: Image Not Found")
else:
    filtered_type = "original" #Default image type 

    print("Press The Following Keys To See The Filters: ")
    print("r - Red Tint\nb - Blue Tint\ng - Green Tint\ni - Increase Red Intensity\nd - Decrease Blue Intensity\nq - Quit") 

    while True:
        filtered_image = apply_color_filter(image, filtered_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filtered_type= "red_tint"
        elif key == ord('b'):
            filtered_type= "blue_tint"
        elif key == ord('g'):
            filtered_type= "green_tint"
        elif key == ord('i'):
            filtered_type= "increase_tint"
        elif key == ord('d'):
            filtered_type= "decrease_tint"
        elif key == ord('q'):
            print("Quiting...")
            break
        else:
            print("Invalid Key !!!")

cv2.destroyAllWindows()            

