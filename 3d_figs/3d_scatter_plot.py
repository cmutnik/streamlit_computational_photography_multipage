"""
3d_scatter_plot.py
https://www.tutorialspoint.com/plotly/plotly_3d_scatter_and_surface_plot.htm
"""
from plotly.offline import iplot
import plotly.graph_objs as go
import numpy as np

z = np.linspace(0, 10, 50)
x = np.cos(z)
y = np.sin(z)
trace = go.Scatter3d(
   x = x, y = y, z = z,mode = 'markers', marker = dict(
      size = 12,
      color = z, # set color to an array/list of desired values
      colorscale = 'Viridis'
      )
   )
layout = go.Layout(title = '3D Scatter plot')
fig = go.Figure(data = [trace], layout = layout)
iplot(fig)
