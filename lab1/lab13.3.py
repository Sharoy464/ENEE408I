##part 1: (1) Create a line plot of the sine function over the interval [0, 2π] using Matplotlib.##
##part(2) Add labels to the axes in a Matplotlib plot.##

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Function")
plt.show()


##(3) Plot the 3d graph of the function given below using Matplotlib.##
#𝑧 = 𝑠𝑖𝑛 (√𝑥2 + 𝑦2)##

import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)
y = np.linspace(-6, 6, 200)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
