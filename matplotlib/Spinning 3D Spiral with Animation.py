import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Step 1: Create the data for the 3D spiral
def generate_spiral(num_points=500, num_turns=5):
    theta = np.linspace(0, 2 * np.pi * num_turns, num_points)  # Angle
    z = np.linspace(0, 10, num_points)  # Height
    r = z  # Radius increases with height
    x = r * np.cos(theta)  # X-coordinate
    y = r * np.sin(theta)  # Y-coordinate
    return x, y, z

# Step 2: Initialize the 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-12, 12])
ax.set_ylim([-12, 12])
ax.set_zlim([0, 12])

# Plot placeholders
spiral_line, = ax.plot([], [], [], lw=2, color='blue')
point, = ax.plot([], [], [], 'ro')  # Moving point at the end of the spiral

# Step 3: Define the animation function
x, y, z = generate_spiral()

def init():
    spiral_line.set_data([], [])
    spiral_line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return spiral_line, point

def update(frame):
    spiral_line.set_data(x[:frame], y[:frame])
    spiral_line.set_3d_properties(z[:frame])
    point.set_data(x[frame], y[frame])
    point.set_3d_properties(z[frame])
    return spiral_line, point

# Step 4: Animate the 3D plot
num_frames = len(x)
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, interval=20, blit=True)

# Step 5: Show the plot
plt.title("Spinning 3D Spiral")
plt.show()
