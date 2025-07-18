# main.py
import argparse
from train_poc_model.car_frontal_detection.train import train_yolo as train_car_front_detection
# from train_poc_model.brand_classification.train import train_yolo as train_brand
# from train_poc_model.bodytype_classification.train import train_yolo as train_body

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
        train_car_front_detection()
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