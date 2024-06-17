from parameters import *
import numpy as np
import matplotlib.pyplot as plt

#HP funktion
def HPf(x, phi, S):
    return S / (np.exp(phi * x))

#inverse T funktion
def inverse_T(x, A, alpha):
    return np.log(A / (A - x)) / alpha


x_val = np.linspace(8, 22, 300)

#schnittpunkt der beiden funtionen berechnen
HP_values = HPf(x_val, phi, S)
inverse_T_values = inverse_T(x_val, A, alpha)
index = np.argmin(np.abs(HP_values - inverse_T_values))

plt.plot(x_val, HPf(x_val, phi, S), color = 'blue')
plt.plot(x_val, inverse_T(x_val, A, alpha), color = 'red')
plt.plot(x_val[index], HP_values[index], 'ro')
plt.ylim(0,8)
plt.show()
print('set point is', HP_values[index])
print( A * (1 - (np.exp(-1))) , 1/alpha)
