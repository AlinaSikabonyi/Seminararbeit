import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parameters import *

#parameters for each pateint taken from parameters.py

# HPf function definition
def ODEsystem(t, z, S, phi, A, alpha):
    x, y = z
    dx_dt = S / np.exp(phi * y) - x
    dy_dt = A - (A / np.exp(alpha * x)) - y
    return [dx_dt, dy_dt]


x0 = [0, 0]


t_span = (0, 50)



sol = solve_ivp(ODEsystem, t_span, x0, args=(S, phi, A, alpha)) #t_eval=np.linspace(0, 50, 1000)

# Plot both x(t) and y(t) in the same plot
plt.plot(sol.t, sol.y[0], label='x(t)')
plt.plot(sol.t, sol.y[1], label='y(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend(['x', 'y'], shadow=True)
plt.show()