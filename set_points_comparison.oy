import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parameters import *

# Define function and solve ODE
def ODEsystem(t, z, S, phi, A, alpha):
    x, y = z
    dx_dt = S / np.exp(phi * y) - x
    dy_dt = A - (A / np.exp(alpha * x)) - y
    return [dx_dt, dy_dt]

x0 = [0.02, 1.41 * 0.077]
t_span = (0, 50)
sol = solve_ivp(ODEsystem, t_span, x0, args=(S, phi, A, alpha))
last_time_point = sol.t[-1] #nimmt durch -1 den letzten Wert von hinten bei Zeit
last_x_value = sol.y[0, -1]  # Wert von x zum letzten Zeitpunkt
last_y_value = sol.y[1, -1]  # Wert von y zum letzten Zeitpunkt

#numerical set point
x_n = last_x_value
y_n = last_y_value

# Maximum curvature (hp)
x_mc1 = 1 / (np.sqrt(2) * phi)
y_mc1 = (np.log(2 * S * phi) / phi)

# Maximum curvature (t)
x_mc2 = np.log(np.sqrt(2) * A * alpha) / alpha
y_mc2 = A - (1 / (2 * alpha))

# Gain factor analysis
x_gf = 1 / alpha
y_gf = A * (1 - np.exp(-1))

# Calculate distances
dist_N_MC1 = np.linalg.norm(np.array([x_n, y_n]) - np.array([x_mc1, y_mc1]))
dist_N_MC2 = np.linalg.norm(np.array([x_n, y_n]) - np.array([x_mc2, y_mc2]))
dist_N_GF = np.linalg.norm(np.array([x_n, y_n]) - np.array([x_gf, y_gf]))

# Print results
print('The difference between the numerical set point and MC1 is:')
print('TSH:', abs(x_n - x_mc1), 'FT4:', abs(y_n - y_mc1), 'Distance:', dist_N_MC1)

print('The difference between the numerical set point and MC2 is:')
print('TSH:', abs(x_n - x_mc2), 'FT4:', abs(y_n - y_mc2), 'Distance:', dist_N_MC2)

print('The difference between the numerical set point and GF is:')
print('TSH:', abs(x_n - x_gf), 'FT4:', abs(y_n - y_gf), 'Distance:', dist_N_GF)

# Scatter plot
plt.scatter([x_n], [y_n], label='Numerical Set Point')
plt.scatter([x_mc1], [y_mc1], label='Maximum Curvature (HP)')
#plt.scatter([x_mc2], [y_mc2], label='Maximum Curvature (T)')
plt.scatter([x_gf], [y_gf], label='Gain Factor')
plt.legend()
plt.xlabel('TSH')
plt.ylabel('FT4')
plt.show()

# Scatter plot
plt.scatter([x_n], [y_n], label='Numerical Set Point')
plt.scatter([x_mc1], [y_mc1], label='Maximum Curvature (HP)')
plt.scatter([x_mc2], [y_mc2], label='Maximum Curvature (T)')
plt.scatter([x_gf], [y_gf], label='Gain Factor')
plt.legend()
plt.xlabel('TSH')
plt.ylabel('FT4')
plt.show()
