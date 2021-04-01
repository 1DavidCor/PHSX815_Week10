# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:35:49 2021

@author: d338c921
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

#Write a program that can find the minimum of a function that you define. The function can be any one (even very simple) as long as it actually has a minimum. 
#You are welcome to use any standard or external C++ or Python libraries (you don't need to implement the minimization routine, only the function to be minimized).
#You can also try to visualize your function and the location of the minimum (not required).

#define the function to be minimized; write f(x, y) as f(x = x[0], y = x[1])
f = lambda x: x[0]**2 + x[0] + 2*x[1]**2 + 1

#find the coordinates of the minimum; Note: scipy.optimize.minimize can only handle "objective functions"
#As I understand it, objective functions are written in terms of one variable x in such a way that f(w, y, z) = f(x) where x is an array: (x, y, z) 
minimum = optimize.minimize(f, x0 = ((0, 0)))

#min coordinates
x_min = minimum.x[0]
y_min = minimum.x[1]
#y coordinate
f_min = f((x_min, y_min))

#set an x, y arrays for plotting
x = np.linspace(x_min - 10, x_min + 10, 2000)
y = np.linspace(y_min - 10, x_min + 10, 2000)

#set grid for 3D plot
xg, yg = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection ="3d")
ax.scatter3D(x_min, y_min, f_min, marker = "o", color = 'r', label = "minimum")
ax.plot_surface(xg, yg, f((xg, yg)), cmap = plt.cm.rainbow)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Minimizing 2D Functions; min @ (' + str(np.round(x_min, 2)) + ', ' + str(np.round(y_min, 2)) + ', ' + str(np.round(f_min, 2)) + ')')

print("Number of Function Evaluations: " + str(minimum.nfev))