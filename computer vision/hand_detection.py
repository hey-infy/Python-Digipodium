import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands    #AI model to detect hand 

cam = cv2.VideoCapture(0)
with mp_hands.Hands( model_complexity = 0, min_detection_confidence = .9, min_tracking_confidence = .9) as hands:    #Load AI which detect hand with all three parameter
    while cam.isOpened():
        status, image = cam.read()
        if not status:
            break
        image.flags.writeable = False   #to improve perfromance , optionally making image unwritable
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    #convert image from bgr to rgb for ai
        results = hands.process(image)
        image.flags.writeable = True #to make image writeable again 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)   #convert img from rgb to bgr for display to human 

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmark,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style() 
                )
        cv2.imshow('MediaPipe Example',image)
        if cv2.waitKey(5) == 27:
            break
cam.release()