import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()
    if ret:
        #convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #HSV value:
        #lower : hue -10, 100, 100, higher: h+10, 255, 255

        red = np.uint8([[[0,0,255]]]) #bgr value of red
        hsv_red  = cv2.cvtColor(red, cv2.COLOR_BGR2HSV) #gets hsv value of red

        #threshold the hsv value to get red color only
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        # cv2.imshow("mask", mask)

        #all things red
        part1 = cv2.bitwise_and(background, background, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        #all things not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2", part2)

        cv2.imshow("cloak", part1 + part2)



        if cv2.waitKey(5) == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
