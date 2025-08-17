import numpy as np
import cv2

def kmeans_segmentation(image_path, k):
    image = cv2.imread(image_path)
    data = image.reshape((-1, 3))  # Reshape to a 2D array of pixels
    data = np.float32(data)

    # Define criteria and apply kmeans
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    segmented_image = centers[labels.flatten()].reshape(image.shape).astype(np.uint8)
    return segmented_image

segmented_output = kmeans_segmentation("image.jpg", 3)
