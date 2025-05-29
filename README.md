# Face Recognition Smart Lock System Using Raspberry Pi

This project implements a **face recognition-based smart lock system** using Python, OpenCV, and a **simulated Raspberry Pi in Proteus**, designed for secure access control in applications like homes and offices.

---

## 🔐 Overview

The system captures webcam images, detects faces using Haar Cascade, and identifies authorized users with the **LBPHFaceRecognizer** at **≥80% confidence**. It then sends control signals via **serial communication** to a Proteus simulation, which includes a DC motor, 16x2 LCD, buzzer, PIR sensor, and push button. 

Unknown faces are logged after 100 failed recognition attempts, combined with motion detection using the PIR sensor.

---

## 🎯 Features

- ✅ Real-time face recognition using **LBPH algorithm** (≥80% confidence).
- 🔄 Serial communication between Python and Proteus using COM ports.
- 📸 Dataset creation with **50 grayscale images per user**.
- 🕵️ PIR sensor motion detection for unknown faces.
- 🖼️ Logging of unrecognized faces after 100 frames.
- 📟 16x2 LCD and DC Motor integration via Proteus simulation.

---

## 🛠️ Technologies Used

### Hardware (Simulated):
- Raspberry Pi
- 16x2 LCD
- DC Motor
- Buzzer
- PIR Sensor
- Push Button

### Software & Libraries:
- Python 3.8+
- OpenCV (Haar Cascade, LBPH)
- PySerial
- NumPy
- Proteus 8 Professional
- Virtual Serial Ports Emulator

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/face-recognition-smart-lock.git
cd face-recognition-smart-lock
