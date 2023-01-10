import matplotlib.pyplot as plt
import numpy as np


#linespace 2*pi mit 100 datenpunkten
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
y2=np.cos(x-np.pi/2)

#grid aktivieren
plt.grid(True)

plt.ylabel('Spannung / V')
plt.xlabel('Zeit / t')

plt.title("Spanung überzeit")

#plotten der arrays
plt.plot(x,y,'b*',linewidth=3, markersize=9, label = "sin(x)")
plt.plot(x,y2,'r-',linewidth=3, markersize=9, label = "cos(x)")

plt.legend(loc='upper center')

plt.show()



