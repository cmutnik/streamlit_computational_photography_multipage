"""
3d_surface_plot.py
https://www.tutorialspoint.com/plotly/plotly_3d_scatter_and_surface_plot.htm
"""
from plotly.offline import iplot
import plotly.graph_objs as go
import numpy as np

x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T # transpose
z = np.cos(x ** 2 + y ** 2)
trace = go.Surface(x = x, y = y, z =z )
data = [trace]
layout = go.Layout(title = '3D Surface plot')
fig = go.Figure(data = data)
iplot(fig)
