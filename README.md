# FORZA Gesture Control 🚗✋

FORZA Gesture Control is an innovative Python-based solution that utilizes **computer vision** and **hand gesture recognition** to control vehicles in the popular racing game, Forza Horizon. Experience a whole new level of gaming by steering your virtual car using just your hand gestures!

---

## 🚀 Features
- **Real-time Gesture Detection:** Detects and processes hand gestures using a webcam.
- **Tilt Detection:** Steer left, right, or center using wrist and index finger gestures.
- **Threaded Input Handling:** Ensures smooth and uninterrupted gameplay.
- **Custom Sensitivity Control:** Easily configurable steering sensitivity.
- **Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SURAJVERMA-BIT/FORZA_GESTURE_CONTROL.git
   
Navigate to the folder:
cd FORZA_GESTURE_CONTROL

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   
4. Run the script:

   ```bash
   python forza_horizon_controller.py

## ✋ How It Works
1. Hand Tracking: Uses Mediapipe Hands for detecting hand landmarks.
2. Steering Detection: Tracks the wrist and index finger to determine steering direction:
Tilt Left: Index finger moves left of the wrist.
Tilt Right: Index finger moves right of the wrist.
Center: Default position when no tilt is detected.
3. Keyboard Simulation: Simulates key presses (A for left, D for right) to steer the vehicle.

## 🖥️ System Requirements
Python 3.8 or later
OpenCV 4.x
Mediapipe
PyAutoGUI

## 📂 Project Structure
FORZA_GESTURE_CONTROL/
│
├── forza_horizon_controller.py  # Main script for gesture control
├── LICENSE                      # License for the project
├── CONTRIBUTING.md              # Guidelines for contributing
├── guide.md                     # Detailed guide for installation and setup
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies

## 🤝 Contributing
We welcome contributions from the community! Check out the CONTRIBUTING.md file for guidelines on how to get started.


## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact
For any queries or suggestions, feel free to reach out at sv9052788@gmail.com.

##❤️ Acknowledgments
Special thanks to:
Mediapipe: For making hand gesture detection possible.
The open-source community for their valuable contributions.

## Enjoy gaming with next-level gesture control! 🚀✨
