import cv2
import numpy as np
import time

# Load YOLO
net = cv2.dnn.readNet("opencv/Yolo/yolov3.weights", "opencv/Yolo/yolov3.cfg")

# Get the names of all layers
layer_names = net.getLayerNames()

# Get the output layers (those are the layers responsible for the detection)
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Initialize the video capture (camera)
cap = cv2.VideoCapture(0)  # 0 is the default camera

# Function to get FPS
def calculate_fps(start_time, frames):
    return frames / (time.time() - start_time)

frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1

    # Get the blob from the image
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Process detections
    class_ids = []
    confidences = []
    boxes = []
    height, width, channels = frame.shape

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w // 2
                y = center_y - h // 2

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-maximum suppression to avoid multiple boxes for the same object
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw boxes and labels
    with open("opencv/Yolo/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Display FPS
    fps = calculate_fps(start_time, frame_count)
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))

            # Draw a rectangle with a background for the label
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Object Detection", frame)

    # Break the loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
