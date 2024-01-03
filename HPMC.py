import numpy as np
import matplotlib.pyplot as plt

# Funktinonen
def HPf(x, s, phi):
    return s / np.exp(phi * x)

def curvHPf(s, phi, x):
    return (s * (phi**2) * np.exp(-phi * x)) / ((1 - (s**2) * (phi**2) * np.exp(-2 * phi * x))**(3/2))

#parameter werte
s = 1000
phi = 0.42


x_values = np.linspace(8,22, 1000)

y_HPf = HPf(x_values, s, phi)
y_curvHPf = curvHPf(s, phi, x_values)

# Finde maximums point von curvHPf
max_index = np.argmax(y_curvHPf)
x_max_curvHPf = x_values[max_index]
y_max_curvHPf = y_curvHPf[max_index]


plt.figure(figsize=(10, 6))

# Plot HPf
plt.plot(x_values, y_HPf, label='HPf(x)')

# Markiere  maximums point von curvHPf in rot
plt.scatter(x_max_curvHPf, y_max_curvHPf, color='red', marker='o', label='Max Point of curvHPf')

#  maximums punkt bis zur x-axe
plt.plot([x_max_curvHPf, x_max_curvHPf], [0, y_max_curvHPf], '--', color='blue')

plt.title('HPf and Max Point of curvHPf')
plt.xlabel('x')
plt.ylabel('Function Values')
plt.legend()
plt.grid(True)
plt.show()