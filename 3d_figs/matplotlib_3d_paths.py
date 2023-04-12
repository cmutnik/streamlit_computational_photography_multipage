"""
matplotlib_3d_paths.py
https://www.tutorialspoint.com/matplotlib/matplotlib_three_dimensional_plotting.htm
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def line_plot_3d():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    ax.plot3D(x, y, z, 'gray')
    ax.set_title('3D line plot')
    plt.show()
    return

def ax_scatter3D_plot():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y
    ax.scatter(x, y, z, c=c)
    ax.set_title('3d Scatter plot')
    plt.show()
    return

def plotting_contour_graphs():
    """Plotting contour graphs.
        
    https://www.geeksforgeeks.org/three-dimensional-plotting-in-python-using-matplotlib/
    """
    def f(x, y):
        """Function for z-axis."""
        return np.sin(np.sqrt(x ** 2 + y ** 3))
    
    # x and y axis.
    x = np.linspace(-1, 5, 10)
    y = np.linspace(-1, 5, 10)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    
    # ax.contour3D is used plot a contour graph.
    ax.contour3D(X, Y, Z)
    return

def plotting_surface_triangulations():
    """Function for plotting surface triangulations.
    
        https://www.geeksforgeeks.org/three-dimensional-plotting-in-python-using-matplotlib/
    """    
    # Angle and radius.
    theta = 2 * np.pi * np.random.random(100)
    r = 6 * np.random.random(100)
    
    # All three axes.
    x = np.ravel(r * np.sin(theta))
    y = np.ravel(r * np.cos(theta))
    z = f(x, y)
    
    ax = plt.axes(projection ='3d')
    ax.scatter(x, y, z, c = z, cmap ='viridis', linewidth = 0.25);
    
    ax = plt.axes(projection ='3d')
    ax.plot_trisurf(x, y, z, cmap ='viridis', edgecolor ='green');
    return


if __name__ == "__main__":
    line_plot_3d()
    ax_scatter3D_plot()
    plotting_contour_graphs()
    plotting_surface_triangulations()
