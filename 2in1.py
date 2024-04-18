import cv2
import mediapipe as mp

# Указать IP-адрес и порт, на котором работает IP Webcam на вашем телефоне
ip_address = "192.168.0.101"  # Пример IP-адреса вашего телефона
port = "8080"  # Пример порта вашего телефона

# Сформировать URL для доступа к видеопотоку с IP Webcam
url = "http://" + ip_address + ":" + port + "/video"

# Создать объект VideoCapture с URL-адресом видеопотока
cap = cv2.VideoCapture(url)

# Проверить, удалось ли открыть видеопоток
if not cap.isOpened():
    print("Ошибка: Не удалось открыть видеопоток.")
    exit()

# Создать окно с заданным названием
cv2.namedWindow("CameraPython", cv2.WINDOW_NORMAL)

# Инициализировать объекты Mediapipe
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

# Цикл для непрерывного чтения изображений с видеопотока
while True:
    # Захватить кадр с видеопотока
    ret, frame = cap.read()

    # Перевести изображение в RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обработать изображение с помощью Mediapipe
    results = hands.process(imgRGB)

    # Отобразить обнаруженные руки и точки
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            for id, point in enumerate(handLms.landmark):
                height, width, _ = frame.shape
                cx, cy = int(point.x * width), int(point.y * height)
                if id == 8:  # Точка для кончика пальца
                    cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    # Отобразить изображение
    cv2.imshow("CameraPython", frame)

    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освободить ресурсы и закрыть окно
cap.release()
cv2.destroyAllWindows()
