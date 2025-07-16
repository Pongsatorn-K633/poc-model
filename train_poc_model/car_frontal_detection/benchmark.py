import torch
import time
from ultralytics import YOLO
import cv2
import glob

# Load model
model = YOLO("runs/detect/train11/weights/best.pt")

# Load dummy images (or actual test images)
image_paths = glob.glob("your_test_images_folder/*.jpg")
images = [cv2.imread(p) for p in image_paths[:16]]  # load 16 images

# Warm-up
for _ in range(5):
    model(images[0])

# Timing
start = time.time()
for img in images:
    model(img)
end = time.time()

total_time = end - start
fps = len(images) / total_time

print(f"Processed {len(images)} images in {total_time:.2f}s -> FPS: {fps:.2f}")
