## Part One : (1) Solve the linear system of equations given below using SciPy.##
#3𝑥 + 𝑦 = 9##
#𝑥 + 2𝑦 = 8##


import numpy as np
from scipy.linalg import solve

print("\n First Part: \n")

A = np.array([[3, 1],
              [1, 2]])


b = np.array([9, 8])


solution = solve(A, b)

print("x =", solution[0])
print("y =", solution[1])


## Part Two :  Find the minimum of the function given below using SciPy's optimization module. 𝑦 = 𝑥2 + 2𝑥 ##

print("\n Second Part: \n")

from scipy.optimize import minimize

def f(x):
    return x**2 + 2*x

x0 = 0

result = minimize(f, x0)

print("Minimum x:", round(result.x[0], 0))
print("Minimum value:", round(result.fun, 0))


## Part Three : ) Perform the Fourier transformation of the function given below using SciPy. Plot the frequency response using matplotlib. ##
# f(x) = sin(100πx) + 1/2 sin(160πx)##

print("\n Third Part: \n")

import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


Fs = 2000  
T = 1.0    
N = int(Fs * T)

x = np.linspace(0, T, N, endpoint=False)


f = np.sin(100*np.pi*x) + 0.5*np.sin(160*np.pi*x)


F = fft(f)
freqs = fftfreq(N, d=1/Fs)


pos = freqs >= 0
freqs_pos = freqs[pos]
mag_pos = np.abs(F[pos]) / N  


plt.figure()
plt.plot(freqs_pos, mag_pos)
plt.xlim(0, 200)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Response")
plt.grid(True)
plt.show()




