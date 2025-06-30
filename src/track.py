# src/track.py

import json
import numpy as np
from src.sort import Sort
import cv2

def run_tracking(detections_path, video_path, output_path):
    with open(detections_path) as f:
        detections = json.load(f)

    tracker = Sort()
    cap = cv2.VideoCapture(video_path)

    frame_id = 0
    tracks_output = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_dets = [
            d["bbox"] + [d["confidence"]]
            for d in detections if d["frame_id"] == frame_id
        ]

        dets_np = np.array(frame_dets) if frame_dets else np.empty((0, 5))

        tracked_objects = tracker.update(dets_np)

        for obj in tracked_objects:
            x1, y1, x2, y2, track_id = obj
            tracks_output.append({
                "frame_id": frame_id,
                "bbox": [float(x1), float(y1), float(x2), float(y2)],
                "track_id": int(track_id)  # ✅ FIXED KEY: always use track_id
            })

        frame_id += 1

    cap.release()

    with open(output_path, "w") as f:
        json.dump(tracks_output, f)

    print(f"Tracking complete! Saved to {output_path}")
