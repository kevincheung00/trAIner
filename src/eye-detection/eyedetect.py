import cv2
import numpy as np

file = open("eyestats.txt", "w")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture("sample.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
eyecount = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y-int((y + h) * 0.7), x:x + w]
        roi_color = frame[y:y-int((y + h) * 0.7), x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)



        if type(eyes) == np.ndarray:
            eyecount+=1

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ew+ew, ey+eh), (0,255,0), 2)

    cv2.imshow('img', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(eyecount)


cap.release()
cv2.destroyAllWindows()
