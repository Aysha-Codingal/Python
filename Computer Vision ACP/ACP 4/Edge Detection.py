import cv2
import matplotlib.pyplot as plt
import numpy as np

def display_image(original, processed, title):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    if len(processed.shape) == 2:
        plt.imshow(processed, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')

    plt.show()

def main():
    path = "example.jpg"
    img = cv2.imread(path)

    if img is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_img = None

    while True:
        print("\n1. Sobel Edge")
        print("2. Canny Edge")
        print("3. Laplacian Edge")
        print("4. Gaussian Blur")
        print("5. Median Filter")
        print("6. Save Result")
        print("7. Exit")
        
        user_choice = input("Pick (1-7): ")

        if user_choice == "1":
            x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            output_img = cv2.bitwise_or(x.astype(np.uint8), y.astype(np.uint8))
            display_image(img, output_img, "Sobel Edge")

        elif user_choice == "2":
            low_val = int(input("Min threshold: "))
            high_val = int(input("Max threshold: "))
            output_img = cv2.Canny(gray, low_val, high_val)
            display_image(img, output_img, "Canny Edge")

        elif user_choice == "3":
            lap = cv2.Laplacian(gray, cv2.CV_64F)
            output_img = np.abs(lap).astype(np.uint8)
            display_image(img, output_img, "Laplacian Edge")

        elif user_choice == "4":
            k_size = int(input("Kernel size (odd number): "))
            output_img = cv2.GaussianBlur(img, (k_size, k_size), 0)
            display_image(img, output_img, "Gaussian Blur")

        elif user_choice == "5":
            k_size = int(input("Kernel size (odd number): "))
            output_img = cv2.medianBlur(img, k_size)
            display_image(img, output_img, "Median Filter")

        elif user_choice == "6":
            if output_img is None:
                print("No image to save!")
            else:
                out_name = input("Save name: ")
                cv2.imwrite(out_name, output_img)
                print("Saved!")

        elif user_choice == "7":
            break

        else:
            print("Invalid input!")

main()