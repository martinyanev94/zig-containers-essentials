import matplotlib.pyplot as plt

def plot_color_histogram(image_path):
    image = cv2.imread(image_path)
    colors = ("b", "g", "r")  # OpenCV uses BGR format

    plt.figure()
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.title("Color Histogram")
    plt.show()

plot_color_histogram("example_image.jpg")
