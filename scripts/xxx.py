import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pathlib import Path

from src.poc_model.core.config import load_config
from src.poc_model.core.logger import setup_logger
from src.poc_model.models.car_frontal_detection.car_frontal_train import train_car_frontal_detection
from src.poc_model.models.brand_classification.brand_train import train_brand_classification
from src.poc_model.models.bodytype_classification.bodytype_train import train_bodytype_classification

def main():
    parser = argparse.ArgumentParser(description="Train a specific detection or classification model.")
    parser.add_argument(
        "--task",
        type=str,
        choices=["car_frontal", "brand", "bodytype"],
        required=True,
        help="Choose which task to train"
    )
    args = parser.parse_args()

    if args.task == "car_frontal":
        train_car_frontal_detection()
    elif args.task == "brand":
        # train_brand()
        print("in development")
    elif args.task == "bodytype":
        # train_body()
        print("in development")
    else:
        raise ValueError("Unknown task")

if __name__ == "__main__":
    main()

# run; python main.py --task car_frontal