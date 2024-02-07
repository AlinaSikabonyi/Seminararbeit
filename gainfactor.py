import numpy as np
from math import e
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parametrs import *

#gain function
def gain(x, A, a, phi):
    y = A * a * phi * x * e**(-a * x)
    return y

#ableitung
def gain_derivative(x, A, a, phi):
    dy_dx = A * phi * e**(-a * x) * (a - a * x)
    return dy_dx

#hoffe der linspace passt
x_values = np.linspace(0, 20, 100)  

# values ausspucken für jedes x
gain_values = gain(x_values, A, a, phi)
derivative_values = gain_derivative(x_values, A, a, phi)
#print(gain_values)


plt.figure(figsize=(8, 6))
plt.plot(x_values, gain_values, label='Gain')
plt.plot(x_values, derivative_values, label='Gain Derivative', linestyle='--', color='orange')
plt.title('Gain and Its Derivative vs. x')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
