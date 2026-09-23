import cv2


# Filter 
def red_tint(img):
    image = img.copy()
    image[:, :, 0] = 0  # Blue = 0
    image[:, :, 1] = 0  # Green = 0
    return image


def green_tint(img):
    image = img.copy()
    image[:, :, 0] = 0  # Blue = 0
    image[:, :, 2] = 0  # Red = 0
    return image


def blue_tint(img):
    image = img.copy()
    image[:, :, 1] = 0  # Green = 0
    image[:, :, 2] = 0  # Red = 0
    return image


def sobel_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0))
    sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1))
    sobel = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)
    return cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)


def canny_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


FILTERS = {
    ord("o"): ("Original", lambda img: img.copy()),
    ord("r"): ("Red Tint", red_tint),
    ord("g"): ("Green Tint", green_tint),
    ord("b"): ("Blue Tint", blue_tint),
    ord("s"): ("Sobel Edges", sobel_edges),
    ord("c"): ("Canny Edges", canny_edges),
}

# Main Coding

image = cv2.imread("example.jpg")

if image is None:
    print("Error: Could not load image!")
else:
    active_filter = FILTERS[ord("o")][1] 

    print("Buttons: [o] Original | [r] Red | [g] Green | [b] Blue")
    print("          [s] Sobel    | [c] Canny | [q] Quit")

    while True:
        cv2.imshow("Filtered Image", active_filter(image))
        key = cv2.waitKey(0) & 0xFF

        if key == ord("q"):
            break
        elif key in FILTERS:
            name, active_filter = FILTERS[key]
            print(f"Applied: {name}")

    cv2.destroyAllWindows()