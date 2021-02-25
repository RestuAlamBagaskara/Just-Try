from cv2 import cv2
import sys
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(
        gray, 
        scaleFactor= 1.3, minNeighbors=5, minSize=(30,30),
        flags= cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0, 266,0), 4)
    
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()