import matplotlib.pyplot as plt
import numpy as np

# Step 1: Define the recursive function to generate the tree
def draw_tree(x, y, angle, length, width, depth):
    if depth == 0:
        return

    # Calculate the new branch position based on the angle
    x_end = x + np.cos(angle) * length
    y_end = y + np.sin(angle) * length

    # Draw the line representing the branch
    plt.plot([x, x_end], [y, y_end], color='green', lw=width)

    # Recursively draw the two branches that grow from the current branch
    draw_tree(x_end, y_end, angle - np.pi / 6, length * 0.7, width * 0.7, depth - 1)  # Left branch
    draw_tree(x_end, y_end, angle + np.pi / 6, length * 0.7, width * 0.7, depth - 1)  # Right branch

# Step 2: Set up the plot
plt.figure(figsize=(8, 8))
plt.axis('off')  # Turn off the axis for better aesthetics
plt.gca().set_facecolor('black')  # Set background to black

# Step 3: Draw the Fractal Tree
draw_tree(x=0, y=0, angle=np.pi / 2, length=10, width=2, depth=10)

# Step 4: Show the plot
plt.title("Fractal Tree Simulation", color='white', fontsize=16)
plt.show()
