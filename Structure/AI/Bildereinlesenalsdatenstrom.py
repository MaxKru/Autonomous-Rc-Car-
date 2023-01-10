import io
import sqlite3
import time


# Iteriere über die Datensätze und erstelle Eingabe- und Ziel-Tensoren
inputs = []
targets = []
for steering, throttle, image in cursor:
    # Funktion zum Decodieren des Bildes
    inputs.append(decode_image(image))
    targets.append((steering, throttle))

# Erstelle das neuronale Netzwerk und trainiere es mit den Daten
# Funktion zum Erstellen des Netzwerks
model = create_model()
model.fit(inputs, targets, epochs=10)


# Stelle eine Verbindung zur Datenbank her
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

while True:
    # Lese die aktuellen Lenk-Einschlag- und Throttle-Werte aus dem Joystick
    steering = read_joystick_steering()  # Funktion zum Lesen des Lenk-Einschlags
    throttle = read_joystick_throttle()  # Funktion zum Lesen des Throttles

    # Schreibe die Werte in die Datenbank
    timestamp = datetime.now()
    conn.execute(""" 
        INSERT INTO data (timestamp, steering, throttle) 
        VALUES (?, ?, ?) 
    """, (timestamp, steering, throttle))
    conn.commit()

    # Warte 1/10 Sekunde, bevor die nächsten Werte gelesen werden
    time.sleep(0.1)
# Schließe die Verbindung zur Datenbank
#conn.close()
