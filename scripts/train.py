import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pathlib import Path

from src.poc_model.core.config import load_config
from src.poc_model.core.logger import setup_logger
from src.poc_model.utils.path_utils import get_project_path
from src.poc_model.models.car_frontal_detection.car_frontal_train import train_car_frontal_detection
from src.poc_model.models.brand_classification.brand_train import train_brand_classification
from src.poc_model.models.bodytype_classification.bodytype_train import train_bodytype_classification

def main():
    parser = argparse.ArgumentParser(description="Train AI models")
    parser.add_argument(
        "--model",
        choices=["car_frontal", "brand", "bodytype"],
        required=True,
        help="Model type to train"
    )
    parser.add_argument("--config", help="Override config file path")
    parser.add_argument("--epochs", type=int, help="Override number of epochs")
    parser.add_argument("--batch-size", type=int, help="Override batch size")

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.model, args.config)

    # Override config with command line args
    if args.epochs:
        config['training']['epochs'] = args.epochs
    if args.batch_size:
        config['training']['batch_size'] = args.batch_size

    # Setup logging
    logger = setup_logger(args.model)

    # Train model
    logger.info(f"Starting training for {args.model}")

    if args.model == "car_frontal":
        train_car_frontal_detection(config)
    elif args.model == "brand":
        # train_brand_classification(config)
        print("Devloping...")
    elif args.model == "bodytype":
        # train_bodytype_classification(config)
        print("Devloping...")

    logger.info("Training completed successfully")

if __name__ == "__main__":
    main()
    
# run; python train.py --model car_frontal