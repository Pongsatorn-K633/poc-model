def train_yolo():
    import os
    from pathlib import Path
    from ultralytics import YOLO
    
     # 1️⃣ switch CWD to the folder containing both .pt files
    model_dir = Path(__file__).parent.resolve()
    os.chdir(model_dir)
        
    model = YOLO("yolo11m.pt")  # Load pre-trained YOLO model 
    
    model.train(
        data="data.yaml",  # Dataset path
        epochs=50,               # Increased epochs due to smaller dataset
        batch=8,                 # Keep batch size moderate for stability
        device="cuda",           # Use GPU
        lr0=0.0008,              # Lower learning rate for fine-tuning
        lrf=0.0001,              # Final learning rate with decay
        weight_decay=0.0007,     # Slightly increased to prevent overfitting
        patience=10,              # Stops training early if no improvement
        optimizer="AdamW",       # modern and stable optimizer
        cos_lr=True,             # Smooth learning rate decay
        amp=True                 # mixed precision training - reduced GPU memory usage
    )

    # Save the trained model **CHANGE THE NAME BEFORE TRAINING AGAIN
    model.save("model/car_frontal_detection_xxx.pt")

if __name__ == '__main__':
    train_yolo()
