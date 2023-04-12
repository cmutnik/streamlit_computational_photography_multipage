"""
# https://sabopy.com/py/matplotlib-3d-33/#toc2
import matplotlib
print(matplotlib.__version__)
3.3.3
print(np.__version__)
1.19.5
"""

# !pip install matplotlib==3.3.3 numpy==1.19.5


from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from IPython.display import HTML
import numpy as np

fig = plt.figure(figsize=(6,6))
ax = fig.gca(projection='3d')
ax.set_box_aspect((1,1,1))
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_zlim(-12, 12) 
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 10)

x= 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
scat1, = ax.plot(x[0,::2],y[0,::2],z[0,::2],alpha=0.5, lw=0, marker="o",color='tab:green')
scat2, = ax.plot(x[0,1::2],y[0,1::2],z[0,1::2],alpha=0.5, lw=0, marker="o",color='tab:red')
def init():
    return scat1, scat2, 

def animate(i):
    
    scat1.set_data((x[:i,::2].flatten(),y[:i,::2].flatten()))
    scat1.set_3d_properties(z[:i,::2].flatten())
    scat2.set_data((x[:i,1::2].flatten(),y[:i,1::2].flatten()))
    scat2.set_3d_properties(z[:i,1::2].flatten())
    return scat1, scat2, 
    

ani = animation.FuncAnimation(fig, animate, 100,
                                   interval=100, init_func=init, blit=True, repeat=True)
ani.save('point_anim.mp4', writer="ffmpeg",dpi=100)
HTML(ani.to_html5_video())
