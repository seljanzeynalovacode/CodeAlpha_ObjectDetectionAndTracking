# Real-Time Object Detection and Tracking with YOLOv8 🎯

![Python](https://img.shields.io/badge/Python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-white?style=for-the-badge&logo=opencv&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

This repository contains a real-time computer vision project focused on **Object Detection and Tracking**. Built as a robust and optimized pipeline, it utilizes the state-of-the-art YOLOv8 model for precise detection and tracking algorithms to assign consistent IDs to objects across video frames.

## ✨ Features

- **Real-Time Video Input:** Captures high-speed live feed directly from the webcam.
- **Advanced Object Detection:** Leverages pre-trained **YOLOv8s** (Small) model for a perfect balance between accuracy and speed.
- **Continuous Object Tracking:** Automatically assigns and tracks unique IDs for recognized objects over time using YOLO's built-in tracking capabilities.
- **Performance Metrics:** Displays an active **FPS (Frames Per Second)** counter on the screen.
- **Confidence Filtering:** Filters out low-probability detections (set to >50% confidence) to reduce false positives.
- **Automated Output Saving:** Automatically records and exports the processed video feed with bounding boxes and labels to an `.mp4` file.

## 🛠️ Tech Stack & Dependencies

- **Programming Language:** Python
- **Computer Vision Library:** OpenCV (`cv2`)
- **Deep Learning Framework:** Ultralytics (YOLO)
- **Mathematical/Time Operations:** Python built-in `time` module

## 📂 Project Structure

```text
Object_Detection_Tracking/
│
├── data/                      # Directory for external test images or video inputs
├── models/                    # Stores pre-trained YOLO weight files
│   └── yolov8s.pt             # YOLOv8 Small model (22 MB)
├── output/                    # Directory for generated outputs
│   └── tracking_result.mp4    # Saved real-time detection & tracking demo video
│
├── main.py                    # Main execution script of the pipeline
├── requirements.txt           # Python dependencies and versions
├── .gitignore                 # Specifies intentionally untracked files for Git
└── README.md                  # Project documentation
```

## 🚀 Getting Started

Follow these instructions to set up the project locally on your machine.

### 1. Prerequisites
Make sure you have Python (3.8 or higher) installed on your system. 

### 2. Installation
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

*(Optional but recommended)* Create and activate a virtual environment:
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages using pip:
```bash
pip install -r requirements.txt
```

*(Note: The `requirements.txt` should contain `opencv-python` and `ultralytics`)*

## 🎮 Usage

Once the dependencies are installed, you can start the real-time detection and tracking process by running the main script.

```bash
python main.py
```

**While the program is running:**
- The webcam will turn on, and a window labeled `YOLOv8 Object Tracking` will appear.
- You will see bounding boxes, class names, tracking IDs, and the real-time FPS counter.
- **To stop the program:** Click on the video window and press the **`q`** key on your keyboard.

Once stopped, the processed video will be automatically saved in the `output/` directory as `tracking_result.mp4`.

## ⚙️ Configuration & Customization

You can easily tweak the script (`main.py`) for different use cases:
- **Change Video Source:** Change `cv2.VideoCapture(0, cv2.CAP_DSHOW)` to `cv2.VideoCapture('data/your_video.mp4')` to process a pre-recorded video.
- **Change Confidence Threshold:** Adjust `conf=0.5` inside the `model.track()` function to be more strict or lenient regarding what objects are displayed.
- **Filter Specific Classes:** Add `classes=[0]` inside `model.track()` if you only want to detect and track humans (Class 0).
