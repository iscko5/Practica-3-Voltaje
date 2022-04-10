import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def getSerialData(self, Samples, serialConnection, lines1, lines2, lineValueText, lineLabel):
    valueP1 = float(serialConnection.readline().strip())  # Lee sensor
    valueP2 = float(serialConnection.readline().strip())  # Lee sensor
    data0.append(valueP1)  # Guarda la última posición.
    data1.append(valueP2)
    lines1.set_data(range(Samples), data0)  # Dibuja la linea
    lines2.set_data(range(Samples), data1)  # Dibuja la linea
    # Muestr valores del sensor del line
    lineValueText.set_text(lineLabel + ' = ' + str(round(valueP1, 2)))
    lineValueText.set_text(lineLabel + ' = ' + str(round(valueP2, 2)))


# Inicialización del puerto de ejecución
serialPort = '/dev/ttyACM0'
baudRate = 9600

try:
    serialConnection = serial.Serial(
        serialPort, baudRate)  # Instancia objeto Serial
except:
    print("Error de conexion")

Samples = 100
data0 = collections.deque([0] * Samples, maxlen=Samples)  # Vector de muestras
data1 = collections.deque([0] * Samples, maxlen=Samples)  # Vector de muestras
sampleTime = 100  # Tiempo de muestreo

# Limites de los ejes
xmin = 0
xmax = Samples
ymin = 0
ymax = 6  # Sería 5 volts pero +1

fig = plt.figure(figsize=(13, 6))  # Crea la figura
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
plt.title("Lectura del sensor en tiempo real")
ax.set_xlabel("Muestra")
ax.set_ylabel("Voltaje")

lineLabel = 'Voltaje'
lines1 = ax.plot([], [], label=lineLabel)[0]  # Grafica datos iniciales
lines2 = ax.plot([], [], label=lineLabel)[0]  # Grafica datos iniciales
lineValueText = ax.text(0.85, 0.95, '', transform=ax.transAxes)

anim = animation.FuncAnimation(fig, getSerialData, fargs=(
    Samples, serialConnection, lines1, lines2, lineValueText, lineLabel), interval=sampleTime)

plt.show()
serialConnection.close()
