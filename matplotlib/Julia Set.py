import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to calculate the Julia set
def julia(c, max_iter, width, height, x_min, x_max, y_min, y_max):
    image = np.zeros((height, width))
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    for i in range(height):
        for j in range(width):
            z = complex(x[j], y[i])
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            image[i, j] = n
    return image

# Interactive plot for the Julia set
def interactive_julia():
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.subplots_adjust(bottom=0.2)
    
    # Initial parameters for the Julia set
    width, height = 800, 800
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    max_iter = 256
    c = complex(-0.7, 0.27015)  # Initial constant for the Julia set
    
    # Generate and plot the Julia set
    def update_plot(val):
        nonlocal c, max_iter
        c = complex(np.cos(val), np.sin(val))  # Modify the constant dynamically
        image = julia(c, max_iter, width, height, x_min, x_max, y_min, y_max)
        ax.imshow(image, cmap='inferno', extent=[x_min, x_max, y_min, y_max])
        ax.set_title(f'Julia Set (Constant: {c})')
        fig.canvas.draw_idle()

    # Add a slider to control the constant
    axcolor = 'lightgoldenrodyellow'
    ax_const = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor=axcolor)
    const_slider = Slider(ax_const, 'Constant Angle', -np.pi, np.pi, valinit=0, valstep=0.01)
    const_slider.on_changed(update_plot)
    
    # Display the plot
    update_plot(0)  # Initial plot
    plt.show()

# Run the interactive Julia set generator
interactive_julia()
