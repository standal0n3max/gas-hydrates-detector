import os
import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import time
from datetime import datetime


# Define the directory to save temporary videos
temp_dir = 'Processing/temp'
os.makedirs(temp_dir, exist_ok=True)  # Create the directory if it doesn't exist

# First video for start only
current_datetime = datetime.now()
date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
video_filename = f'{temp_dir}/{date_time_str}.mp4'
out = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
out.release()
previous_out = video_filename

def predict_image_class(model, frame):
    # Preprocess the frame
    img = cv2.resize(frame, (150, 150))  # Resize frame to match model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to between 0 and 1

    # Make the prediction
    start_time = time.time()  # Start time measurement
    prediction = model.predict(img_array)
    end_time = time.time()  # End time measurement

    processing_time = end_time - start_time  # Calculate processing time

    # Decode the prediction
    if prediction[0][0] > 0.5:
        return processing_time, "hydrates_yes"
    else:
        return processing_time, "hydrates_no"

# Load the trained model
model = tf.keras.models.load_model('hydrate_model.h5')

# Access the webcam
video_capture = cv2.VideoCapture(0)  # '0' usually represents the default webcam

# Initialize variables for time-based video saving
start_time = time.time()
time_interval = 10  # Save video every X seconds
frame_counter = 0
required_frames = 4  # Save video if at least Y consecutive frames have 'hydrates_yes' prediction


# Initialize VideoWriter object and variables
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
#out = None
hydrates_yes_count = 0



while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error reading frame from webcam")
        break

    # Perform any processing or prediction here
    processing_time, predicted_class = predict_image_class(model, frame)
    cv2.putText(frame, f'Predicted Class: {predicted_class}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Check if predicted_class is 'hydrates_yes' and increment the counter
    if predicted_class == 'hydrates_yes':
        hydrates_yes_count += 1

    # Write the frame into the output video every 30 seconds
    elapsed_time = time.time() - start_time

    # If enough 'hydrates_yes' frames, save the video
    if elapsed_time > time_interval:
        if hydrates_yes_count >= required_frames:
            # If an existing video clip is open, release it
            if out is not None:
                out.release()

            # Define a filename with current date and time
            current_datetime = datetime.now()
            date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            video_filename = f'{temp_dir}/{date_time_str}.mp4'

            # Create a new VideoWriter object for the clip
            out = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

            # Reset start time for the next interval
            start_time = time.time()
        else:
            hydrates_yes_count = 0
            # Delete previous video if there is no hydrates
            if os.path.exists(previous_out):
                os.remove(previous_out)
                print(f"Deleted file: {previous_out}")
            else:
                print(f"File not found: {previous_out}")

            # Reset start time for the next interval
            start_time = time.time()

        # Reset counters for the next interval
        previous_out = video_filename
        hydrates_yes_count = 0


    # Write the frame into the output video
    if out is not None:
        out.write(frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video writer, webcam, and close all windows
if out is not None:
    out.release()
video_capture.release()
cv2.destroyAllWindows()
#%%

#%%
