#forza_horizon_controler.py
import cv2
import mediapipe as mp
import pyautogui
import threading

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

steering_sensitivity = 0.03
current_tilt = "Center"
lock = threading.Lock()

def handle_keypress():
    global current_tilt
    while True:
        with lock:
            tilt_status = current_tilt
        if tilt_status == "Tilt: Left":
            pyautogui.keyDown('a')
            pyautogui.keyUp('d')
        elif tilt_status == "Tilt: Right":
            pyautogui.keyDown('d')
            pyautogui.keyUp('a')
        else:
            pyautogui.keyUp('a')
            pyautogui.keyUp('d')

keypress_thread = threading.Thread(target=handle_keypress, daemon=True)
keypress_thread.start()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    tilt_status = "Center"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            if index_finger.x < wrist.x - steering_sensitivity:
                tilt_status = "Tilt: Left"
            elif index_finger.x > wrist.x + steering_sensitivity:
                tilt_status = "Tilt: Right"

    with lock:
        current_tilt = tilt_status
    
    cv2.putText(frame, tilt_status, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Steering Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
