### **GUIDE.md**

This guide explains how to set up and use the Forza Horizon Gesture Control system.

## Prerequisites:
- Python 3.7 or higher
- Webcam
- Dependencies installed (see below)

## Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/SURAJVERMA-BIT/FORZA_GESTURE_CONTROL.git

2. Navigate to the project directory:
   '''bash
   cd FORZA_GESTURE_CONTROL
   '''

3. Install the required dependencies:
   '''bash
   pip install -r requirements.txt
   '''


## Running the Program:
1. Connect your webcam.
2. Run the script:
    '''bash
    python src/forza_horizon_controller.py
    '''
3. Use your hand gestures to control the car:
Tilt Left: Move your index finger to the left of your wrist.
Tilt Right: Move your index finger to the right of your wrist.

## Troubleshooting:
1) Camera not detected: Ensure your webcam is properly connected.
2) Gestures not recognized: Adjust the steering_sensitivity variable in the script.
