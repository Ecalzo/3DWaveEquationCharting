#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:33:16 2018

@author: ec
"""

# countour map -- topographical data, or anything in 3 dimensions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import numpy as np

df = pd.read_csv('Data.csv')
xyz = np.array(df[['x','t','z']])
afont = {'fontname':'Arial'}

# reshaping into 2D arrays to function with matplotlib
x = xyz[:,0]
X = np.reshape(x, (33, 11))
y = xyz[:,1]
Y = np.reshape(y, (33, 11))
z = xyz[:,2]
Z = np.reshape(z, (33, 11))

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# set x, y, and z labels, sizes and paddings
ax.set_xlabel('Distance', size = 15, labelpad=10, **afont)
ax.set_ylabel('Time', size = 15, labelpad=10, **afont)
ax.set_zlabel('Displacement', size=15, labelpad=5, **afont)

# set the tick size - set y and z first, then rotate x if needed
ax.tick_params(labelsize=10)
#ax.tick_params(axis='x', labelrotation=70)

plt.suptitle('Wave Displacement as a Function of Distance and Time with a = 1', size = 15)

# set the font of the labels
for tick in ax.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax.get_yticklabels():
    tick.set_fontname("Arial")
for tick in ax.get_zticklabels():
    tick.set_fontname("Arial")

ax.plot_surface(X,Y,Z, rstride = 1, cstride = 1, cmap='hot', antialiased=True, shade=False)
#plt.savefig('heatMapGraph.png', dpi=600, bbox_inches='tight')
plt.show()

