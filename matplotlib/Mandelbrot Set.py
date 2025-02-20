import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to calculate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iter

# Generate the Mandelbrot image
def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((height, width))
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            image[i, j] = mandelbrot(c, max_iter)
    return image

# Interactive plot for the Mandelbrot set
def interactive_mandelbrot():
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.subplots_adjust(bottom=0.2)
    
    # Initial parameters for the Mandelbrot set
    width, height = 800, 800
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 256
    
    # Generate and plot the Mandelbrot set
    def update_plot(val):
        nonlocal x_min, x_max, y_min, y_max, max_iter
        image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, int(val))
        ax.imshow(image, cmap='inferno', extent=[x_min, x_max, y_min, y_max])
        ax.set_title(f'Mandelbrot Set (Iterations: {int(val)})')
        fig.canvas.draw_idle()

    # Add a slider to control the max iterations
    axcolor = 'lightgoldenrodyellow'
    ax_iter = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor=axcolor)
    iter_slider = Slider(ax_iter, 'Max Iterations', 10, 1000, valinit=max_iter, valstep=1)
    iter_slider.on_changed(update_plot)
    
    # Display the plot
    update_plot(max_iter)
    plt.show()

# Run the interactive Mandelbrot generator
interactive_mandelbrot()
