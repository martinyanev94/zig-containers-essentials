import cv2
import numpy as np
from multiprocessing import Pool

def process_image(image_path):
    image = cv2.imread(image_path)
    # Example processing: convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

if __name__ == "__main__":
    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with paths to your images
    with Pool(processes=3) as pool:
        results = pool.map(process_image, image_paths)
    
    for idx, result in enumerate(results):
        cv2.imshow(f'Processed Image {idx + 1}', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
