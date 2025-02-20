import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Step 1: Define the random walk function
def random_walk_3d(steps):
    # Start at the origin (0, 0, 0)
    x, y, z = [0], [0], [0]
    
    # Generate random steps in 3D
    for _ in range(steps - 1):
        direction = np.random.choice(['x', 'y', 'z'])
        step_size = np.random.choice([-1, 1])
        if direction == 'x':
            x.append(x[-1] + step_size)
            y.append(y[-1])
            z.append(z[-1])
        elif direction == 'y':
            x.append(x[-1])
            y.append(y[-1] + step_size)
            z.append(z[-1])
        else:
            x.append(x[-1])
            y.append(y[-1])
            z.append(z[-1] + step_size)
    
    return np.array(x), np.array(y), np.array(z)

# Step 2: Set up the plot and animation
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Step 3: Function to update the plot
def update(frame):
    ax.clear()
    
    # Generate random walk data up to the current frame
    x, y, z = random_walk_3d(frame)
    
    # Plot the random walk in 3D space
    ax.plot(x, y, z, color=plt.cm.viridis(frame / 1000), linewidth=2)  # Color transition
    ax.scatter(x[-1], y[-1], z[-1], color='red', s=50)  # Mark the current position
    
    # Set the plot limits and labels
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_zlim([-50, 50])
    ax.set_title(f"3D Random Walk (Step: {frame})", color='white')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    ax.grid(False)
    ax.set_facecolor('black')  # Set background color to black

# Step 4: Create the animation
ani = FuncAnimation(fig, update, frames=1000, interval=10, repeat=False)

# Step 5: Display the plot
plt.show()
