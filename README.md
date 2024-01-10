# Gas hydrates detector
## Overview
The script utilizes a pre-trained deep learning model (hydrate_model.h5) to classify frames from the webcam into two categories: "hydrates_yes" or "hydrates_no." The model expects input frames resized to 150x150 pixels and uses the TensorFlow library for predictions.
### CV_webcam.py
This code  demonstrates a real-time video processing application using TensorFlow and OpenCV for predicting hydration levels from a webcam feed.
### bot.py
Script complements the video processing functionality by integrating a Telegram bot to notify users when a certain condition is met during video processing. Specifically, when the video_processing.py script detects hydration nucleation (three or more hydration-positive videos saved in the 'Processing/temp' directory), the Telegram bot sends a notification to the specified chat ID.
### main.py
The main.py script orchestrates the execution of the video processing and Telegram bot scripts by launching them as separate subprocesses.
## Functionality
- Video Capture: Accesses the default webcam (VideoCapture(0)) and continuously captures frames.
- Prediction: Utilizes the loaded model to predict whether a frame indicates hydration or not. This prediction occurs in real-time for each frame captured.
- Video Saving Logic:
  + Saves a video clip if a certain number of consecutive frames are classified as "hydrates_yes" within a defined time interval (10 seconds by default).
  + Deletes the previous saved video clip if no "hydrates_yes" frames are detected in a time interval.
- User Interaction: The script exits when the 'q' key is pressed.
- Telegram Bot Setup: Creates a bot object using the telebot library and sets up bot token and chat ID.
- Directory Handling: Checks for the existence of the 'Processing/saved' directory and creates it if absent.
- Continuous Monitoring: Monitors the 'Processing/temp' directory, counting the number of '.mp4' video files.
- Sends a Telegram message ("Hydrate nucleation occurred") and moves videos to 'Processing/saved' when three or more videos are detected.
- Subprocess Management: Launches bot.py and CV_webcam.py as separate subprocesses using Python's subprocess module.
## Dependencies
certifi==2023.11.17
charset-normalizer==3.3.2
Cython==3.0.7
h5py==3.10.0
idna==3.6
keras==2.13.1
libclang==16.0.6
numpy==1.24.3
opencv-python==4.5.5.62
packaging==23.2
pyTelegramBotAPI==4.14.1
requests==2.31.0
tensorboard==2.13.0
tensorboard-data-server==0.7.2
tensorflow==2.13.1
tensorflow-estimator==2.13.0
tensorflow-io-gcs-filesystem==0.34.0
urllib3==2.1.0
wheel==0.42.0
## Usage
1. Ensure all dependencies are installed (pip install tensorflow opencv-python numpy).
2. Place the pre-trained model file (hydrate_model.h5) in the same directory as this script.
3. Run the script.
## File Structure
- CV_webcam.py: Real-time video processing script for hydration prediction.
- bot.py: Telegram bot script for notification and directory management.
- hydrate_model.h5: Pre-trained deep learning model for hydration prediction.
- Processing/
  + temp/: Directory to store temporary video clips.
  + saved/: Directory to store processed videos.
## Usage Notes
Ensure proper camera access and permissions for the script to use the webcam.
Adjust the time_interval, required_frames, and other parameters based on specific requirements.
The script is currently configured to work with the default webcam ('0'). Change VideoCapture(0) if using a different camera.
