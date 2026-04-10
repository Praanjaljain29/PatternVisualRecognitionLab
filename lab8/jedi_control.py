import cv2
import pyautogui
from ultralytics import YOLO
import time
import os

# 1. Load your model
model = YOLO('best.pt') 

cap = cv2.VideoCapture(0)
cooldown = 0 

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    results = model(frame, conf=0.8, verbose=False)
    annotated_frame = results[0].plot()

    msg = "SYSTEM: STANDBY"
    color = (200, 200, 200)

    for box in results[0].boxes:
        label = model.names[int(box.cls[0])].lower()
        
        if time.time() > cooldown:
            # --- WINDOW MANAGEMENT ---
            if "fist" in label:
                msg = "ACTION: PRIVACY SHIELD (WIN+D)"
                pyautogui.hotkey('win', 'd') 
                cooldown = time.time() + 2.0
            
            elif "peace" in label:
                msg = "ACTION: CAPTURING SCREENSHOT"
                pyautogui.hotkey('win', 'prtscr')
                color = (0, 255, 255)
                cooldown = time.time() + 2.0

            # --- VOLUME & MEDIA ---
            elif "like" in label and "dislike" not in label:
                msg = "ACTION: VOLUME UP"
                pyautogui.press('volumeup')
                cooldown = time.time() + 0.2
            
            elif "dislike" in label:
                msg = "ACTION: VOLUME DOWN"
                pyautogui.press('volumedown')
                cooldown = time.time() + 0.2

            elif "mute" in label:
                msg = "ACTION: TOGGLE MUTE"
                pyautogui.press('volumemute')
                cooldown = time.time() + 1.0

            elif "stop" in label:
                msg = "ACTION: MEDIA PLAY/PAUSE"
                pyautogui.press('playpause')
                cooldown = time.time() + 1.5

            # --- APP LAUNCHERS (THE "UNIQUE" PART) ---
            elif "ok" in label:
                msg = "ACTION: OPENING CHROME"
                os.system("start chrome") # For Windows
                color = (0, 255, 0)
                cooldown = time.time() + 3.0

            elif "call" in label:
                msg = "ACTION: OPENING NOTEPAD"
                os.system("start notepad")
                color = (255, 165, 0)
                cooldown = time.time() + 3.0

            elif "three" in label:
                msg = "ACTION: OPENING CALCULATOR"
                os.system("start calc")
                cooldown = time.time() + 3.0

            # --- BROWSER NAVIGATION ---
            elif "rock" in label:
                msg = "ACTION: REFRESH PAGE (F5)"
                pyautogui.press('f5')
                cooldown = time.time() + 2.0

    # Draw the HUD
    cv2.rectangle(annotated_frame, (0, 420), (640, 480), (0, 0, 0), -1)
    cv2.putText(annotated_frame, msg, (20, 460), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Jedi Desktop Controller", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()