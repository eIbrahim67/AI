import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lorenz Attractor equations
def lorenz(x, y, z, sigma=10, beta=8/3, rho=28):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Generate Lorenz Attractor
def generate_lorenz(n_steps=100000, dt=0.01):
    x, y, z = 0.1, 0, 0
    x_vals, y_vals, z_vals = [], [], []
    
    for _ in range(n_steps):
        dx, dy, dz = lorenz(x, y, z)
        x += dx * dt
        y += dy * dt
        z += dz * dt
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)
    
    return np.array(x_vals), np.array(y_vals), np.array(z_vals)

# Plot and animate Lorenz Attractor with dynamic colors
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Enhanced Lorenz Attractor", color='white')
ax.set_facecolor('black')

# Generate data
x_vals, y_vals, z_vals = generate_lorenz()

# Create a color gradient based on velocity
velocity = np.sqrt(np.diff(x_vals)**2 + np.diff(y_vals)**2 + np.diff(z_vals)**2)
norm = plt.Normalize(velocity.min(), velocity.max())
colors = plt.cm.viridis(norm(velocity))

# Plot the 3D line
line, = ax.plot([], [], [], color='cyan', lw=0.8)
scat = ax.scatter([], [], [], color='white', s=0.1)

# Set limits and labels
ax.set_xlim([-30, 30])
ax.set_ylim([-30, 30])
ax.set_zlim([0, 50])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to update the plot for animation
def update(frame):
    # Update the line and scatter plot
    line.set_data(x_vals[:frame], y_vals[:frame])
    line.set_3d_properties(z_vals[:frame])

    # Update color of the scatter points
    scat._offsets3d = (x_vals[:frame], y_vals[:frame], z_vals[:frame])
    scat.set_color(colors[:frame])

    return line, scat

# Animate the Lorenz Attractor
ani = FuncAnimation(fig, update, frames=len(x_vals), interval=1, blit=False)

plt.show()
