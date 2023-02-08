import matplotlib.pyplot as plt 
import numpy as np


# set surface plots
b0 = np.arange(-200, 200, 5)
b1 = np.arange(-200, 200, 5)
x, y = np.meshgrid(b0, b1)

def surface_plot(b0,b1,z1):
   # x, y = np.meshgrid(x,y)
    
    fig1 = plt.figure(figsize = (6,6))
    axl = plt.axes(projection = '3d')
    surf1 = axl.plot_surface(x,y,z1,cmap=plt.cm.viridis)

    #set axis labels
    axl.set_xlabel("x", labelpad= 10)
    axl.set_ylabel("y", labelpad= 10)
    axl.set_zlabel("z", labelpad= 0)

    fig1.colorbar(surf1, shrink = .5, aspect = 20, location = "left")
    plt.show




def contour_plot(x,y,f, grid_lines=50):
    x, y = np.mesh(x,y)
    z = f(x,y)
    plt.figure(figsize=(8,8))
    cp = plt.contour(x,y,z, grid_lines)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    plt.show()
    
    
 