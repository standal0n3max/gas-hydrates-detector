# Gas hydrates detector
## CV_webam
This code  demonstrates a real-time video processing application using TensorFlow and OpenCV for predicting hydration levels from a webcam feed.
###Overview
The script utilizes a pre-trained deep learning model (hydrate_model.h5) to classify frames from the webcam into two categories: "hydrates_yes" or "hydrates_no." The model expects input frames resized to 150x150 pixels and uses the TensorFlow library for predictions.
###Functionality
- Video Capture: Accesses the default webcam (VideoCapture(0)) and continuously captures frames.
- Prediction: Utilizes the loaded model to predict whether a frame indicates hydration or not. This prediction occurs in real-time for each frame captured.
- Video Saving Logic:
  + Saves a video clip if a certain number of consecutive frames are classified as "hydrates_yes" within a defined time interval (10 seconds by default).
  + Deletes the previous saved video clip if no "hydrates_yes" frames are detected in a time interval.
- User Interaction: The script exits when the 'q' key is pressed.
###Dependencies
Python 3.x
TensorFlow
OpenCV (cv2)
numpy
###Usage
1. Ensure all dependencies are installed (pip install tensorflow opencv-python numpy).
2. Place the pre-trained model file (hydrate_model.h5) in the same directory as this script.
3. Run the script.
###File Structure
hydrate_model.h5: Pre-trained deep learning model for hydration prediction.
Processing/temp/: Directory to store temporary video clips.
###Usage Notes
Ensure proper camera access and permissions for the script to use the webcam.
Adjust the time_interval, required_frames, and other parameters based on specific requirements.
The script is currently configured to work with the default webcam ('0'). Change VideoCapture(0) if using a different camera.
