from pathlib import Path
import sys
# print(type(__file__))
# print(type(Path(__file__)))
# print(type(Path(__file__).parent))
print(sys.path.insert(0, str(Path(__file__).parent.parent)))
print(Path(__file__))
print(Path.cwd())
# print(Path(__file__).parent)

# __file__: the path of the current Python script (as a string).
# Path(__file__): converts that string into a Path object.
# .parent: gets the directory containing the file.

# If not found, try relative to current working directory
config_dir = Path.cwd() / "config"
print("cwd \n", config_dir)

def find_config_dir() -> Path:
    """Find the config directory by searching up the directory tree."""
    print("Start!")
    current = Path(__file__).parent
    while current != current.parent:  # Stop at root directory
        print(current)
        config_dir = current / "config"
        print("config: ", config_dir)
        if config_dir.exists() and config_dir.is_dir():
            return config_dir
        current = current.parent
        print("dir: ", current)
    

        
if __name__ == "__main__":
    find_config_dir()