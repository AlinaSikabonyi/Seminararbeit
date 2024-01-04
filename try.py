from parameters import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def T(x, A, alpha):
    return A - (A / np.exp(alpha * x))

def curvT(x, A, alpha):
    y = (-A * (alpha ** 2) * (np.exp(alpha * x))) / ((1 + A ** 2 * alpha ** 2 * np.exp(-2 * alpha * x)) ** (3 / 2))
    return y


plt.plot(x_val, y_val, label='T(x)')

#plt.scatter(max_x, T(max_x, A, alpha), color='red')
plt.xlabel('TSH (mU/L)')
plt.ylabel('FT4 (pmol/L)')
plt.legend()
plt.show()
