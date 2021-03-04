from cv2 import cv2

video =cv2.VideoCapture(0)
muka = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mata = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    cond, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = muka.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in wajah:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)
        roiwarna = frame[y:y+h, x:x+w]
        roigray = gray [y:y+h, x:x+w]
        eye = mata.detectMultiScale(roigray, 1.1, 3)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roiwarna, (ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    cv2.imshow('Detection With Camera', frame)

    k=cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()