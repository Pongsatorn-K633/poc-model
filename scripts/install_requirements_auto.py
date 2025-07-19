import subprocess
import sys
import shutil
import os

# Resolve project root based on this script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

REQ_DIR = os.path.join(PROJECT_ROOT, "requirements")
GPU_REQ = os.path.join(REQ_DIR, "requirements-gpu.txt")
CPU_REQ = os.path.join(REQ_DIR, "requirements-cpu.txt")

def has_nvidia_gpu():
    return shutil.which("nvidia-smi") is not None

def ask_yes_no(question):
    while True:
        ans = input(f"{question} [Y/N]: ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please answer Y or N.")

def run_uv_install(req_file):
    if not os.path.exists(req_file):
        print(f"❌ Requirement file not found: {req_file}")
        sys.exit(1)

    # Show which interpreter & env
    print(f"🐍 Using Python: {sys.executable}")
    print(f"📂 Installing from: {req_file}")
    print("📦 Running: uv pip install ...\n")

    cmd = [
        "uv", "pip", "install",
        "-r", req_file,
        "--index-strategy", "unsafe-best-match"
    ]
    subprocess.check_call(cmd)

def main():
    print("🔍 Detecting system GPU support...")
    gpu = has_nvidia_gpu()
    chosen = GPU_REQ if gpu else CPU_REQ

    if gpu:
        print("✅ NVIDIA GPU detected -> selecting GPU requirements.")
    else:
        print("❌ No NVIDIA GPU detected -> selecting CPU requirements.")

    if not ask_yes_no(f"⚠️ Proceed with install from '{os.path.relpath(chosen, PROJECT_ROOT)}'?"):
        print("🚫 Cancelled.")
        return

    run_uv_install(chosen)
    print("\n✅ Done.")
    print("Tip: run 'python -c \"import torch; print(torch.cuda.is_available())\"' to verify.")

if __name__ == "__main__":
    main()
