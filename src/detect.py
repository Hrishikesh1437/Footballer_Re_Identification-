# src/detect.py

import cv2
import json
from ultralytics import YOLO

def run_detection(video_path, model_path, output_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    detections = []
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, verbose=False)

        for r in results:
            for box in r.boxes:
                xyxy = box.xyxy[0].tolist()
                cls = int(box.cls[0].item())
                conf = float(box.conf[0].item())

                detections.append({
                    "frame_id": frame_id,
                    "bbox": xyxy,
                    "class_id": cls,
                    "confidence": conf
                })

        frame_id += 1

    cap.release()

    with open(output_path, "w") as f:
        json.dump(detections, f)

    print(f"Detections saved to: {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    run_detection(args.video, args.model, args.output)
