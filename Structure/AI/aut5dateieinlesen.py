#tflite datein reinladen
#eingabe ausgabe holen
#kamera bilder einlesen
#berechnen der ausgaben
#funktionen aufrufen

import cv2 
import tensorflow as tf 
# Lade das neuronale Netzwerk aus der .tflite-Datei 
interpreter = tf.lite.Interpreter(model_path="model.tflite") 
# Stelle sicher, dass das neuronale Netzwerk bereit ist 
interpreter.allocate_tensors() 
# Hole die Eingabe- und Ausgabe-Tensoren des neuronale Netzwerks 
input_tensor_index = interpreter.get_input_details()[0]["index"] 
output_tensor_index = interpreter.get_output_details()[0]["index"] 
# Lese das Bild von der CSI-Kamera 
image = read_image_from_camera() 
# Funktion zum Lesen des Bildes
# Öffne die CSI-Kamera und lese Bilder von ihr 
camera = cv2.VideoCapture(0) 
while True: 
    #geht auch
    # image = read_image_from_camera() 
    # input_data[0] = image
    # Lese das nächste Bild von der Kamera 
    frame = camera.read()
    # Setze das Bild als Eingabe für das neuronale Netzwerk 
    input_data = interpreter.tensor(input_tensor_index) 
    input_data[0] = frame
    # Führe Berechnungen mit dem neuronale Netzwerk durch 
    interpreter.invoke() 
    # Hole die Ergebnisse der Berechnungen 
    output_data = interpreter.tensor(output_tensor_index) 
    steering, throttle = output_data[0] 
    # Verwende die Berechnungen, um den Lenk-Einschlag und Throttle zu steuern 
    control_steering(steering) 
    # Funktion zum Steuern des Lenk-Einschlags 
    control_throttle(throttle) 
    # Funktion zum Steuern der Throttle