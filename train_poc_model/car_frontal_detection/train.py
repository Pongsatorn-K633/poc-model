def train_yolo():
    import os
    from pathlib import Path
    from ultralytics import YOLO
    
     # 1️⃣ switch CWD to the folder containing both .pt files
    model_dir = Path(__file__).parent.resolve()
    os.chdir(model_dir)
        
    model = YOLO("yolo11m.pt")  # Load pre-trained YOLO model 
    
    model.train(
        data="C:/Users/user/Documents/VScode/poc-model/src/car_frontal_detection/data_detect.yaml",  # Dataset path
        epochs=50,               # Increased epochs due to smaller dataset
        batch=4,                 # Keep batch size moderate for stability
        device="cuda",           # Use GPU
        lr0=0.0008,              # Lower learning rate for fine-tuning
        lrf=0.0001,              # Final learning rate with decay
        weight_decay=0.0007,     # Slightly increased to prevent overfitting
        patience=5,              # Stops training early if no improvement
        optimizer="AdamW",       # modern and stable optimizer
        cos_lr=True,             # Smooth learning rate decay
        amp=True
    )

    # Save the trained model
    model.save("car_frontal_detection.pt")

if __name__ == '__main__':
    train_yolo()
