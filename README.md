# Setup PoC-model repo

Pre-requisite
1. install python [Must use python version 3.8 - 3.11]
2. pip install uv [We recommend using uv for full dependency resolution, which not let you install incompatible versions. It's also faster]

Setup
1. uv venv .venv  [uv venv .venv --python=python3.10.11 to specific python version]
2. .venv\Scripts\activate
3. Install requirements:
    - If your device contain Nvidia GPU that allow CUDA (and using conda) --> conda env create -f environment.yml
    - If your device contain Nvidia GPU that allow CUDA (and using uv) --> uv pip install -r requirements/requirements-gpu.txt
    - If your device contain AMD GPU that allow ROCm --> uv pip install -r requirements/requirements-gpu.txt but change from cu117 to rocm5.6
    - If your device not contain GPU (Mac) --> uv pip install -r requirements/requirements-cpu.txt








# PoC-model Initial Set Up
- Download the packages using conda;&nbsp; conda env create -f environment.yml
- Request the dataset from Tai.
- Update/Recheck the data.yaml on train/valid/test data path (Base is C:\\Users\\user\\)
- run checkCUDA.py before training (If you're using an NVIDIA GPU, CUDA is recommended for faster performance)
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




💡 Note: The `scripts/` folder must contain `yolo11n.pt` for AMP support.  
This file is automatically copied during `setup.bat`.  
Do not delete unless you override AMP fallback behavior.
