# PROGRAMMER: Kevin Pember

# IMPORT STATEMENTS
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib import cm
# SOLUTION

################Basic program from docs#########################


# Create the figure and axes object
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the sphere
radius = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = radius*sin(phi)*cos(theta)
y = radius*sin(phi)*sin(theta)
z = radius*cos(phi)

# Plot the surface
ax.plot_surface(x, y, z, color='blue')

# Set the aspect ratio to 1 so that the sphere is displayed correctly
ax.set_aspect('equal')

# Show the plot
plt.show()