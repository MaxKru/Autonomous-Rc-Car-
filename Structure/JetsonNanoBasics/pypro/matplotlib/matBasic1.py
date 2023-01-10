import matplotlib.pyplot as plt
import numpy as np

#erstellen von zwei arrays von hand
#x = [1,2,3,4]
#y = [3,5,7,9]
#z = [10,8,6,4]

#arange welchen abstand die werte haben sollen
#x=np.arange(-4,4,.1)
#angage wie viele daten punkte man möchte
x=np.linspace(-4,4,25)
#y=x*x
y=np.square(x)
y2=x*x+2
#y2=np.square(x)+2
y3 = x*x-2

# * heißt zeig nur die punkte
# - heißt zeig auch die linie
# r heißt rote linie
# -- zeigt gepunktete linie
# -.   :   
# linewidth = 3 linie dicker

#grid aktivieren
plt.grid(True)

plt.xlabel('Spannung / V')
plt.ylabel('Zeit / t')

plt.title("Spanung überzeit")

#achsen skalieren
#plt.axis([0,5,2,12])

#plotten der arrays
plt.plot(x,y,'r-*',linewidth=3, markersize=9, label = "Rote linie")
#plt.plot(x,z,'b:^',linewidth=3, markersize=9, label = "Blaue linie")
plt.plot(x,y2,'b:^',linewidth=3, markersize=9, label = "Blaue linie")
plt.plot(x,y3,'g-o',linewidth=3, markersize=9, label = "grüne linie")
#damit die labels angezeigt werden muss man die label in eine legende schrieben
plt.legend(loc='upper center')

plt.show()



