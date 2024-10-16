import numpy as np
import matplotlib.pyplot as plt 

a = np.load('/home/aravindh/rail_bot.npy')
print(np.shape(a))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(a[:,0],a[:,1],a[:,2])
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()