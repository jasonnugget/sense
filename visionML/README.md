VisionML YOLO Boilerplate
=========================

Production-ready starter for training YOLO models with the `ultralytics` stack. Assumes Python 3.10+ and GPU available (CUDA 11.8+ or Apple Silicon).

Project layout
--------------
- `configs/dataset.yaml` – YOLO dataset spec pointing at train/val/test splits.
- `configs/training.yaml` – Centralized hyperparameters and experiment metadata.
- `src/train.py` – Single entry point to launch training and optional evaluation.
- `src/utils/env.py` – Minimal env loader for `.env` and required variables.
- `.env.example` – Environment variables to copy into `.env`.
- `requirements.txt` – Pinned high-level dependencies (install torch per platform instructions below).

Environment variables
---------------------
Copy `.env.example` to `.env` and adjust:
- `DATA_DIR` (required): Absolute path to dataset root containing `images/` and `labels/` subfolders.
- `RUNS_DIR` (optional): Where YOLO run artifacts are saved. Defaults to `runs/` under repo.
- `PROJECT_NAME` (optional): Logical project name for run grouping. Defaults to `visionml`.
- `WANDB_API_KEY` (optional): Enable Weights & Biases logging when set.
- `DEVICE` (optional): `cpu`, `mps`, or CUDA device string (e.g., `0`, `0,1`). Defaults to `0` when CUDA available.

Dependencies
------------
1) Install PyTorch with the correct CUDA or MPS build (follow https://pytorch.org/get-started/locally/). Example for CUDA 11.8:
   ```bash
   pip install --extra-index-url https://download.pytorch.org/whl/cu118 torch torchvision torchaudio
   ```
2) Install Python deps:
   ```bash
   pip install -r requirements.txt
   ```

Dataset structure
-----------------
Expected YOLO-format folders under `${DATA_DIR}`:
```
${DATA_DIR}/
  images/
    train/*.jpg
    val/*.jpg
    test/*.jpg   # optional
  labels/
    train/*.txt
    val/*.txt
    test/*.txt   # optional
```
Each label file uses YOLO class indexing and normalized xywh format.

Running training
----------------
```bash
cp .env.example .env  # edit paths
python -m src.train --epochs 100 --batch 16 --imgsz 640 --model yolov8n.pt
```
Flags override `configs/training.yaml`. See `python -m src.train --help` for full options.

Experiment logging
------------------
- Weights & Biases auto-enables when `WANDB_API_KEY` is present in the environment.
- Runs are stored under `${RUNS_DIR}`; artifacts include weights, metrics, and predictions.

Testing & inference quickstart
------------------------------
- Validate trained weights: `python -m src.train --weights runs/detect/train/weights/best.pt --mode val`
- Single-image inference: `yolo predict model=runs/detect/train/weights/best.pt source=/path/to/image.jpg`

Security & reproducibility
--------------------------
- Locked dependency versions live in `requirements.txt`; prefer virtualenv or venv per project.
- Keep datasets outside the repo; only configs live here to avoid large files.

Next steps
----------
- Integrate CI to lint and run a short sanity train on a tiny subset.
- Extend `configs/training.yaml` for sweeps, augmentations, and custom loss configs.
