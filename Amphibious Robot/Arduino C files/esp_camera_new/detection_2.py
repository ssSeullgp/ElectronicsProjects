import serial
import cv2

# Serial port connection import
ser = serial.Serial('COM3', 115200, timeout=1)

# Capture video from ESP32CAM 
cap = cv2.VideoCapture(0)  # Replace 0 with IP address with wifi

while True:
  # Reads image from ESP32CAM
  ret, frame = cap.read()
  if not ret:
    print("Error reading frame")
    break

  # Reads bounding box data from serial port 
  data = ser.readline().decode('utf-8').strip()
  if not data:
    continue

  # Parse bounding box data (modify based on actual format)
  boxes = []
  for box_str in data.split(','):
    if not box_str:
      continue
    x, y, width, height = map(int, box_str.split(':'))
    boxes.append((x, y, width, height))

  # Draw bounding boxes on the frame
  for x, y, width, height in boxes:
    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

  # Displays the frame with bounding boxes
  cv2.imshow('ESP32CAM Live Stream', frame)

  # Exit on 'q' key press
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
ser.close()