import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, cam = cap.read() #ret -> True or False
    if ret:
        cv2.imshow("image", cam)
        if cv2.waitKey(5) == ord("s"):
            #save the image
            cv2.imwrite('image.jpg',cam)
            break

cap.release()
cv2.destroyAllWindows()