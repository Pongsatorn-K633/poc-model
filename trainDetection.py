from ultralytics import YOLO

def train_yolo():
    model = YOLO("yolo11m.pt")  # Load pre-trained YOLO model

    model.train(
        data="C:/Users/user/Documents/VScode/DemoModel/data_detect.yaml",  # Dataset path
        epochs=50,               # Increased epochs due to smaller dataset
        batch=32,                # Keep batch size moderate for stability
        device="cuda",           # Use GPU
        lr0=0.0008,              # Lower learning rate for fine-tuning
        lrf=0.0001,              # Final learning rate with decay
        cos_lr=True,             # Smooth learning rate decay
        weight_decay=0.0007,     # Slightly increased to prevent overfitting
        patience=5,              # Stops training early if no improvement
        optimizer="AdamW"
    )

    # Save the trained model
    model.save("car-frontal_detection.pt")

if __name__ == '__main__':
    train_yolo()
