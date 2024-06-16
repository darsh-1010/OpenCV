## OpenCV
Different projects such as gesture volume control using python library called OpenCV

## Project 1 : Gesture Volume Control

This project allows you to control your computer's volume using intuitive hand gestures captured by your webcam. It leverages the capabilities of OpenCV for computer vision and MediaPipe for hand landmark detection.

**Features:**
- **Real-time Volume Control:** Adjusts volume in real-time based on the distance between your thumb and index finger.
- **Intuitive Gestures:** Spread your thumb and index finger apart to increase volume, contract them to decrease volume.
- **Optional Mirroring:** Flips the webcam image for a more natural experience (optional).
- **Customizable Sensitivity:** Adjust the threshold distance that triggers volume changes.

**Requirements:**
- Python 3.x
- OpenCV (cv2)
- MediaPipe (mediapipe)
- Optional: pyautogui (for keyboard shortcuts) - Install with `pip install pyautogui`

**How to Use:**
1. Download or clone this repository.
2. Ensure you have the required libraries installed (`cv2`, `mediapipe`, and optionally `pyautogui`).
3. Run the script: `python hand_volume_control.py` (replace with the actual script name if different).
4. A window will display your webcam feed with hand landmarks and volume control feedback.
5. Spread your thumb and index finger apart to increase volume, contract them to decrease volume.
6. Press the Esc key to exit the program.

**Customization:**
- Edit the `dist` threshold value in the code to adjust the sensitivity of volume changes.
- Explore other hand gestures using different finger combinations or landmark positions (requires code modifications).

**Additional Notes:**
- Consider error handling for cases where the webcam is unavailable or MediaPipe fails to initialize.
- Explore performance optimization techniques for real-time applications (e.g., frame rate reduction).

**Further Development:**

- Implement continuous volume adjustment based on the calculated distance.
- Introduce a hand gesture to mute/unmute the volume.
- Explore more complex hand gesture recognition for additional functionalities.

