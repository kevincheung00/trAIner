import numpy as np
import argparse
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

file = open("emotionstats.txt", "w")

# Create the model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

angryCount = 0
disgustedCount = 0
fearfulCount = 0
happyCount = 0
neutralCount = 0
sadCount = 0
surprisedCount = 0



model.load_weights('model.h5')

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# start the webcam feed

input_video = cv2.VideoCapture("sample2.mp4")
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
# cap = cv2.VideoCapture(0)
while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = input_video.read()
    if not ret:
        break
    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        if maxindex == 0:
            angryCount += 1
        elif maxindex == 1:
            disgustedCount += 1
        elif maxindex == 2:
            fearfulCount += 1
        elif maxindex == 3:
            happyCount += 1
        elif maxindex == 4:
            neutralCount += 1
        elif maxindex == 5:
            sadCount += 1
        elif maxindex == 6:
            surprisedCount += 1
        # cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

slices = [angryCount, disgustedCount, fearfulCount, happyCount, neutralCount, sadCount, surprisedCount]
emotions = ["angry", "disgusted", "nervous", "happy", "neutral", "sad", "surprised"]

plt.pie(slices, labels=emotions)
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)


plt.axis("image")

plt.legend()

plt.show()



print("Angry Count: " + str(angryCount))
print("Disgusted Count: " + str(disgustedCount))
print("Fearful Count: " + str(fearfulCount))
print("Happy Count: " + str(happyCount))
print("Neutral Count: " + str(neutralCount))
print("Sad Count: " + str(sadCount))
print("Surprised Count: " + str(surprisedCount))

file.write(str(angryCount))
file.write(str(disgustedCount))
file.write(str(fearfulCount))
file.write(str(happyCount))
file.write(str(neutralCount))
file.write(str(sadCount))
file.write(str(surprisedCount))

input_video.release()
cv2.destroyAllWindows()
