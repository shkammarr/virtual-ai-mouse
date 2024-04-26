import cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import threading
import time

detector = HandDetector(detectionCon=0.9, maxHands=1)

cap = cv2.VideoCapture(0)
# 0 for external, 1 for internal webcam
# width and height
cam_w, cam_h = 645, 485
cap.set(3, cam_w)
cap.set(4, cam_h)

frameR = 100  # writing this becoz hand ges is not working after a limit
l_delay = 0


def l_clk_delay():
    global l_delay
    global l_clk_thread
    time.sleep(1)  # time interval
    l_delay = 0
    l_clk_thread = threading.Thread(target=l_clk_delay)


def r_clk_delay():
    global r_delay
    global r_clk_thread
    time.sleep(1)  # time interval
    r_delay = 0
    r_clk_thread = threading.Thread(target=r_clk_delay)


def double_clk_delay():
    global double_delay
    global double_clk_thread
    time.sleep(1)
    double_delay = 0
    double_clk_thread = threading.Thread(target=double_clk_delay)


l_clk_thread = threading.Thread(target=l_clk_delay)
r_clk_thread = threading.Thread(target=r_clk_delay)
double_clk_thread = threading.Thread(target=double_clk_delay)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.rectangle(img, (frameR, frameR), (cam_w - frameR, cam_h - frameR), (255, 0, 255), 2)

    if hands:
        print(hands)  # Print the hands dictionary to inspect its structure
        # Access the correct key for the landmark list
        lmlist = hands[0]['lmList']  # Adjust the key based on the structure
        ind_x, ind_y = lmlist[8][0], lmlist[8][1]  # using 8 landmark
        mid_x, mid_y = lmlist[12][0], lmlist[12][1]
        # drawing a circle to show the tip of index finger
        cv2.circle(img, (ind_x, ind_y), 5, (0, 255, 255), 2)

        # we only want to move mouse, only at index finger hence
        fingers = detector.fingersUp(hands[0])  # 0 for open, 1 for close
        print(fingers)

        # mouse movement only when index finger is on
        if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 1:
            conv_x = int(np.interp(ind_x, (frameR, cam_w - frameR), (0, 1278)))
            conv_y = int(np.interp(ind_y, (frameR, cam_h - frameR), (0, 720)))
            mouse.move(conv_x, conv_y)  # for moving mouse

            # left click
            # if both index and middle finger are open,
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1:
            if abs(ind_x - mid_x) < 25:
                if fingers[3] == 0 and l_delay == 0:
                    mouse.click(button="left")
                    l_delay = 1
                    l_clk_thread.start()

                # it was giving multiple click so, we will use threading
                # right click
                if fingers[3] == 1 and l_delay == 0:
                    mouse.click(button="right")
                    l_delay = 1
                    l_clk_thread.start()

        # mouse scrolling
        # index middle and thumb is open & pinky close = downward scrolling
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and fingers[4] == 0:
            if abs(ind_x - mid_x) < 25:
                mouse.wheel(delta=-1)

        # index middle and thumb is open & pinky close = upward scrolling
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and fingers[4] == 1:
            if abs(ind_x - mid_x) < 25:
                mouse.wheel(delta=+1)
        # piny open -> up scroll
        # pinky close -> down scroll

        # double click
        if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[4] == 0:
            mouse.double_click(button="left")

    cv2.imshow("Camera Feed", img)
    cv2.waitKey(1)
