# src/match.py

import json

def match_tracks(broadcast_tracks_path, tacticam_tracks_path, output_path):
    with open(broadcast_tracks_path) as f:
        broadcast_tracks = json.load(f)

    with open(tacticam_tracks_path) as f:
        tacticam_tracks = json.load(f)

    matches = []
    for i in range(min(len(broadcast_tracks), len(tacticam_tracks))):
        matches.append({
            "broadcast_id": broadcast_tracks[i]["track_id"],  # ✅ FIXED KEY
            "tacticam_id": tacticam_tracks[i]["track_id"],    # ✅ FIXED KEY
            "similarity": 0.95  # dummy similarity
        })

    with open(output_path, "w") as f:
        json.dump(matches, f)

    print(f"ID matches saved to {output_path}")
