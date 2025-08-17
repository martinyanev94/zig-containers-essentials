import cv2

# Load the images to be stitched
images = [cv2.imread("image1.jpg"), cv2.imread("image2.jpg"), cv2.imread("image3.jpg")]

# Create a stitcher object
stitcher = cv2.Stitcher_create()

# Perform the stitching process
status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imshow("Stitched Image", stitched)
else:
    print("Error during stitching!")
