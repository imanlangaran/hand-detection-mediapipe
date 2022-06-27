import cv2 as cv
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


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
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                             mp_drawing.DrawingSpec(color=(0,0,250), thickness=5, circle_radius=3),
                                             mp_drawing.DrawingSpec(color=(0,250,0), thickness=2, circle_radius=2))

            
            cv.imshow("hand traking", image)


        if cv.waitKey(1) == ord('q'):
            break

cap.release()
cv.destroyAllWindows()



