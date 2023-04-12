# https://stackoverflow.com/questions/60685749/python-plotly-how-to-add-an-image-to-a-3d-scatter-plot
import numpy as np
import pandas as pd
from PIL import Image
from scipy import misc
import plotly.express as px
import plotly.graph_objects as go

def make_scatter_plot(show=True):
    # Sample data: 3 trajectories
    t = np.linspace(0, 10, 200)
    df = pd.concat([pd.DataFrame({'x': 900 * (1 + np.cos(t + 5 * i)), 'y': 400 * (1 + np.sin(t)), 't': t, 'id': f'id000{i}'}) for i in [0, 1, 2]])
    # 3d scatter plot
    fig = px.scatter_3d(df, x='x', y='y', z='t', color='id', )
    fig.update_traces(marker=dict(size=2))
    if show:
        fig.show()
    return

def bottom_surface_image_in_3D_scatterplot():
    im = misc.face()
    im_x, im_y, im_layers = im.shape
    eight_bit_img = Image.fromarray(im).convert('P', palette='WEB', dither=None)
    dum_img = Image.fromarray(np.ones((3,3,3), dtype='uint8')).convert('P', palette='WEB')
    idx_to_color = np.array(dum_img.getpalette()).reshape((-1, 3))
    colorscale=[[i/255.0, "rgb({}, {}, {})".format(*rgb)] for i, rgb in enumerate(idx_to_color)]

    # Sample data: 3 trajectories
    t = np.linspace(0, 10, 200)
    df = pd.concat([pd.DataFrame({'x': 400 * (1 + np.cos(t + 5 * i)), 'y': 400 * (1 + np.sin(t)), 't': t, 'id': f'id000{i}'}) for i in [0, 1, 2]])
    # im = im.swapaxes(0, 1)[:, ::-1]
    colors=df['t'].to_list()

    # # 3d scatter plot
    x = np.linspace(0,im_x, im_x)
    y = np.linspace(0, im_y, im_y)
    z = np.zeros(im.shape[:2])
    fig = go.Figure()

    fig.add_trace(go.Scatter3d(
        x=df['x'], 
        y=df['y'], 
        z=df['t'],
        marker=dict(
            color=colors,
            size=4,
        )
        ))

    fig.add_trace(go.Surface(x=x, y=y, z=z,
        surfacecolor=eight_bit_img, 
        cmin=0, 
        cmax=255,
        colorscale=colorscale,
        showscale=False,
        lighting_diffuse=1,
        lighting_ambient=1,
        lighting_fresnel=1,
        lighting_roughness=1,
        lighting_specular=0.5,

    ))

    fig.update_layout(
        title="My 3D scatter plot",
        width=800,
        height=800,
        scene=dict(xaxis_visible=True,
                    yaxis_visible=True, 
                    zaxis_visible=True, 
                    xaxis_title="X",
                    yaxis_title="Y",
                    zaxis_title="Z" ,

        ))


    fig.show()

if __name__ == "__main__":
    make_scatter_plot()
    # plt.clf()
    # add_3d_image_to_scatter_plot()
    bottom_surface_image_in_3D_scatterplot()
