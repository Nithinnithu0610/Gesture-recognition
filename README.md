
# Task_3_final - Gesture Recognition (Prepared for Submission)

This folder merges your uploaded Task 3 files and adds the missing pieces required by the reviewer:
- System usage logging (CPU & memory)
- Gesture outputs logging
- Saving frames for detected gestures
- A second 'SmolVLM' module (placeholder + integration notes)
- Benchmark scripts to compare OpenCV/MediaPipe vs SmolVLM
- requirements.txt and organized docs

**How to run (example)**

1. Create a virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the main detector (OpenCV + MediaPipe) on a video or webcam:
```
python execute.py --input sample_video.mp4 --out_dir ./outputs --use_video
```

3. Run SmolVLM module (placeholder) similarly:
```
python smolvlm_module/smolvlm_module.py --input sample_video.mp4 --out_dir ./outputs_smolvlm
```

4. Run benchmarks:
```
python benchmarks/run_benchmarks.py --input_dir ./sample_videos --output benchmarks/results_summary.csv
```

See docs/ for diagrams and task details (copied from your uploads).

Notes:
- The SmolVLM module is prepared as an integration wrapper and includes instructions on how to connect a real SmolVLM model (link to interview task provided).
- Example `benchmarks/results_summary.csv` is included with sample numbers for demonstration. Replace with real run results after executing the scripts.
