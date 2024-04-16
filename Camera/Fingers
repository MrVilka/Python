import cv2
import mediapipe as mp
camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        for id, point in enumerate(handLms.landmark):
            width, height, color = img.shape
            width, height = int(point.x * height), int(point.y * width)
            if(id == 8):
                cv2.circle(img, (width, height), 15, (255, 0, 255), cv2.FILLED)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break

