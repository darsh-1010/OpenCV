import cv2
import mediapipe as mp
import pyautogui  # Optional (for potential hand gesture control)

# Initialize variables for hand landmark coordinates
x1, y1, x2, y2 = 0, 0, 0, 0

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _, image = webcam.read()
    image = cv2.flip(image,1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_width)

                # Update landmark coordinates based on hand detection
                if id == 8:
                    x1, y1 = x, y
                elif id == 4:
                    x2, y2 = x, y

                # Draw circles at updated landmark positions (if hands are detected)
                cv2.circle(center=(x, y), img=image, radius=8, color=(0, 255, 255), thickness=3)

    dist = ((x2 - x1)**2 + (y2-y1)**2)**(0.5)//4
     # Draw a line between the updated landmark coordinates (if both are valid)
    if x1 and y1 and x2 and y2:  # Concise conditional check
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    if dist > 50:
        pyautogui.press("volumeup")
    else:
        pyautogui.press("volumedown")
                

    cv2.imshow("Hand Volume Control", image)
    key = cv2.waitKey(10)
    if key == 27:  # Esc key to quit
        break

webcam.release()
cv2.destroyAllWindows()
