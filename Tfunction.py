from parameters import *
import numpy as np
import matplotlib.pyplot as plt
import math

#Thyroid Function
def T(x, A, alpha):
    return A - (A / np.exp(alpha * x))

#erste Ableitung
def d(x, A, alpha):
    return A * alpha / np.exp(alpha * x)

#zweite Ableitung
def d_2(x, A, alpha):
    return -A * alpha**2 / np.exp(alpha * x)

#Krümmung
def curvT(x, A, alpha):
    d_x = d(x, A, alpha)  #Werte berechnen
    d_2_x = d_2(x, A, alpha)  #Werte berechnen
    y = d_2_x / ((1 + d_x ** 2) ** (3 / 2))
    return y

#erste Ableitung der krümmung
def dercurvT(x, A, alpha):
    return np.gradient(curvT(x, A, alpha), x)

x_val = np.linspace(0, 30, 300)

#finde schnittpunkt von dercurvT und x-achse mittels diesem befehl
crossings = np.where(np.diff(np.sign(dercurvT(x_val, A, alpha))) != 0)[0] #schaut sich die unterschiedlichen vorzeichen an, np.diff schaut änderung der signum funktion an
intersection_x = x_val[crossings[0]] #stellt den x wert fest wo der schnitt liegt und nennt ihn intersepction

fig, ax1 = plt.subplots()

#plot von T fun
color = 'tab:blue'
ax1.set_xlabel('time')
ax1.set_ylabel('Thyroid function', color=color)
ax1.plot(x_val, T(x_val, A, alpha), color=color, label='Thyroid function')
ax1.tick_params(axis='y', labelcolor=color)
ax1.scatter(intersection_x, T(intersection_x, A, alpha), color='red', label='Set point') #plotten von set-point
ax1.plot([intersection_x, intersection_x], [0, T(intersection_x, A, alpha)], color='gray', linestyle='--')# zeiht eine linie durch bis zur T funktion

ax2 = ax1.twinx()  #zweite y achse mit selber x_achse

#curvature function mit anderer y achse
color = 'tab:red'
ax2.set_ylabel('curvature', color=color)
ax2.plot(x_val, curvT(x_val, A, alpha), color=color, label='Curvature')
ax2.plot(x_val, dercurvT(x_val, A, alpha), linestyle='dashed', color=color, label='Derivative of Curvature')
ax2.tick_params(axis='y', labelcolor=color)
#x-achse (zeit achse) auf der höhe des zweiten plots
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)

#legende
plt.legend()
#set point wie in masterarbeit
print((A - (1 / (2 * alpha))), (np.log(np.sqrt(2) * A * alpha) / alpha))
# set point durch diesen code ermittelt
print('the set-point of the Thyroid function is' , T(intersection_x, A, alpha))
plt.show()
