"""3D plot of plane path flying over the poles."""
import plotly.graph_objs as go
import numpy as np

# Define latitude, longitude, and altitude values for the path.
lat = np.linspace(-90, 90, 100)
lon = np.linspace(-180, 180, 100)
alt = 10000

# Create a meshgrid of latitude and longitude values.
Lon, Lat = np.meshgrid(lon, lat)

# Convert to Cartesian coordinates.
X = (alt + 6371) * np.cos(np.deg2rad(Lat)) * np.cos(np.deg2rad(Lon))
Y = (alt + 6371) * np.cos(np.deg2rad(Lat)) * np.sin(np.deg2rad(Lon))
Z = (alt + 6371) * np.sin(np.deg2rad(Lat))

# Create a 3D plot of the plane path.
fig = go.Figure(data=[go.Scatter3d(x=X.flatten(), y=Y.flatten(), z=Z.flatten(), mode='lines')])

# Set the axis labels and plot title.
fig.update_layout(scene=dict(xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')),
                  title='3D plot of plane path over the poles')

# Show the plot
fig.show()
