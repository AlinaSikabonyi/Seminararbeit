import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parameters import *

# HPf function definition
def HPf(t, z, alpha, A, S, phi):
    x, y = z
    dx_dt = S / np.exp(phi * y) - x
    dy_dt = A - (A / np.exp(alpha * x)) - y
    return [dx_dt, dy_dt]

sol = solve_ivp(HPf, [0, 50], [0, 0], args=(alpha, A, S, phi), dense_output=True)

t = np.linspace(0, 50, 300)
z = sol.sol(t)

plt.plot(t, z.T)
plt.xlabel('t')
plt.legend(['x', 'y'], shadow=True)
plt.title('Lotka-Volterra System')
plt.show()