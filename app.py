import gradio as gr
import time
from src.detect import run_detection
from src.track import run_tracking
from src.match import match_tracks
from src.visualize import visualize_tracks

def full_pipeline(broadcast_video, tacticam_video):
    # Define output paths
    broadcast_dets = "output/broadcast_detections.json"
    tacticam_dets = "output/tacticam_detections.json"
    broadcast_tracks = "output/broadcast_tracks.json"
    tacticam_tracks = "output/tacticam_tracks.json"
    id_matches = "output/id_matches.json"
    broadcast_vis = "output/broadcast_visualized.mp4"
    tacticam_vis = "output/tacticam_visualized.mp4"

    # 1️⃣ Run detection
    run_detection(broadcast_video, "models/yolov11.pt", broadcast_dets)
    run_detection(tacticam_video, "models/yolov11.pt", tacticam_dets)

    # 2️⃣ Run tracking
    run_tracking(broadcast_dets, broadcast_video, broadcast_tracks)
    run_tracking(tacticam_dets, tacticam_video, tacticam_tracks)

    # 3️⃣ Match IDs
    match_tracks(broadcast_tracks, tacticam_tracks, id_matches)

    # 4️⃣ Visualize tracks
    visualize_tracks(broadcast_video, broadcast_tracks, broadcast_vis)
    visualize_tracks(tacticam_video, tacticam_tracks, tacticam_vis)

    # Ensure videos are fully written before returning
    time.sleep(1)

    return broadcast_vis, tacticam_vis, id_matches

# Gradio Interface
iface = gr.Interface(
    fn=full_pipeline,
    inputs=[
        gr.Video(label="Upload Broadcast Video"),
        gr.Video(label="Upload Tacticam Video")
    ],
    outputs=[
        gr.Video(label="Broadcast Visualized"),
        gr.Video(label="Tacticam Visualized"),
        gr.File(label="ID Matches JSON")
    ],
    title="Football Tracking & Re-ID Pipeline",
    description="Upload your broadcast & tacticam videos → run detection, tracking, ID matching, and download results."
)

if __name__== "__main__":
    iface.launch()