import platform
import subprocess
import sys

def has_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def is_macos():
    return platform.system() == "Darwin"

def check_amd_on_macos():
    try:
        result = subprocess.run(["system_profiler", "SPDisplaysDataType"], stdout=subprocess.PIPE, text=True)
        return "AMD" in result.stdout or "Apple" in result.stdout
    except Exception:
        return False

def main():
    print("🔍 Checking GPU support...\n")

    if has_cuda():
        print("✅ CUDA-capable NVIDIA GPU detected (torch.cuda.is_available() == True)")
        sys.exit(0)
    elif is_macos() and check_amd_on_macos():
        print("⚠️ macOS with AMD or Apple GPU detected (Metal supported)")
        sys.exit(0)
    else:
        print("❌ No supported GPU found (CUDA/AMD/Metal not detected).")
        print("    Model training may be slow or incompatible with GPU acceleration.")
        sys.exit(1)

if __name__ == "__main__":
    main()
