import argparse
import cv2
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument("--model", default="models/best.onnx")
parser.add_argument("--conf", type=float, default=0.50)
args = parser.parse_args()
model = YOLO(args.model, task="detect")
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise SystemExit("Webcam unavailable")
while True:
    ok, frame = cam.read()
    if not ok:
        break
    result = model.predict(frame, conf=args.conf, verbose=False)[0]
    cv2.imshow("Smart Currency AI V2 - press Q", result.plot())
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
