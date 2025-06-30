# # src/visualize.py

# import cv2
# import json

# def visualize_tracks(video_path, tracks_path, output_path, label="TrackID"):
#     with open(tracks_path) as f:
#         tracks = json.load(f)

#     cap = cv2.VideoCapture(video_path)

#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

#     frame_id = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_tracks = [t for t in tracks if t["frame_id"] == frame_id]

#         for track in frame_tracks:
#             x1, y1, x2, y2 = map(int, track["bbox"])
#             tid = track["track_id"]  # ✅ now guaranteed to exist

#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f"{label}: {tid}", (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         out.write(frame)
#         frame_id += 1

#     cap.release()
#     out.release()

#     print(f"Visualization saved to {output_path}")
import cv2
import json

def visualize_tracks(video_path, tracks_path, output_path, label="TrackID"):
    """
    Draws tracked bounding boxes on each frame of the input video
    and saves the result as an MP4 file with a browser-compatible codec.

    Args:
        video_path (str): Path to input video file.
        tracks_path (str): Path to tracking results JSON file.
        output_path (str): Path to save the output visualized video.
        label (str): Optional label prefix for track IDs.
    """
    # Load tracking results
    with open(tracks_path) as f:
        tracks = json.load(f)

    # Open input video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # ✅ Use 'avc1' for H.264 – browser/Gradio compatible
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Get tracks for the current frame
        frame_tracks = [t for t in tracks if t["frame_id"] == frame_id]

        for track in frame_tracks:
            x1, y1, x2, y2 = map(int, track["bbox"])
            tid = track.get("track_id", "N/A")

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw track ID label
            cv2.putText(frame, f"{label}: {tid}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        out.write(frame)
        frame_id += 1

    cap.release()
    out.release()
    print(f"[✔] Visualization saved to {output_path}")