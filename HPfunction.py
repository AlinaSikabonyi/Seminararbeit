from parameters import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def HPf(x, phi, S):
    return S / (np.exp(phi * x))

def curvHPf(x, S, phi):
    y = S * phi**2 * np.exp(-phi * x)/((1 - S**2 * phi**2 * np.exp(-2 * S * phi * x))**(3/2))
    return y

x_val = np.linspace(8, 22, 300)
y_val = HPf(x_val, phi, S)

#print(HPf(x_val, phi, S))
plt.plot(x_val, y_val, label = 'HPf')
plt.xlabel('Time')
plt.ylabel('Values')
plt.show()

