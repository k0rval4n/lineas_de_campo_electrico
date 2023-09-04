"""Graficar lineas de campo correspondientes a 2 cargas con valores y posiciones arbitrarias en 2 dimensiones"""

# Se importan los modulos necesarios: Numpy, Matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Inicia programa
"""
#DEV INPUTS
l = 10
q1 = 1
q1x = 1
q1y = 0
q2 = -1
q2x = -1
q2y = 0
"""
K = 9*(10**9)  # Valor constante de Coulomb.

# Se le solicita al usuario introducir los datos necesarios.
# Si el interprete no deja introducir inputs, comentar esta seccion (""") e introducir manualmente los DEV INPUTS  en el codigo.
l = float(input("Indique el limite de la region a representar: "))  # Se pregunta los limites a representar.
q1 = float(input("Indique la carga de q1: "))
q1x = float(input("Indique la coordenada x de q1: "))
q1y = float(input("Indique la coordenada y de q1: "))
#norma1 = ((X-q1x)**2+(Y-q1y)**2)
q2 = float(input("Indique la carga de q2: "))
q2x = float(input("Indique la coordenada x de q2: "))
q2y = float(input("Indique la coordenada y de q2: "))
#norma2 = ((X-q2x)**2+(Y-q2y)**2)

bordes = [q1x, q1y, q2x, q2y]
for coord in bordes:
    if coord > l:
        l = 1.1*coord

x = np.arange(-l,l,0.01)
y = np.arange(-l,l,0.01)

X,Y = np.meshgrid(x,y)

# Se expresa la ecuación del campo electrico para cada eje (X e Y).
Ex = (K*q1)/(((X-q1x)**2+(Y-q1y)**2)**(3/2)) * (X-q1x) + (K*q2)/(((X-q2x)**2+(Y-q2y)**2)**(3/2)) * (X-q2x)
Ey = (K*q1)/(((X-q1x)**2+(Y-q1y)**2)**(3/2)) * (Y-q1y) + (K*q2)/(((X-q2x)**2+(Y-q2y)**2)**(3/2)) * (Y-q2y)

# Se crea la figura base.
fig, ax = plt.subplots(figsize=(7,7))
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.text(l, 1.01*(l), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

# Se utiliza la funcion streamplot para generar las lineas del campo dado anteriormente.
ax.streamplot(X, Y, Ex, Ey, color="black")
ax.set_aspect("equal")

# Se agrega la representacion grafica de la carga puntual, junto con su color y su signo.
if q1 > 0:
    ax.plot(q1x, q1y, "-o", markersize=20, color="coral")
    ax.text(q1x, q1y, "+", ha="center", va="center", size=12, weight="bold", color="black")
elif q1 < 0:
    ax.plot(q1x, q1y, "-o", markersize=20, color="cornflowerblue")
    ax.text(q1x, q1y,"-", ha="center", va="center", size=20, weight="bold", color="black")
if q2 > 0:
    ax.plot(q2x, q2y, "-o", markersize=20, color="coral")
    ax.text(q2x, q2y, "+", ha="center", va="center", size=12, weight="bold", color="black")
elif q2 < 0:
    ax.plot(q2x, q2y, "-o", markersize=20, color="cornflowerblue")
    ax.text(q2x, q2y, "-", ha="center", va="center", size=20, weight="bold", color="black")

# Muestra la figura.
plt.show()
