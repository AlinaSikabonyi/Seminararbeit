import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parameters import *

#parameters for each pateint taken from parameters.py

#ODE system defniert input vektor output AUCH vektor
def ODEsystem(t, z, S, phi, A, alpha):
    x, y = z
    dx_dt = S / np.exp(phi * y) - x
    dy_dt = A - (A / np.exp(alpha * x)) - y
    return [dx_dt, dy_dt]

#AWP
x0 = [0.02, (1.41 * 0.077)]

#Zeitspanne
t_span = (0, 50)


#solver zumgenaurenauswerten entweder t-eval oder dense-out = true
sol = solve_ivp(ODEsystem, t_span, x0, args=(S, phi, A, alpha)) #t_eval=np.linspace(0, 50, 1000)


last_time_point = sol.t[-1] #nimmt durch -1 den letzten Wert von hinten bei Zeit
last_x_value = sol.y[0, -1]  # Wert von x zum letzten Zeitpunkt
last_y_value = sol.y[1, -1]  # Wert von y zum letzten Zeitpunkt


print('SET POINT EQUATIONS')
print('Numerical Set Point:')
print("TSH:", last_x_value)
print("FT4:", last_y_value)

print('Maximum Curvature Theory:')
print('1)')
print('TSH:',  1 / (np.sqrt(2) * phi))
print('FT4:', (np.log(2 * S * phi) / phi))

print('2)')
print('TSH:', np.log(np.sqrt(2) * A * alpha) / alpha)
print('FT4:', (A - (1 / (2 * alpha))))



print('gain factor analysis:')
print('TSH:', 1 / (alpha))
print('FT4:', A * ( 1  - np.exp(-1)))



plt.scatter(last_time_point, last_x_value, color = 'red' )
plt.scatter(last_time_point, last_y_value, color = 'red' )

# Plot both x(t) and y(t) in the same plot
plt.plot(sol.t, sol.y[0], label='x(t)') #y[0] nach der ersten variable in diesem fall x also TSH
plt.plot(sol.t, sol.y[1], label='y(t)') #y[1] nach der zweiten variable in diesem fall y also FT4
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend(['TSH', 'FT4'], shadow=True)
plt.show()
