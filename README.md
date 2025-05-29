# Face Recognition Smart Lock System Using Raspberry Pi

## Overview
This project implements a face recognition-based smart lock system using Python, OpenCV, and a Raspberry Pi simulated in Proteus, designed for secure access control in applications like home and office security. The system captures webcam images, detects faces with Haar Cascade, and uses LBPHFaceRecognizer to identify authorized individuals with 80% confidence for known faces. It creates a dataset of 50 grayscale images per user for training and performs real-time recognition, sending '1' (known) or '0' (unknown) via serial communication (COM3, 9600 baud) to control a DC motor and 16x2 LCD. Unknown faces trigger image logging after 100 frames and PIR sensor motion checks. The Proteus simulation integrates a buzzer, switch, and motor, displaying "Valid Person Door Open" or "Unknown Person Door Close." This project demonstrates embedded systems, computer vision, and IoT integration.

## Features
- Real-time face recognition with 80% confidence using LBPHFaceRecognizer.
- Serial communication to control a simulated Raspberry Pi with motor and LCD.
- Dataset creation for training with 50 grayscale face images per user.
- Motion detection for unknown faces via PIR sensor in Proteus simulation.
- Image logging for unrecognized faces after 100 frames for security.

## Technologies Used
- **Hardware (Simulated)**: Raspberry Pi, 16x2 LCD, DC Motor, Buzzer, PIR Sensor, Push Button
- **Software**: Python 3.8+, OpenCV, PySerial, NumPy
- **Simulation**: Proteus 8 Professional
- **Libraries**: OpenCV (Haar Cascade, LBPHFaceRecognizer), PySerial
- **Tools**: Virtual Serial Ports Emulator

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/face-recognition-smart-lock.git
   cd face-recognition-smart-lock


Install Dependencies:

Ensure Python 3.8+ is installed.
Install required Python packages:pip install opencv-python numpy pyserial


Download and install Tesseract OCR if needed for additional processing.
Install Proteus 8 Professional for simulation.
Install Virtual Serial Ports Emulator to create virtual COM ports.


Configure Files:

Place haarcascade_frontalface_default.xml in the project root (available from OpenCV’s GitHub).
Ensure a webcam is connected or configure a virtual camera for testing.
Update serial_port in face_recognition.py if your COM port differs (e.g., COM3).


Set Up Proteus Simulation:

Open the Proteus project file (smart_lock_simulation.pdsprj) in Proteus 8.
Configure the Raspberry Pi simulation with the provided raspberry_pi_code.py.
Connect virtual COM ports (e.g., COM3) between the Python script and Proteus.



Usage

Create Face Dataset:

Run face_data_creation.py:python face_data_creation.py


Enter a name when prompted, and the script captures 50 grayscale face images, saving them in the datasets folder.


Run Face Recognition:

Start the Proteus simulation to initialize the Raspberry Pi and hardware components.
Run face_recognition.py:python face_recognition.py


The system processes webcam video, detects faces, and identifies them against the trained dataset.
For known faces (confidence < 80), it sends '1' to Proteus, displaying "Valid Person Door Open" on the LCD and activating the motor.
For unknown faces, it sends '0', displays "Unknown Person Door Close," logs the image in unknown_person, and checks PIR sensor for motion.


Interact with Hardware:

Press the virtual switch in Proteus to trigger face recognition.
The buzzer sounds, and the LCD updates based on the recognition result.



Project Structure
face-recognition-smart-lock/
│
├── datasets/                   # Stores face images for training
├── unknown_person/             # Stores images of unrecognized faces
├── face_data_creation.py       # Script to capture and save face datasets
├── face_recognition.py         # Script for real-time face recognition
├── raspberry_pi_code.py        # Raspberry Pi code for Proteus simulation
├── smart_lock_simulation.pdsprj # Proteus simulation file
├── haarcascade_frontalface_default.xml # Haar Cascade file for face detection
├── README.md                   # Project documentation
└── LICENSE                     # License file

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request with a detailed description of your changes.

Please ensure code follows PEP 8 style guidelines and includes comments for clarity.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Anna University Regional Campus Coimbatore for project guidance.
OpenCV and Proteus communities for open-source tools and resources.



