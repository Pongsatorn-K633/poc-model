@echo off
setlocal enabledelayedexpansion

:: === CONFIG ===
set VENV_DIR=venv
set GPU_REQ=requirements\requirements-gpu.txt
set CPU_REQ=requirements\requirements-cpu.txt
set CONDA_ENV=requirements\environment.yml
set GPU_SUPPORT=0

echo ===============================
echo 🧠 Smart Setup for poc-model
echo ===============================

:: Step 0: Check for Python and validate version
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found in PATH.
    echo 👉 Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Get major.minor version
for /f "usebackq delims=" %%i in (`python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"` ) do (
    set PY_VERSION=%%i
)

:: Split version manually
for /f "tokens=1,2 delims=." %%a in ("%PY_VERSION%") do (
    set PY_MAJOR=%%a
    set PY_MINOR=%%b
)

:: Validate version >= 3.8
set /a VER_CHECK=!PY_MAJOR!*10+!PY_MINOR!
if !VER_CHECK! LSS 38 (
    echo ❌ Python version must be at least 3.8 (found: !PY_MAJOR!.!PY_MINOR!)
    pause
    exit /b 1
)

:: Step 1: Ensure torch is installed to run GPU check
pip show torch >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Installing torch (lightweight check)...
    pip install torch --quiet
)

:: Step 2: Check for CUDA via PyTorch
echo 🔍 Checking GPU support...
python scripts\check_gpu.py
if %errorlevel% equ 0 (
    set GPU_SUPPORT=1
)

:: Step 3: Recommend Conda if GPU is available
if %GPU_SUPPORT% equ 1 (
    echo ✅ CUDA-capable NVIDIA GPU detected.
    echo.
    echo 🔷 RECOMMENDED: Use Conda for best GPU performance:
    echo --------------------------------------------
    echo 1. conda env create -f %CONDA_ENV%
    echo 2. conda activate poc-model
    echo --------------------------------------------
    echo.
    choice /M "Do you want to continue setup with pip + GPU instead?"
    if errorlevel 2 (
        echo ❌ Setup cancelled by user.
        pause
        exit /b 1
    )
    set REQ_FILE=%GPU_REQ%
) else (
    echo ⚠️ No CUDA GPU detected. Falling back to CPU-only setup.
    set REQ_FILE=%CPU_REQ%
)

:: Step 4: Create virtual environment if needed
if not exist "%VENV_DIR%\" (
    echo 📦 Creating virtual environment in '%VENV_DIR%'...
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment.
        pause
        exit /b 1
    )
)

:: Step 5: Activate virtual environment
echo ✅ Activating virtual environment...
call %VENV_DIR%\Scripts\activate.bat

:: Step 6: Install dependencies
echo 📄 Installing dependencies from %REQ_FILE%...
pip install --upgrade pip
pip install -r %REQ_FILE%

:: Step 7: Install the project in editable mode using pyproject.toml
echo 🧩 Installing poc-model in editable (dev) mode...
pip install -e .

:: Step 8: Copy AMP model into scripts folder to avoid download
echo ♻️ Copying yolo11n.pt for AMP compatibility...
if exist weights\pretrained_model\yolo11n.pt (
    copy /Y weights\pretrained_model\yolo11n.pt scripts\yolo11n.pt >nul
    echo ✅ yolo11n.pt copied to scripts\
) else (
    echo ⚠️ Warning: yolo11n.pt not found in weights\pretrained_model
)

echo.
echo 🎉 Setup complete!
echo 👉 To activate the environment later: venv\Scripts\activate
pause
