import cv2
import numpy as np
import os
import serial
import time
from datetime import datetime

# Initialize serial communication (adjust COM port and baud rate as needed)
serial_port = 'COM1'  # Change to your serial port (e.g., COM3, /dev/ttyUSB0)
baud_rate = 9600
try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud")
    time.sleep(2)  # Allow time for serial connection to stabilize
except serial.SerialException as e:
    print(f"Serial connection failed: {e}")
    ser = None

haar_file = 'haarcascade_frontalface_default.xml'  # Ensure the path is correct
datasets = 'datasets'  # Folder containing your dataset
unknown_folder = 'unknown_person'  # Folder to save unknown person images

# Create unknown_person folder if it doesn't exist
if not os.path.exists(unknown_folder):
    os.makedirs(unknown_folder)

print('Training...')

# Initialize variables
(images, labels, names, id) = ([], [], {}, 0)

# Walk through the dataset directory and load images and labels
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir  # Map subdir names to labels
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))  # Load image in grayscale
            labels.append(int(label))  # Store the label
        id += 1  # Increment id for the next person

# Convert lists to numpy arrays
(images, labels) = [np.array(lst) for lst in [images, labels]]

# Initialize the LBPHFaceRecognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)  # Train the model

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(haar_file)

# Initialize webcam
webcam = cv2.VideoCapture(0)  # Use 0 for default webcam
cnt = 0

while True:
    ret, im = webcam.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces

    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]  # Extract face region
        face_resize = cv2.resize(face, (130, 100))  # Resize face

        prediction = model.predict(face_resize)  # Predict using the trained model

        if prediction[1] < 80:
            # Known face detected, send '1' to unlock the door
            cv2.putText(im, f'{names[prediction[0]]} - {prediction[1]:.0f}', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            print(f'Person: {names[prediction[0]]}, Confidence: {prediction[1]:.0f}')
            if ser and ser.is_open:
                ser.write(b'1')  # Send '1' to serial port
                print("Sent: 1 (Unlock)")
            cnt = 0
        else:
            # Unknown face detected, send '0' to keep locked
            cnt += 1
            cv2.putText(im, 'Unknown', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
            if ser and ser.is_open:
                ser.write(b'0')  # Send '0' to serial port
                print("Sent: 0 (Lock)")
            if cnt > 100:
                print("Unknown Person")
                # Save image with timestamp in unknown_person folder
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                unknown_image_path = os.path.join(unknown_folder, f"unknown_{timestamp}.jpg")
                cv2.imwrite(unknown_image_path, im)
                print(f"Saved unknown person image: {unknown_image_path}")
                cnt = 0

        # Draw rectangle around the face
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Display the output
    cv2.imshow('OpenCV', im)

    # Press 'Esc' to exit
    if cv2.waitKey(10) & 0xFF == 27:
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()
if ser and ser.is_open:
    ser.close()
    print("Serial connection closed")
