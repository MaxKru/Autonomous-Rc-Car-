import cv2  # Importieren von OpenCV zur Verwendung der Kamera
import tensorflow as tf  # Importieren von TensorFlow zur Verwendung des neuronalen Netzes

# Definieren des neuronalen Netzes (hier wird ein einfaches Netz mit einer versteckten Schicht verwendet)
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Eingabeschicht mit 28x28 Bildern
    tf.keras.layers.Dense(128, activation='relu'),  # Versteckte Schicht mit 128 Neuronen
    tf.keras.layers.Dense(10, activation='softmax') # Ausgabeschicht mit 10 Neuronen für die 10 Klassen
])

# Laden von vortrainierten Gewichten für das Netz (hier wird das MNIST-Datenset verwendet)
model.load_weights('mnist_model.h5')

# Verbinden mit der Kamera (in diesem Beispiel wird die erste Kamera verwendet)
cap = cv2.VideoCapture(0)

# Festlegen der Aufnahmefrequenz (in diesem Beispiel wird alle 5 Sekunden ein Bild aufgenommen)
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = int(5 * fps)  # Wartezeit in Millisekunden

while True:  # Endlosschleife zum Aufnehmen und Klassifizieren von Bildern
    ret, frame = cap.read()  # Aufnehmen eines Bilds
    if not ret:  # Überprüfen, ob das Bild erfolgreich aufgenommen wurde
        break

    # Vorverarbeitung des Bilds für das neuronale Netz
    # (hier wird das Bild skaliert und in ein NumPy-Array umgewandelt)
    frame = cv2.resize(frame, (28, 28))
    frame = frame.astype('float32') / 255

    # Klassifizierung des Bilds mithilfe des neuronalen Netzes
    prediction = model.predict(frame[None, :, :, :])  # Füttern des Netzes mit dem Bild
    prediction_class = prediction.argmax()  # Bestimmung der vorhergesagten Klasse


    # Anzeigen des Klassifizierungsergebnisses auf dem Bild
    cv2.putText(frame, f'Prediction: {prediction_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Anzeigen des aktuellen Bilds mit Klassifizierungsergebnis
    cv2.imshow('frame', frame)

    # Warten auf nächste Aufnahme (in diesem Beispiel alle 5 Sekunden)
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

# Beenden der Verbindung mit der Kamera und Schließen des Fensters
cap.release()
cv2.destroyAllWindows()
