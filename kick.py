from math import pi 

rho = 1.2
A = pi*0.11**2
CD = 0.2
m = 0.43
g = 9.81
Fg = m*g



V = 120*5.0/18


Fd = 0.5*CD*rho*A*V**2


print ('For hard kick (V=%g): Gravitational force (%g) and Drag force (%g)' % (V,Fg,Fd))  


V = 30*5.0/18 


Fd = 0.5*CD*rho*A*V**2  


print ('For soft kick (V=%g): Gravitational force (%g) and Drag force (%g)' % (V,Fg,Fd)) 