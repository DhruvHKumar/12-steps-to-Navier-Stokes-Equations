import numpy                      		  
from matplotlib import pyplot as plt      

nx = 81  
dx = 2 / (nx-1)
nt = 25    
dt = .025  
c = 1      

u = numpy.ones(nx)      
u[int(.5 / dx):int(1 / dx + 1)] = 2  
print(u)
plt.plot(numpy.linspace(0, 2, nx), u);

un = numpy.ones(nx) 
for n in range(nt):  
    un = u.copy() 
    for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    plt.plot(numpy.linspace(0, 2, nx), u);

print(u)
plt.show()
