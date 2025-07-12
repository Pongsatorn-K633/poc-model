# PoC-model Initial Set Up
- Download the packages using conda;&nbsp; conda env create -f environment.yml
- Request the dataset from Tai.
- run cli/checkCUDA.py before training (If you're using an NVIDIA GPU, CUDA is recommended for faster performance)
- Update/Recheck the data.yaml on train/valid/test data path (For the model you're going to train)
<br>
<br>

# Start PoC-model 
- To start Training, get in poc-model folder and type; python main.py --task {car_frontal | brand | bodytype}
    - If you want to train the model again, deleting labels.cache is recommend (both train and valid data)
- train.py is used for model fine-tuning from yolo11m
    - yolov11n.pt is downloaded automatically just for AMP (Automatic Mixed Precision), it still use yolov11m.pt as your weight
    - feel free to experiment with different hyperparameters for optimization. (This setting is use for RTX4070 Laptop VRAM 8 GB)
<br>
<br>

# Devloping...
- insert /test folder
- insert pyproject.toml