import cv2  # OpenCV library for video processing
import os   # OS library to handle file paths

# Create the folder "Extracted Images" in the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
output_folder = os.path.join(script_directory, "Extracted Images")

# Check if the folder exists, and if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
video = cv2.VideoCapture(0)  # Accessing Webcame
frame_count = 0  # Counter to number the extracted frames

while video.isOpened():
    # Read each frame from the video
    ret, frame = video.read()
    if ret:

        frame = cv2.flip(frame,1)# 1 for y axis, -1 for x axis , 0 for both axes

        # Generate the file path for saving the frame
        file_path = os.path.join(output_folder, f"Frame_{frame_count}.png")

        # Display the frame
        cv2.imshow("Video Frame", frame)

        # Save the resized frame in the "Extracted Images" folder
        cv2.imwrite(file_path, frame)

        # Increment the frame counter
        frame_count += 1

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
