import numpy as np
import matplotlib.pyplot as plt

# Burning Ship fractal generation
def burning_ship(c, max_iter):
    z = c
    for n in range(max_iter):
        z = complex(abs(z.real), abs(z.imag))**2 + c
        if abs(z) > 2:
            return n
    return max_iter

# Define image size, max iteration, and coordinates
width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iter = 256

# Create an image
image = np.zeros((height, width))

# Generate the fractal
for y in range(height):
    for x in range(width):
        # Map pixel position to complex plane
        c = complex(x_min + (x / width) * (x_max - x_min), y_min + (y / height) * (y_max - y_min))
        # Generate the fractal value
        image[y, x] = burning_ship(c, max_iter)

# Display the fractal
plt.figure(figsize=(10, 10))
plt.imshow(image, cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Burning Ship Fractal", color='white')
plt.gca().set_facecolor('black')
plt.show()
