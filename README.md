````md
# 🖐️ TouchLess AI — Adaptive Hand Gesture Utility Control

A real-time **computer vision based touchless utility control system** developed using **OpenCV, MediaPipe, and Python**.

The project enables users to interact with system utilities such as **volume control, brightness adjustment, screenshot capture, and bi-directional scrolling** through webcam-based hand gesture recognition without requiring physical input devices.

---

# 🚀 Features

- 🔊 Adaptive volume control using thumb-index gesture
- 💡 Dynamic brightness adjustment using thumb-pinky gesture
- 📜 Motion-based bi-directional scrolling
- 📸 Screenshot capture using thumbs-up gesture
- 🎥 Real-time hand landmark tracking using MediaPipe
- 🎯 Personalized gesture calibration
- ✨ False-trigger prevention and gesture separation
- ⚡ Low-latency real-time interaction

---

# 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- screen-brightness-control
- NumPy

---

# 📂 Project Structure

```text
TouchLess-AI/
│
├── core/
│   ├── calibration.py
│   ├── gesture_logic.py
│   ├── hand_tracker.py
│   ├── mouse_control.py
│   ├── system_control.py
│   ├── smoothing.py
│   └── config.py
│
├── screenshots/
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
git clone <your-repository-link>
cd TouchLess-AI
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
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