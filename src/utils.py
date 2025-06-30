# Put reusable functions here, e.g., for loading videos, saving crops, extracting embeddings, visualizations, etc.

def draw_bbox(frame, bbox, id):
    x1, y1, x2, y2 = [int(v) for v in bbox]
    import cv2
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(frame, f'ID: {id}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
