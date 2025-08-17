import numpy as np

def convolve2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')
    output = np.zeros_like(image)

    for i in range(image_height):
        for j in range(image_width):
            output[i, j] = np.sum(padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)
    
    return output

# Example Gaussian kernel
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16

# Example image
image = np.array([[100, 150, 200],
                  [200, 250, 300],
                  [300, 350, 400]])

blurred_image = convolve2d(image, kernel)
