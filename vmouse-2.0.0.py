import cv2
import mediapipe as mp
import pyautogui
import time
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
m_y=0
ib_y=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id == 5:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    ib_x = screen_width/frame_width*x
                    ib_y = screen_height/frame_height*y

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    m_x = screen_width/frame_width*x
                    m_y = screen_height/frame_height*y

                    print('middle', m_x, m_y)
                    pyautogui.moveTo(m_x, m_y)

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    t_x = screen_width/frame_width*x
                    t_y = screen_height/frame_height*y
                    if abs(ib_y - t_y) < 10:
                      pyautogui.click(button='left', clicks=2, interval=3)

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    i_x = screen_width/frame_width*x
                    i_y = screen_height/frame_height*y
                    if abs(i_y - ib_y) < 10:
                        pyautogui.click(button='right', clicks=1, interval=3)


    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
