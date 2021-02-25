from cv2 import cv2
import sys

#Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

#Create the Haar Carscade
faceCascade = cv2.CascadeClassifier(cascPath)

#membaca gambar
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#deteksi wajah dalam gambar
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(10,10),
    flags= cv2.CASCADE_SCALE_IMAGE
)
print(" {0} Wajah ditemukan!".format(len(faces)))

#menggambar persegi panjang
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0),5)
cv2.imshow("Wajah Ditemukan", image)
cv2.waitKey(0)