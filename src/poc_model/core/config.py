import yaml
from pathlib import Path
from typing import Dict, Any, Optional

def get_device():
    """Automatically detect the best available device."""
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return "mps"  # Apple Silicon Macs
        else:
            return "cpu"
    except ImportError:
        return "cpu"

def find_config_dir() -> Path:
    """Find the config directory by searching up the directory tree."""
    current = Path(__file__).parent
    while current != current.parent:  # Stop at root directory
        config_dir = current / "config"
        if config_dir.exists() and config_dir.is_dir():
            return config_dir
        current = current.parent
    
    # If not found, try relative to current working directory
    config_dir = Path.cwd() / "config"
    if config_dir.exists():
        return config_dir
    
    raise FileNotFoundError("Could not find config directory")

def load_config(model_type: str, config_path: Optional[str] = None, device: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration for a specific model type."""

    # Map model types to config files
    model_configs = {
        "car_frontal": "car_frontal_detection.yaml",
        "brand": "brand_classification.yaml",
        "bodytype": "bodytype_classification.yaml"
    }

    if model_type not in model_configs:
        raise ValueError(f"Unknown model type: {model_type}")

    # Find config directory
    config_dir = find_config_dir()

    # Load base config
    base_config_path = config_dir / "base.yaml"
    with open(base_config_path) as f:
        base_config = yaml.safe_load(f)

    # Load model-specific config
    if config_path:
        model_config_path = Path(config_path)
    else:
        model_config_path = config_dir / model_configs[model_type]

    with open(model_config_path) as f:
        model_config = yaml.safe_load(f)

    # Merge configurations
    merged_config = {**base_config, **model_config}

    # Set device - use provided device, or auto-detect
    merged_config['device'] = device if device else get_device()
    
    # Apply device-specific optimizations
    if merged_config['device'] == 'cuda':
        # Enable CUDA-specific optimizations
        merged_config.setdefault('training', {})['mixed_precision'] = merged_config.get('training', {}).get('mixed_precision', True)
        merged_config.setdefault('training', {})['deterministic'] = False  # Better performance on CUDA
    elif merged_config['device'] == 'cpu':
        # CPU optimizations
        merged_config.setdefault('training', {})['mixed_precision'] = False  # Not supported on CPU
        merged_config.setdefault('training', {})['deterministic'] = True

    return merged_config