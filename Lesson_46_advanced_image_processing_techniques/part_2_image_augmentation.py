from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create an instance of ImageDataGenerator for augmentation
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Load a sample image
img = image.load_img('image.jpg')  # Replace with your image path
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# Generate augmented images
i = 0
for batch in datagen.flow(x, batch_size=1):
    plt.imshow(image.array_to_img(batch[0]))
    plt.axis('off')
    plt.show()
    i += 1
    if i > 20:  # Stop after 20 augmented images
        break
