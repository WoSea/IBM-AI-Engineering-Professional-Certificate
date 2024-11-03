from PIL import Image
import matplotlib.pyplot as plt

# Load the sprite image
sprite_path = "/mnt/data/fashion-mnist-sprite.png"
sprite_image = Image.open(sprite_path)

# Define the size of each sub-image (assuming 28x28 for Fashion MNIST)
sub_image_size = (28, 28)
sprite_width, sprite_height = sprite_image.size

# Calculate the number of rows and columns
num_cols = sprite_width // sub_image_size[0]
num_rows = sprite_height // sub_image_size[1]

# Extract and display each sub-image
fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 10))
for row in range(num_rows):
    for col in range(num_cols):
        left = col * sub_image_size[0]
        upper = row * sub_image_size[1]
        right = left + sub_image_size[0]
        lower = upper + sub_image_size[1]
        
        # Crop the sub-image
        sub_image = sprite_image.crop((left, upper, right, lower))
        
        # Display in the grid
        ax = axes[row, col]
        ax.imshow(sub_image, cmap="gray")
        ax.axis("off")

plt.show()
