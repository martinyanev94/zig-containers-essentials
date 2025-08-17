import cv2

def canny_edge_detection(image_path):
    image = cv2.imread(image_path, 0)  # Load image in grayscale
    blurred = cv2.GaussianBlur(image, (5, 5), 1.5)
    edges = cv2.Canny(blurred, 50, 150)  # Perform Canny edge detection
    return edges

edges_found = canny_edge_detection("example_image.jpg")
