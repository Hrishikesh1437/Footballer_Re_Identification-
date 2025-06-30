# ⚽ Multi-Camera Football Player Tracking Pipeline

**Author:** Hrishikesh Anand Tirupati  
**Submission Date:** 30-06-2025  

---

## 📌 Project Overview

This project demonstrates an end-to-end pipeline for **multi-camera football player detection, tracking, Re-ID matching**, and final **visualization**.  
It uses **YOLOv8**, **SORT tracker**, and a simple **Re-ID matcher** to track players across different camera feeds (Broadcast and Tacticam) and visualize the results with ID matching.

---

## 🗂️ Repository Structure

```plaintext
📁 Footbal_Task_1/
├── src/
│   ├── detect.py       # Player detection with YOLOv8
│   ├── track.py        # Player tracking with SORT
│   ├── match.py        # Simple Re-ID matching
│   ├── visualize.py    # Visualization of tracking & Re-ID
│   ├── sort.py         # SORT tracker implementation
│   ├── reid.py         # Dummy Re-ID model
├── videos/
│   ├── broadcast.mp4   # Broadcast camera input video
│   ├── tacticam.mp4    # Tacticam camera input video
├── output/
│   ├── broadcast_detections.json
│   ├── tacticam_detections.json
│   ├── broadcast_tracks.json
│   ├── tacticam_tracks.json
│   ├── id_matches.json
│   ├── broadcast_visualized.mp4
│   ├── tacticam_visualized.mp4
├── app.py              # Gradio/Streamlit app for running the pipeline
├── README.md           # Project documentation
```
⚙️ Tech Stack
```plaintext
Python 3.12

YOLOv8 (Ultralytics)

OpenCV

NumPy

SORT (Simple Online and Realtime Tracking)

Re-ID (Basic dummy matching for demonstration)

Gradio / Streamlit for UI
```

🚀 How to Run
1️⃣ Create & activate a virtual environment
```plaintext
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
2️⃣ Install dependencies
```plaintext

pip install -r requirements.txt
```
3️⃣ Run the full pipeline
```plaintext

# If using Gradio
python app.py

# Or if using Streamlit
streamlit run app.py
```
4️⃣ Upload your input videos
```plaintext

broadcast.mp4 (Broadcast camera)

tacticam.mp4 (Tacticam camera)
```
5️⃣ Pipeline steps:
```plaintext
✅ Detect players ➜
✅ Track with SORT ➜
✅ Re-ID matching ➜
✅ Visualize & save output videos ➜
✅ Download results
```
🧩 Key Features
```plaintext
YOLOv8 for accurate player detection

SORT for fast tracking

Dummy Re-ID for linking IDs across views

Clean output videos with bounding boxes & IDs

Interactive web UI for easy testing & uploading new videos
```

📂 Output
```plaintext
All intermediate and final outputs are saved under the /output folder:

*_detections.json — Raw detections

*_tracks.json — SORT tracking results

id_matches.json — Re-ID matching results

*_visualized.mp4 — Final videos with bounding boxes & IDs
```
✏️ Author

Hrishikesh Anand Tirupati

📅 Date: 30-06-2025

