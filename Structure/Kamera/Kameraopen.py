import picamera
# Erstelle ein Objekt der Kamera-Klasse 
camera = picamera.PiCamera() 
# Stelle sicher, dass die Kamera bereit ist 
camera.start_preview() 
# Lese ein Bild von der Kamera ein und speichere es in der Variablen "image" 
image = camera.capture() 