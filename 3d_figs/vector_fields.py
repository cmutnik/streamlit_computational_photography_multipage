"""
vector_fields.py
https://blog.plotly.com/post/175740325442/cone-plots-in-plotly-with-python
"""

def three_non_linear_ODEs():
    """This example looks at the Rössler system - a system of three non-linear ordinary differential equations."""
    import plotly
    print(plotly.__version__)
    from scipy.integrate import odeint
    # import plotly.graph_objs as go
    import plotly.plotly as py
    # import plotly.tools as tls
    # import plotly.figure_factory as ff

    # import copy
    # import pandas as pd
    import numpy as np
    # from numpy import pi, sin, cos, sqrt


    def eq_vf(pos, t):
        x, y, z = pos 
        return  -y-z, x+0.2*y, 0.2+z*(x-5.7)
    pos0 = (0.6, 1, .0)
    t = np.arange(0.0, 75, 0.025) 
    pos = odeint(eq_vf, pos0, t)
    x, y, z=pos.T
    x.shape
    (3000,)
    trajectory = dict(type='scatter3d',
                    x=x,
                    y=y,
                    z=z, 
                    mode='lines',
                    line=dict(width=2, 
                                color='rgb(102,135,231)'))
    axis = dict(showbackground=True, 
                backgroundcolor="rgb(235, 235,235)",
                gridcolor="rgb(255, 255, 255)",      
                zerolinecolor="rgb(255, 255, 255)")


    layoutRoss = dict(width=900,
                    height=750,
                    autosize=False,
                    scene=dict( camera=dict(eye=dict(x=1.25, y=-1.40, z=0.5)),
                                xaxis=dict(axis),
                                yaxis=dict(axis), 
                                zaxis=dict(axis),
                                aspectratio=dict(x=1,
                                                y=1,
                                                z=0.85))
                    )
    figR = dict(data=[trajectory], layout=layoutRoss)
    py.iplot(figR, filename='Rossler',validate=False)
    return

def hypothetical_wind_data_in_three_atmospheric_layers():
    """This example looks at hypothetical wind data in three atmospheric layers."""
    import plotly
    print(plotly.__version__)
    import plotly.graph_objs as go
    import plotly.plotly as py
    import plotly.tools as tls
    import plotly.figure_factory as ff

    import copy
    import pandas as pd
    import numpy as np
    from numpy import pi, sin, cos, sqrt


    x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.8))


    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
        np.sin(np.pi * z))
    def flatten_vf(x, y, z, u, v, w):
        return x.flatten(), y.flatten(), z.flatten(), u.flatten(), v.flatten(), w.flatten()
    x, y, z, u, v, w=flatten_vf(x,y,z,u,v,w)
    pl_deep = [[0.0, 'rgb(39, 26, 44)'],
            [0.1, 'rgb(53, 41, 74)'],
            [0.2, 'rgb(63, 57, 108)'],
            [0.3, 'rgb(64, 77, 139)'],
            [0.4, 'rgb(61, 99, 148)'],
            [0.5, 'rgb(65, 121, 153)'],
            [0.6, 'rgb(72, 142, 157)'],
            [0.7, 'rgb(80, 164, 162)'],
            [0.8, 'rgb(92, 185, 163)'],
            [0.9, 'rgb(121, 206, 162)'],
            [1.0, 'rgb(165, 222, 166)']]
    trace2 = dict(type='cone',
                x=x,
                y=y,
                z=z,
                u=u,
                v=v,
                w=w,
                sizemode='scaled',
                sizeref=0.25, #this is the default value 
                showscale=True,
                colorscale=pl_deep, 
                colorbar=dict(thickness=20, ticklen=4), 
                anchor='tail'
            )
    fig2 = dict(data=[trace2])
    title = 'Vertical levels of a numerical weather model'
    py.iplot(fig2, filename='vertical_levels',validate=False)
    return

if __name__ == "__main__":
    three_non_linear_ODEs()
    hypothetical_wind_data_in_three_atmospheric_layers()
