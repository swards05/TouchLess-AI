# 🖐️ TouchLess AI — Gesture-Based Laptop Control Suite

A real-time **computer vision based touchless laptop controller** built using **OpenCV, MediaPipe, and Python**.

This project enables users to control **mouse movement, click, scrolling, volume, brightness, screenshots, calculator launch, and window closing** using simple hand gestures.

---

## 🚀 Features
- 🔊 Dynamic volume control using thumb-index pinch
- 💡 Dynamic brightness control using thumb-middle pinch
- 🖱️ Virtual mouse movement
- 👆 Pinch-based mouse click
- ✌️ Gesture-based scrolling
- 📸 Screenshot capture
- 👍 Calculator launch
- ✊ Close active window
- 🎥 Real-time hand tracking using MediaPipe
- ✨ Smooth cursor movement

---

## 🛠️ Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Screen Brightness Control

---

## 📂 Project Structure
TouchLess-AI/
│
├── main.py
├── requirements.txt
├── README.md
│
├── core/
│ ├── hand_tracker.py
│ ├── gesture_logic.py
│ ├── mouse_control.py
│ ├── system_control.py
│ ├── smoothing.py
│ └── config.py
│
└── screenshots/

---

## ▶️ Installation
```bash
git clone <your-repo-link>
cd TouchLess-AI
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

✋ Gesture Guide

Gesture	Action:

☝️ Index finger	Mouse move
🤏 Thumb + Index pinch	Click
✌️ Index + Middle	Scroll
🤟 3 fingers	Screenshot
👍 Thumb only	Open Calculator
👍 + ☝️	Volume
👍 + 🖕	Brightness
✊ Fist	Close active window