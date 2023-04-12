"""Plot the path of a projectile using `plotly`."""
# !pip install plotly==5.14.1 numpy==1.23.5 nbformat==4.2.0
# # !pip install math==1.3.0


#%%
import numpy as np
import plotly.graph_objs as go
import math

# Define Cartesian coordinates
x = 1.0
y = 2.0
z = 3.0

# Convert to polar coordinates.
r = np.sqrt(x**2 + y**2 + z**2)
theta = np.arctan2(y, x)
phi = np.arctan2(np.sqrt(x**2 + y**2), z)

# Print the results.
print("Cartesian coordinates: ({}, {}, {})".format(x, y, z))
print("Polar coordinates: (r={}, theta={}, phi={})".format(r, theta, phi))

#%%

# Define initial conditions
initial_velocity = 9.8 # [m/s]
initial_angle = math.pi / 4.0 # [radians]
initial_position = np.array([0.0, 0.0, 0.0]) # x, y, z coordinates
gravitational_acceleration = 9.81 # [m/s^2]

# Calculate time of flight.
time_of_flight = 2.0 * initial_velocity * math.sin(initial_angle) / gravitational_acceleration

# Generate time values at equal intervals.
num_points = 100
t_values = np.linspace(0, time_of_flight, num_points)

# Calculate x and y coordinates in polar coordinates.
x_values = initial_velocity * math.cos(initial_angle) * t_values
y_values = initial_velocity * math.sin(initial_angle) * t_values - 0.5 * gravitational_acceleration * t_values ** 2

# Convert to Cartesian coordinates.
x_cartesian = x_values * np.cos(initial_position[2])
y_cartesian = x_values * np.sin(initial_position[2])
z_cartesian = y_values

# Print the results.
print("Cartesian coordinates: ({}, {}, {})".format(x_cartesian, y_cartesian, z_cartesian))
print("Polar coordinates: (r={}, theta={}, phi={})".format(r, theta, phi))


#%%
"""Plot the path of a projectile in cartesian coordinates using `plotly`."""
#########################
# Cartesian Coordinates
#########################
# Create 3D scatter plot (Cartesian coordinates).
fig = go.Figure(data=[go.Scatter3d(x=x_cartesian, y=y_cartesian, z=z_cartesian, mode='lines')])
fig.update_layout(title='Projectile Motion in Polar Coordinates', scene=dict(xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')))
fig.show()

# # Using `x_cartesian`, `y_cartesian``, `z_cartesian``
# Convert to polar coordinates.
r = np.sqrt(x_cartesian**2 + y_cartesian**2 + z_cartesian**2)
theta = np.arctan2(y_cartesian, x_cartesian)
phi = np.arctan2(np.sqrt(x_cartesian**2 + y_cartesian**2), z_cartesian)



# Define initial conditions.
initial_velocity = 9.8 # [m/s]
initial_angle = math.pi / 4.0 # [radians]
initial_position = np.array([0.0, 0.0, 0.0]) # x, y, z coordinates
gravitational_acceleration = 9.81 # [m/s^2]

# Calculate time of flight.
time_of_flight = 2.0 * initial_velocity * math.sin(initial_angle) / gravitational_acceleration

# Generate time values at equal intervals.
num_points = 100
t_values = np.linspace(0, time_of_flight, num_points)

# Calculate x and y coordinates in polar coordinates.
x_values = initial_velocity * math.cos(initial_angle) * t_values
y_values = initial_velocity * math.sin(initial_angle) * t_values - 0.5 * gravitational_acceleration * t_values ** 2



#%%
"""Plot the path of a projectile in polar coordinates using `plotly`."""
#########################
# Polar Coordinates
#########################
# Convert to polar coordinates.
r_values = np.sqrt(x_cartesian**2 + y_cartesian**2 + z_cartesian**2)
theta_values = np.arctan2(y_cartesian, x_cartesian)
phi_values = np.arctan2(np.sqrt(x_cartesian**2 + y_cartesian**2), z_cartesian)

# Create 3D scatter plot (polar coordinates).
fig = go.Figure(data=[go.Scatter3d(x=theta_values, y=phi_values, z=r_values, mode='lines')])
fig.update_layout(title='Projectile Motion in Polar Coordinates', scene=dict(xaxis=dict(title='Theta'), yaxis=dict(title='Phi'), zaxis=dict(title='R')))
fig.show()

#%%

"""Plot the path of a projectile in spherical coordinates using `plotly` in Python."""
#########################
# Spherical Coordinates
#########################
# r = (x_cartesian**2 + y_cartesian**2 + z_cartesian**2)**.5
# theta = np.arctan(y_cartesian, x_cartesian)
# phi = np.arctan2( (x_cartesian**2 + y_cartesian**2), z_cartesian)
r = np.sqrt(x_cartesian ** 2 + y_cartesian ** 2 + z_cartesian ** 2)
theta = np.arctan2(y_cartesian, x_cartesian)
phi = np.arctan2(np.sqrt(x_cartesian ** 2 + y_cartesian ** 2), z_cartesian)


print(f"r == r_values: {r == r_values}")
print(f"theta == theta_values: {theta == theta_values}")
print(f"phi == phi_values: {phi == phi_values}")
# Convert spherical coordinates to Cartesian coordinates for plotting.
x_spherical = r * np.sin(phi) * np.cos(theta)
y_spherical = r * np.sin(phi) * np.sin(theta)
z_spherical = r * np.cos(phi)

# Create 3D scatter plot (spherical coordinates).
fig = go.Figure(data=[go.Scatter3d(x=x_spherical, y=y_spherical, z=z_spherical, mode='lines')])
fig.update_layout(title='Projectile Motion in Spherical Coordinates', scene=dict(xaxis=dict(title='x_spherical'), yaxis=dict(title='y_spherical'), zaxis=dict(title='z_spherical')))
fig.show()


# %%
