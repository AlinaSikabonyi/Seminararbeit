from parameters import *
import numpy as np
import matplotlib.pyplot as plt

#HP funktion
def HPf(x, phi, S):
    return S / (np.exp(phi * x))

#erste ableitung
def d(x, phi, S):
    return -S * phi / np.exp(phi * x)
    #return np.gradient(HPf(x, S, phi), x)

#zweite ableitung
def d_2(x, phi, S):
    return S * phi ** 2 / np.exp(phi * x)
    #return np.gradient(d(x, S, phi), x)

#Krümmung
def curvHPf(x, S, phi):
    d_x = d(x, phi, S)  # Auswerten der ersten Ableitung an den Stellen x
    d_2_x = d_2(x, phi, S)  # Auswerten der zweiten Ableitung an den Stellen x
    y = d_2_x / ((1 + d_x ** 2) ** (3 / 2))
    return y

#def curvHPf(x, S, phi):
    #y = (S * phi**2 * np.exp(-phi * x))/((1 - S**2 * phi**2 * np.exp(-2 * S * phi * x))**(3/2))
    #return y

#Ableitung der krümmung
def dercurvHPF(x, S, phi):
    return np.gradient(curvHPf(x,S,phi),x)

x_val = np.linspace(8, 22, 300)
y_val = HPf(x_val, phi, S)

fig, ax1 = plt.subplots()

#HP funktion
color = 'tab:blue'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('HPf', color=color)
ax1.plot(x_val, y_val, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() #selbe x-achse unterschiedliche y-achse

#krümmung
color = 'tab:red'
ax2.set_ylabel('curvature', color=color)
ax2.plot(x_val, curvHPf(x_val, S, phi), color=color)
ax2.plot(x_val, dercurvHPF(x_val, S, phi), linestyle='dashed', color=color)
ax2.tick_params(axis='y', labelcolor=color)
#x achse auf höhe deds zweiten plots
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)

#funltioniert leider nicht
crossings = np.where(np.diff(np.sign(dercurvHPF(x_val, S, phi))) != 0)[0]
intersection_x = x_val[crossings[0]]
ax1.plot([intersection_x, intersection_x], [0, HPf(intersection_x, S, phi)], color='black', linestyle='--')

fig.tight_layout()
plt.show()

