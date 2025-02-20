import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Step 1: Define the Solar System Parameters
class Planet:
    def __init__(self, name, radius, speed, color, size):
        self.name = name  # Planet name
        self.radius = radius  # Orbital radius
        self.speed = speed  # Orbital speed
        self.color = color  # Planet color
        self.size = size  # Planet size
        self.angle = 0  # Current angle in orbit
    
    def update_position(self):
        self.angle += self.speed  # Increment the angle for rotation
        x = self.radius * np.cos(self.angle)
        y = self.radius * np.sin(self.angle)
        return x, y

# Create planets
planets = [
    Planet(name="Mercury", radius=2, speed=0.1, color='gray', size=50),
    Planet(name="Venus", radius=3, speed=0.08, color='orange', size=80),
    Planet(name="Earth", radius=4, speed=0.06, color='blue', size=100),
    Planet(name="Mars", radius=5, speed=0.05, color='red', size=70),
    Planet(name="Jupiter", radius=7, speed=0.03, color='brown', size=200),
    Planet(name="Saturn", radius=9, speed=0.02, color='gold', size=180),
    Planet(name="Uranus", radius=11, speed=0.015, color='cyan', size=150),
    Planet(name="Neptune", radius=13, speed=0.01, color='blue', size=140),
]

# Step 2: Initialize the 3D plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])
ax.set_zlim([-5, 5])
ax.axis('off')  # Hide axes for better aesthetics

# Draw the "sun"
ax.scatter(0, 0, 0, color='yellow', s=1000, label="Sun")

# Add a background
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Add stars in the background
num_stars = 100  # Number of stars
star_x = np.random.uniform(-15, 15, num_stars)
star_y = np.random.uniform(-15, 15, num_stars)
star_z = np.random.uniform(-5, 5, num_stars)
ax.scatter(star_x, star_y, star_z, color='white', s=2, alpha=0.8)  # Small, faint stars

# Placeholders for planet positions and orbits
planet_scatter = [ax.scatter([], [], [], color=p.color, s=p.size) for p in planets]
orbit_lines = [ax.plot([], [], [], '--', color=p.color, alpha=0.5)[0] for p in planets]
planet_labels = [ax.text(0, 0, 0, '', color='white', fontsize=10) for p in planets]

# Step 3: Define the animation function
def update(frame):
    for i, planet in enumerate(planets):
        # Update planet position
        x, y = planet.update_position()
        planet_scatter[i]._offsets3d = (np.array([x]), np.array([y]), np.array([0]))
        
        # Update orbit lines
        theta = np.linspace(0, 2 * np.pi, 100)
        orbit_x = planet.radius * np.cos(theta)
        orbit_y = planet.radius * np.sin(theta)
        orbit_lines[i].set_data(orbit_x, orbit_y)
        orbit_lines[i].set_3d_properties(np.zeros_like(theta))
        
        # Update planet label
        planet_labels[i].set_position((x, y))
        planet_labels[i].set_text(planet.name)
    return planet_scatter + orbit_lines + planet_labels

# Step 4: Animate the Solar System
ani = FuncAnimation(fig, update, frames=360, interval=50, blit=False)

# Step 5: Show the Solar System
plt.title("Enhanced 3D Solar System Simulation with Starry Background", color='white', fontsize=16)
plt.legend(loc="upper right", fontsize=10)
plt.show()
