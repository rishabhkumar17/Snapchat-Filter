import cv2
import numpy as np
import pandas as pd


image = './Test/Before.png'


face_cascade = cv2.CascadeClassifier("./third-party/haarcascade_frontalface_alt.xml")
eyecascade = cv2.CascadeClassifier("./third-party/frontalEyes35x16.xml")
nosecascade = cv2.CascadeClassifier("./third-party/Nose18x15.xml")

glasses = cv2.imread('./Filter/glasses.png', -1)
mustache = cv2.imread('./Filter/mustache.png', -1)

frame = cv2.imread(image)

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_frame, 1.2, 5)

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

for face in faces:

    x, y, w, h = face
    
    rol_gray =  gray_frame[y:y+h, x:x+h]
    rol_color = frame[y:y+h, x:x+h]


    eyes = eyecascade.detectMultiScale(rol_gray,1.3,3)
    for (ex,ey,ew,eh) in eyes:

        glasses = cv2.resize(glasses,(ew,eh))
        
        gw, gh, gc = glasses.shape
        for i in range(0, gw):
            for j in range(0, gh):
                if glasses[i,j][3] != 0:
                    rol_color[ey + i, ex + j] = glasses[i,j]

    nose = nosecascade.detectMultiScale(rol_gray, 1.3, 7)
    for (nx, ny, nw, nh) in nose:

        mustache = cv2.resize(mustache, (nw+10,nh))

        mw, mh, mc = mustache.shape
        for i in range(0,mw):
            for j in range(0, mh):
                if mustache[i,j][3] != 0:
                    rol_color[ny+int(nh/2.0)+i, nx+j+3] = mustache[i,j]

frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

cv2.imshow("window", frame)

frame = np.resize(frame,(1,3))

pd.DataFrame(frame,  columns=['Channel 1', 'Channel 2', 'Channel 3']).to_csv('./Prediction.csv', index= False)

cv2.waitKey(0)
