#!/usr/bin/env python
# coding: utf-8

# installing pacheges

# In[1]:


# !pip install opencv-python
# !pip install mediapipe --user


# import librareis

# In[1]:


import cv2 as cv
import mediapipe as mp
import matplotlib.path as pltPath
import numpy as np


# In[2]:


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# declare the drawing specs

# In[3]:


dotDrawingSpec = mp_drawing.DrawingSpec(color=(50,0,50), thickness=2, circle_radius=1)
lineDrawingSpec = mp_drawing.DrawingSpec(color=(50,250,50), thickness=2, circle_radius=2) 


# first virsion 
# 

# its just detect the hands and draws the lines and dots

# In[4]:


cap = cv.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            image = cv.flip(image, 1)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, dotDrawingSpec, lineDrawingSpec)
#                     for i in range(5):
#                         cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[i].x, (120*i,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
#                         cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[i].y, (120*i,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
#                         cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[i].z, (120*i,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
#                         cv.putText(image, str(i), (120*i,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    
                    """
                    cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[0].x, (5,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[0].y, (5,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[0].z, (5,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "0", (5,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    
                    cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[1].x, (120,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[1].y, (120,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[1].z, (120,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "1", (120,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    
                    cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[2].x, (240,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[2].y, (240,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[2].z, (240,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "2", (240,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    
                    cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[3].x, (360,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[3].y, (360,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[3].z, (360,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "3", (360,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    
                    cv.putText(image, "x:%.4f"%results.multi_hand_landmarks[0].landmark[4].x, (480,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "y:%.4f"%results.multi_hand_landmarks[0].landmark[4].y, (480,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "z:%.4f"%results.multi_hand_landmarks[0].landmark[4].z, (480,60), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    cv.putText(image, "4", (480,80), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
                    """
            
            if results.multi_handedness:
                for hand in results.multi_handedness:
                    if hand.classification[0].index == 1:
                        pos = (480,100)
                    elif hand.classification[0].index == 0:
                        pos = (20,100)
                    cv.putText(image, 
                           str(hand.classification[0].label)+ 
                           "-%.4f"%hand.classification[0].score,
                           pos, cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250,0,0), 1)
                    
                
            
            cv.imshow("hand traking", image)


            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if key == ord('s'):
                cv.imwrite("file1.jpg", image)
                break

cap.release()
cv.destroyAllWindows()


# second virsion
# - simple comparison on Y axis to count fingers

# In[103]:


cap = cv.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        
        right_counter = 0

        if ret:

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            image = cv.flip(image, 1)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, dotDrawingSpec, lineDrawingSpec)
                    
                for finger_TIP in (8,12,16,20):
                    if results.multi_handedness[0].classification[0].index == 1 and results.multi_hand_landmarks[0].landmark[finger_TIP].y < results.multi_hand_landmarks[0].landmark[finger_TIP-1].y:
                        right_counter = right_counter+1
                
                cv.putText(image, "r:%.d"%right_counter, (400, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)

            
#             if results.multi_handedness:
#                 for hand in results.multi_handedness:
#                     if hand.classification[0].index == 1:
#                         pos = (480,100)
#                     elif hand.classification[0].index == 0:
#                         pos = (20,100)
#                     cv.putText(image, 
#                            str(hand.classification[0].index)+
#                            str(hand.classification[0].label)+ 
#                            "-%.4f"%hand.classification[0].score,
#                            pos, cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250,0,0), 1)
                    
                
            
            cv.imshow("hand traking", image)
#             print(result)


            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if key == ord('s'):
                cv.imwrite("file1.jpg", image)
                break

cap.release()
cv.destroyAllWindows()


# third version 
# - just checks the count of thumb finger
# - makes a polygon of some joints and checks if the thomb is inside of the polygon or not

# In[107]:


cap = cv.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        
        right_counter = 0

        if ret:

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            image = cv.flip(image, 1)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, dotDrawingSpec, lineDrawingSpec)
                    
                    
                poly = [[results.multi_hand_landmarks[0].landmark[p].x, results.multi_hand_landmarks[0].landmark[p].y] for p in (0, 1, 2, 3, 6, 10, 14, 18, 17)]
                point = [results.multi_hand_landmarks[0].landmark[4].x, results.multi_hand_landmarks[0].landmark[4].y]
                path = pltPath.Path(poly)
                if not path.contains_point(point):
                    right_counter = 1
                cv.putText(image, "r:%.d"%right_counter, (400, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)

            
                
            
            cv.imshow("hand traking", image)


            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if key == ord('s'):
                cv.imwrite("file1.jpg", image)
                break

cap.release()
cv.destroyAllWindows()


# fourth version
# - using polygon technique for all fingers

# In[7]:


cap = cv.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        
        right_counter =0
        left_counter = 0
        right_result = []
        left_result = []

        if ret:

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            image = cv.flip(image, 1)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, dotDrawingSpec, lineDrawingSpec)
#                     cv.putText(image, str(num), (40*num, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)
                    poly   = [[results.multi_hand_landmarks[num].landmark[p].x, results.multi_hand_landmarks[num].landmark[p].y] for p in (0, 1, 2, 3, 6, 10, 14, 18, 17)]
                    points = [[results.multi_hand_landmarks[num].landmark[p].x, results.multi_hand_landmarks[num].landmark[p].y] for p in (4, 8, 12, 16, 20)]
                    path = pltPath.Path(poly)
                    if results.multi_handedness[num].classification[0].index == 1:
                        right_result = [not elem for elem in path.contains_points(points)]
                        right_counter = sum(right_result)
                    elif results.multi_handedness[num].classification[0].index == 0:
                        left_result = [not elem for elem in path.contains_points(points)]
                        left_counter = sum(left_result)
                
                    
                
            cv.putText(image, "r:%.d"%right_counter, (400, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)
            cv.putText(image, "l:%.d"%left_counter, (40, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)

            
                
            
            cv.imshow("hand traking", image)


            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if key == ord('s'):
                cv.imwrite("file1.jpg", image)
                break

cap.release()
cv.destroyAllWindows()


# In[136]:


#just incase it needed
cap.release()
cv.destroyAllWindows()


# testing serial communication

# In[1]:


# !pip install pyserial


# In[4]:


import serial


# In[3]:


arduino = serial.Serial(port="COM7", baudrate=9600)


# In[10]:


text = "3,7"


# In[11]:


arduino.write(bytes(text,"utf-8"))


# In[9]:


arduino.close()


# combining codes

# In[18]:


def send_to_arduino():
    global left_counter, right_counter, sending_thread, arduino
#     if arduino.isOpen():
    arduino.write(bytes(str(left_counter) + "," + str(right_counter) + ",","utf-8"))
    sending_thread = threading.Timer(0.05,send_to_arduino)
    sending_thread.start()


# In[25]:


cap = cv.VideoCapture(0)
arduino = serial.Serial(port="COM7", baudrate=9600)


sending_thread = threading.Timer(0.01,send_to_arduino)
sending_thread.start()

right_counter = 0
left_counter = 0

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        
#         right_counter = 0
#         left_counter = 0
        right_result = []
        left_result = []

        if ret:

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            image = cv.flip(image, 1)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, dotDrawingSpec, lineDrawingSpec)
#                     cv.putText(image, str(num), (40*num, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)
                    poly   = [[results.multi_hand_landmarks[num].landmark[p].x, results.multi_hand_landmarks[num].landmark[p].y] for p in (0, 1, 2, 3, 6, 10, 14, 18, 17)]
                    points = [[results.multi_hand_landmarks[num].landmark[p].x, results.multi_hand_landmarks[num].landmark[p].y] for p in (4, 8, 12, 16, 20)]
                    path = pltPath.Path(poly)
                    if results.multi_handedness[num].classification[0].index == 1:
                        right_result = [not elem for elem in path.contains_points(points)]
                        right_counter = sum(right_result)
                    elif results.multi_handedness[num].classification[0].index == 0:
                        left_result = [not elem for elem in path.contains_points(points)]
                        left_counter = sum(left_result)
                
                if len(results.multi_hand_landmarks) == 1:
                    if results.multi_handedness[0].classification[0].index == 1:
                        left_result = []
                        left_counter = 0
                    elif results.multi_handedness[0].classification[0].index == 0:
                        right_result = []
                        right_counter = 0
                        
            else:
                right_result = []
                right_counter = 0
                left_result = []
                left_counter = 0
                
                    
                
            cv.putText(image, "r:%.d"%right_counter, (400, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)
            cv.putText(image, "l:%.d"%left_counter, (40, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (250, 250,5), 1)

#             arduino.write(bytes(str(left_counter) + "," + str(right_counter),"utf-8"))
            
                
            
            cv.imshow("hand traking", image)


            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if key == ord('s'):
                cv.imwrite("file1.jpg", image)
                break

                
sending_thread.cancel()                
arduino.close()
cap.release()
cv.destroyAllWindows()


# In[5]:


import threading


# In[6]:


left_counter = 2
right_counter = 2


# In[10]:


def send_to_arduino():
    global left_counter, right_counter, sending_thread, arduino
    arduino.write(bytes(str(left_counter) + "," + str(right_counter) + ",","utf-8"))
    sending_thread = threading.Timer(0.2,send_to_arduino)
    sending_thread.start()


# In[9]:


arduino = serial.Serial(port="COM7", baudrate=9600)

sending_thread = threading.Timer(0.5,send_to_arduino)
sending_thread.start()


# In[11]:


arduino.close()
sending_thread.cancel()


# seprator

# In[14]:


def hello():
    global cntr
    print(cntr)
    global t
    t = threading.Timer(10, hello)
    t.start()
    


# In[15]:


t2 = threading.Timer(1,pluse)
t2.start()
t = threading.Timer(10, hello)
t.start()


# In[16]:


t2.cancel()
t.cancel()

