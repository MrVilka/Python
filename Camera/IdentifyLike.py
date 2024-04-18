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

            # Получаем координаты кончиков большого и указательного пальцев
            thumb_tip = handLms.landmark[4]  # Индекс кончика большого пальца
            index_tip = handLms.landmark[8]  # Индекс кончика указательного пальца

            # Получаем вертикальные координаты кончиков пальцев
            thumb_tip_y = thumb_tip.y
            index_tip_y = index_tip.y

            # Проверяем, если большой и указательный пальцы подняты
            if thumb_tip_y < index_tip_y:
                # Если оба пальца подняты, распознаем жест "Лайк"
                cv2.putText(img, "Like", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Камера", img)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
