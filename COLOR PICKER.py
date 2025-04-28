# Importing Libraries

import cv2  
import numpy as np  

# Callback function for the trackbar 
def trackbar_callback(x):
    pass

# Create a blank image 
color_canvas = np.zeros((500, 500, 3), np.uint8)

# Create a named window 
cv2.namedWindow("COLOR PICKER")

# Create a switch trackbar 
switch_label = "ON/OFF"
cv2.createTrackbar(switch_label, "COLOR PICKER", 0, 1, trackbar_callback)

# Create trackbars for RGB color components
cv2.createTrackbar("Red", "COLOR PICKER", 0, 255, trackbar_callback)
cv2.createTrackbar("Green", "COLOR PICKER", 0, 255, trackbar_callback)
cv2.createTrackbar("Blue", "COLOR PICKER", 0, 255, trackbar_callback)

# Main loop 
while True:
    # Display the current canvas
    cv2.imshow("COLOR PICKER", color_canvas)

    # Exit when 'q' key is pressed 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Get the position of the ON/OFF switch
    switch_state = cv2.getTrackbarPos(switch_label, "COLOR PICKER")

    # Get the values of RGB color components
    red_value = cv2.getTrackbarPos("Red", "COLOR PICKER")
    green_value = cv2.getTrackbarPos("Green", "COLOR PICKER")
    blue_value = cv2.getTrackbarPos("Blue", "COLOR PICKER")

    # Update the canvas based on the switch state
    if switch_state == 0:
        # Set the canvas to black when the switch is OFF
        color_canvas[:] = 0
    else:
        # Update the canvas with the selected RGB color values when the switch is ON
        color_canvas[:] = [blue_value, green_value, red_value]

# Destroy the loop
cv2.destroyAllWindows()
