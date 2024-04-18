import cv2

# Указать IP-адрес и порт, на котором работает IP Webcam на вашем телефоне
# (узнайте IP-адрес вашего телефона в настройках приложения IP Webcam)
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

# Цикл для непрерывного чтения изображений с видеопотока
while True:
    # Захватить кадр с видеопотока
    ret, frame = cap.read()







    cv2.imshow("CameraPython", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()