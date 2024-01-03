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
x0 = [0, 0]

#Zeitspanne
t_span = (0, 50)


#solver zumgenaurenauswerten entweder t-eval oder dense-out = true 
sol = solve_ivp(ODEsystem, t_span, x0, args=(S, phi, A, alpha)) #t_eval=np.linspace(0, 50, 1000)

# Plot both x(t) and y(t) in the same plot
plt.plot(sol.t, sol.y[0], label='x(t)') #y[0] nach der ersten variable in diesem fall x also TSH 
plt.plot(sol.t, sol.y[1], label='y(t)') #y[1] nach der zweiten variable in diesem fall y also FT4 
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend(['TSH', 'FT$'], shadow=True)
plt.show()
