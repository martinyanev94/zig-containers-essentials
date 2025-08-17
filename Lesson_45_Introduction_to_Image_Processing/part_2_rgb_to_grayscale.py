def rgb_to_grayscale(r, g, b):
    return int(0.2989 * r + 0.5870 * g + 0.1140 * b)

# Example usage
image = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],  # A 1x3 image with RGB pixels
]

grayscale_image = [[rgb_to_grayscale(r, g, b) for r, g, b in row] for row in image]
