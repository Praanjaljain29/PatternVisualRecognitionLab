# Real-Time Hand Gesture Recognition and OS Control using YOLOv8

## Overview
This mini project builds a real-time hand gesture recognition system using YOLOv8 and maps detected gestures to operating-system actions (volume control, screenshots, app launch, media control, etc.).

The system uses webcam input, performs gesture detection frame-by-frame, and triggers desktop commands when confidence is high enough.

## Objectives
- Train a YOLOv8 gesture detector for multi-class hand gestures.
- Evaluate detection quality using precision, recall, mAP, F1, and confusion matrix.
- Build a practical Human-Computer Interaction (HCI) demo that controls OS actions from gestures.

## Project Structure
- `hand-gesture-os-controller-yolov8.ipynb` - training and experimentation notebook.
- `jedi_control.py` - real-time webcam inference + OS action mapping script.
- `best.pt` - trained YOLOv8 model weights used for inference.
- `gesture_controller_final/` - training outputs (plots, confusion matrices, sample predictions, weights, and run metadata).

## Dataset and Classes
The detector is trained on 18 gesture classes:

1. call
2. dislike
3. fist
4. four
5. like
6. mute
7. ok
8. one
9. palm
10. peace
11. peace_inverted
12. rock
13. stop
14. stop_inverted
15. three
16. three2
17. two_up
18. two_up_inverted

## Training Configuration (YOLOv8)
Key settings used in training:
- Model: `yolov8n.pt` (pretrained)
- Epochs: `50`
- Image size: `640`
- Batch size: `16`
- Optimizer: `auto`
- Device: GPU (`device: 0`)

Source: `gesture_controller_final/args.yaml`

## Final Performance (from training logs)
At epoch 50:
- Precision: `0.9537`
- Recall: `0.9110`
- mAP@0.5: `0.9607`
- mAP@0.5:0.95: `0.8019`

Source: `gesture_controller_final/results.csv`

## Real-Time Control Mapping
Implemented in `jedi_control.py`.

- `fist` -> Show desktop (`Win + D`)
- `peace` -> Screenshot (`Win + PrtSc`)
- `like` -> Volume up
- `dislike` -> Volume down
- `mute` -> Toggle mute
- `stop` -> Play/Pause media
- `ok` -> Open Chrome
- `call` -> Open Notepad
- `three` -> Open Calculator
- `rock` -> Refresh (`F5`)

A cooldown mechanism is used to prevent repeated keypress triggering in consecutive frames.

## How to Run
### 1) Install dependencies
```bash
pip install ultralytics opencv-python pyautogui
```

### 2) Run the controller
```bash
python jedi_control.py
```

### 3) Controls
- Press `q` to quit the webcam window.

## Results Artifacts
The folder `gesture_controller_final/` includes:
- Learning curves (`results.png`, `results.csv`)
- Precision/Recall/F1-confidence curves
- Confusion matrices
- Validation prediction samples
- Trained weights (`weights/best.pt`, `weights/last.pt`)

## Limitations
- Performance may drop in low light, heavy background clutter, or motion blur.
- Similar gestures can still confuse the model in edge cases.
- OS key mappings are currently Windows-oriented.

## Future Improvements
- Add temporal smoothing / gesture confirmation over multiple frames.
- Add a GUI for custom gesture-to-action mapping.
- Export to ONNX/TensorRT for lower-latency inference.
- Add support for Linux/macOS shortcut mappings.

## Author
Praanjal Jain
