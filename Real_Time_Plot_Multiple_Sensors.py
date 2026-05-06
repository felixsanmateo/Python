import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np



def getSerialData(self,Samples,numData,serialConnection,lines):

    for i in range(numData):
        real = value = float(serialConnection.readline().strip())  #Leer sensor / Read sensor
        data[i].append(value) #Guarda lectura en la última posición / #Save reading in the end position
        lines[i].set_data(range(Samples),data[i]) # Dibujar nueva linea / Drawn new line
        
        if i == 0:
            linea1, = ax1.plot(1, label="ph", color='blue')
            linea1.set_label(f"{real}")
            ax1.legend(loc=1, handles=[linea1]);

        if i == 1:
            linea2, = ax2.plot(1, label="ppm", color='red')
            linea2.set_label(f"{real}")
            ax2.legend(loc=1, handles=[linea2]);

        if i == 2:
            linea3, = ax3.plot(1, label="ºC", color='yellow')
            linea3.set_label(f"{real}")
            ax3.legend(loc=1, handles=[linea3]);

        if i == 3:
            linea4, = ax4.plot(1, label="NTU", color='green')
            linea4.set_label(f"{real}")
            ax4.legend(loc=1, handles=[linea4]);
        
        
serialPort = 'COM5' # Puerto serial arduino / Arduino serial port
baudRate = 9600  # Baudios

try:
  serialConnection = serial.Serial(serialPort, baudRate) # Instanciar objeto Serial / Instance Serial Object
except:
  print('Cannot conect to the port')

Samples = 600  #Muestras / Samples
sampleTime = 1000  #Tiempo de muestreo / Sample Time
numData = 4

# Limites de los ejes / Axis limit
xmin = 0
xmax = Samples
ymin = [0, 0 , -55 ,0]
ymax = [14, 1000 , 125 , 5]
lines = []
data = []
ph = 0.0

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([1], [1], color='blue'))
    lines.append(Line2D([1], [2], color='red'))
    lines.append(Line2D([2], [1], color='yellow'))
    lines.append(Line2D([2], [2], color='green'))
      

fig = plt.figure()# Crea una nueva figura #Create a new figure.
ax1 = fig.add_subplot(2, 2, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
ax1.title.set_text('PH')
# ax1.set_xlabel("Segundos")
ax1.set_ylabel("PH")
ax1.add_line(lines[0])
ax1.grid(True)

ax2 = fig.add_subplot(2, 2, 2,xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
ax2.title.set_text('Conductividad')
# ax2.set_xlabel("Seguntos")
ax2.set_ylabel("ppm")
ax2.add_line(lines[1])
ax2.grid(True)

ax3 = fig.add_subplot(2, 2, 3,xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
ax3.title.set_text('Temperatura')
ax3.set_xlabel("Segundos")
ax3.set_ylabel("ºC")
ax3.add_line(lines[2])
ax3.grid(True)

ax4 = fig.add_subplot(2, 2, 4,xlim=(xmin, xmax), ylim=(ymin[3] , ymax[3]))
ax4.title.set_text('Turbidez')
ax4.set_xlabel("Segundos")
ax4.set_ylabel("NTU")
ax4.add_line(lines[3])
ax4.grid(True)

    
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)

plt.show()


serialConnection.close() # cerrar puerto serial/ close serial port
 
