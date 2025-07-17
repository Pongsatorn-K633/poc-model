import logging
import sys
from pathlib import Path
from datetime import datetime

def setup_logger(model_type: str) -> logging.Logger:
    """Setup logger for a specific model type."""

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Create logger
    logger = logging.getLogger(f"poc_model.{model_type}")
    logger.setLevel(logging.INFO)

    # Clear existing handlers
    logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_handler = logging.FileHandler(
        logs_dir / f"{model_type}_{timestamp}.log"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger