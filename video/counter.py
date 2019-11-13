import numpy as np
import time
import imutils
import cv2
from datetime import datetime
import json
from data import save_tracking_to_file

from person import Person

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

# the output will be written to output.avi
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'MJPG'),15.,(640,480))

avg = None
video = cv2.VideoCapture("realtest.mp4")
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

inCount = 0
outCount = 0
save = True

persons = []
pid = 0
cx_margin= 50
cy_margin= 50

left_line = 299
right_line = 301


while 1:
    ret, frame = video.read()
    frame = imutils.resize(frame, width=600)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if avg is None:
        print("Starting...")
        avg = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, avg, 0.5)

    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]

    dilated = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 7000:
            continue
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        (x, y, w, h) = cv2.boundingRect(c)

        cv2.circle(frame,(cx,cy), 5, (0,0,255), -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # För att kunna ta bort persons som inte är med längre
        for p in persons:   
            p.update_frames(p.get_updated_frames()+1) # räknar hur många ramar varje objekt inte förnyade
            if p.get_updated_frames() > 20:
                persons.remove(p)

        new_people = True
        for p in persons:
            if abs(cx - p.getCX()) <= cx_margin and abs(cy - p.getCY() <= cy_margin):
                new_people = False
                p.update_cord(cx=cx, cy=cy)
                p.update_frames(0)
                break

        if new_people == True:
            p = Person(cx=cx, cy=cy, start_cx=cx, pid=pid)
            persons.append(p)
            pid += 1

    for p in persons:
        if p.get_start_cx() <= left_line and p.getCX() >= 350:
            print("Human walked in")
            inCount += 1
            persons.remove(p)
            save_tracking_to_file("in")
        elif p.get_start_cx() >= right_line and p.getCX() <= 250:
            print("Human walked out")
            outCount += 1
            persons.remove(p)
            save_tracking_to_file("out")
    
    # Lines
    cv2.line(frame, (100, 0), (100,600), (0,255,0), 2)
    cv2.line(frame, (500, 0), (500,600), (0,255,0), 2)

    # Texts
    cv2.putText(frame, "People In: {}".format(inCount), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "People Out: {}".format(outCount), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Frame",frame)
    #cv2.imshow("Gray",gray)
    #cv2.imshow("Dilated", dilated)
    #cv2.imshow("FrameDelta",frameDelta)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(10000)
    
    if save:
        data = {}
        data["inCount"] = inCount
        data["outCount"] = outCount
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
    
video.release()
cv2.destroyAllWindows()
