import torch

def check_cuda():
    print("🔍 Checking CUDA availability...\n")
    
    if torch.cuda.is_available():
        print("✅ CUDA is available!")
        print(f"🖥️  GPU Device Name : {torch.cuda.get_device_name(0)}")
        print(f"🔢 Number of Devices: {torch.cuda.device_count()}")
        print(f"🧩 CUDA Version     : {torch.version.cuda}\n")
    else:
        print("❌ CUDA is NOT available.")
        print("⚠️  Possible reasons:")
        print("- CUDA-capable GPU not found or drivers not installed.")
        print("- Installed PyTorch version is CPU-only.")
        print("- CUDA Toolkit or PyTorch CUDA not installed in environment.\n")
        
# def check_model():
#     import os
#     print(os.path.exists("yolo11m.pt"))  # should return True


if __name__ == "__main__":
    check_cuda()
    # check_model()

