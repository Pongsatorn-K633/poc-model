from pathlib import Path
import yaml
from ultralytics import YOLO
from datetime import datetime
from src.poc_model.utils.path_utils import get_project_path

def train_car_frontal_detection():
    script_dir = Path(__file__).parent.resolve()     # scripts/
    root_dir = script_dir.parent                    # project root (poc-model/)
    config_path = get_project_path("config/car_frontal_detection.yaml")
    model_path = get_project_path("root_dir/pretrained_model/yolo11m.pt")
    data_yaml_path = get_project_path("data/car_frontal_detection_data/data.yaml")


    # 2️⃣ Load configuration from YAML file
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"❌ Error: Configuration file not found at {config_path}")
        return
    except yaml.YAMLError as e:
        print(f"❌ YAML parse error: {e}")
        return

    # 3️⃣ Extract configuration sections
    model_config = config.get('model', {})
    training_config = config.get('training', {})
    output_config = config.get('output', {})

    # 4️⃣ Load and validate dataset configuration
    data_yaml_path = training_config.get('data.yaml', 'data.yaml')
    if not Path(data_yaml_path).is_absolute():
        data_yaml_path = model_path / data_yaml_path

    try:
        with open(data_yaml_path, 'r') as file:
            data_config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"❌ Error: Dataset YAML not found at {data_yaml_path}")
        return
    except yaml.YAMLError as e:
        print(f"❌ Dataset YAML parse error: {e}")
        return

    # 5️⃣ Load pretrained model
    model_name = model_config.get('pretrained_model', 'yolo11m.pt')
    if not Path(model_name).is_absolute():
        model_name = model_path / model_name

    if not Path(model_name).exists():
        print(f"❌ Model file not found: {model_name}")
        return

    model = YOLO(str(model_name))

if __name__ == '__main__':
    train_car_frontal_detection()