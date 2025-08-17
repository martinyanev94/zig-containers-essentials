import tensorflow_hub as hub
import matplotlib.pyplot as plt

# Load the pre-trained style transfer model
style_model = hub.load("https://hub.TensorFlow.co/assets/fast_style_transfer/")  

# Load content and style images
content_image = load_and_process_image("content.jpg")
style_image = load_and_process_image("style.jpg")

# Perform style transfer
stylized_image = model(tf.constant(content_image), tf.constant(style_image))

# Display the result
plt.imshow(stylized_image)
plt.axis('off')
plt.show()
