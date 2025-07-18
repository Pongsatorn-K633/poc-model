from pathlib import Path
import yaml
from ultralytics import YOLO
from datetime import datetime
import shutil


def train_car_frontal_detection():
    # 📁 Set up paths
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parents[3]  # poc-model/

    config_path = project_root / "config" / "car_frontal_detection.yaml"
    default_data_yaml = project_root / "data" / "car_frontal_detection_data" / "data.yaml"
    model_dir = project_root / "weights" / "pretrained_model"
    model_path = model_dir / "yolo11m.pt"

    # 📖 Load YAML config
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Config not found: {config_path}")
        return
    except yaml.YAMLError as e:
        print(f"❌ YAML error in config: {e}")
        return

    model_config = config.get("model", {})
    training_config = config.get("training", {})
    output_config = config.get("output", {})

    print("🤖 Pretrained Model -", model_config)
    print("🤖 Hyperparameters -", training_config)

    # 📁 Resolve dataset YAML
    data_yaml = training_config.get("data_yaml", str(default_data_yaml))
    data_yaml_path = Path(data_yaml) if Path(data_yaml).is_absolute() else project_root / data_yaml

    try:
        with open(data_yaml_path, 'r') as f:
            yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Dataset YAML not found: {data_yaml_path}")
        return
    except yaml.YAMLError as e:
        print(f"❌ YAML error in dataset config: {e}")
        return

    # 📦 Resolve model paths
    model_file = model_config.get("pretrained_model", "yolo11m.pt")
    model_path = Path(model_file) if Path(model_file).is_absolute() else model_dir / model_file

    if not model_path.exists():
        print(f"❌ Pretrained model not found: {model_path}")
        return


    # 🧠 Load main model and train
    print(f"✅ Loading main model: {model_path}")
    print(f"✅ Using dataset config: {data_yaml_path}")
    print(f"✅ Using training config: {config_path}")

    model = YOLO(str(model_path))
    results = model.train(
        data=str(data_yaml_path),
        epochs=training_config["epochs"],
        imgsz=training_config["imgsz"],
        batch=training_config["batch_size"],
        device=training_config["device"],
        lr0=training_config["learning_rate"],
        lrf=training_config["final_lr"],
        weight_decay=training_config["weight_decay"],
        patience=training_config["patience"],
        optimizer=training_config["optimizer"],
        cos_lr=training_config["cosine_lr"],
        amp=training_config["mixed_precision"],
        name=output_config["model_name"],
        project=str(project_root / output_config["save_directory"])
    )

    # 💾 Save best model with timestamp and auto-increment version
    save_dir = project_root / output_config.get("save_directory", "weights/finetuned_model")
    save_dir.mkdir(parents=True, exist_ok=True)

    # Auto-increment version by checking existing files
    model_name = output_config.get('model_name', 'car_frontal_detection')
    existing_files = list(save_dir.glob(f"{model_name}_v*.pt"))
    
    if existing_files:
        # Extract version numbers and find the highest
        versions = []
        for file in existing_files:
            try:
                version_part = file.stem.split('_v')[-1].split('_')[0]  # Get version before timestamp
                versions.append(int(version_part))
            except (ValueError, IndexError):
                continue
        next_version = max(versions) + 1 if versions else 1
    else:
        next_version = 1
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_filename = f"{model_name}_v{next_version}_{timestamp}.pt"

    final_model_path = save_dir / model_filename
    best_model_path = results.save_dir / "weights" / "best.pt"

    if best_model_path.exists():
        shutil.copy2(best_model_path, final_model_path)
        print(f"✅ Best model saved to: {final_model_path}")
    else:
        print("❌ Best model not found after training")

if __name__ == '__main__':
    train_car_frontal_detection()
