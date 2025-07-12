# PoC-model Initial Set Up
- Download the packages using conda;&nbsp; conda env create -f environment.yml
- Request the dataset from Tai.
- run checkCUDA.py before training (If you're using an NVIDIA GPU, CUDA is recommended for faster performance)
<br>
<br>

# Start PoC-model 
- trainDetection.py is used for model fine-tuning from yolo11m
    - change *data path* and *model path* to match your local path (yolov11n.pt is downloaded automatically just for AMP (Automatic Mixed Precision), it still use yolov11m.pt as your weight)
    - feel free to experiment with different hyperparameters for optimization. (This setting is use for RTX4070 Laptop VRAM 8 GB)
- If you want to train the model again, deleting labels.cache is recommend (both train and valid data)

# Devloping...
- insert /test folder
- insert pyproject.toml