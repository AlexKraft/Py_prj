import cv2
import numpy as np

# Створення чорного зображення розміром 1024x768
width, height = 1024, 768
ix, iy = -1, -1
drawing = False
# black_image = np.zeros((height, width, 3), np.uint8)

# # Відображення зображення
# cv2.imshow('Чорне зображення', black_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # Координати та розміри прямокутника
# x1, y1, w, h = 100, 200, 300, 150
# white_color = (255, 255, 255)  # Білий колір

# # Малюємо прямокутник на зображенні
# cv2.rectangle(black_image, (x1, y1), (x1 + w, y1 + h), white_color, -1)

# # Відображення зображення з прямокутником
# cv2.imshow('Зображення з прямокутником', black_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.imwrite('black_image.png', black_image)


# Отримання відеопотоку з веб-камери
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
bigger = cv2.resize(frame, (1024, 768))

def draw_rectangle_with_drag(event, x, y, flags, param):
    global ix, iy, drawing, bigger
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(bigger, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(bigger, pt1=(ix, iy), pt2=(x, y), color=(255, 255, 255), thickness=-1)

cv2.namedWindow(winname="Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_rectangle_with_drag)

while True:
    cv2.imshow("Title of Popup Window", bigger)
    if cv2.waitKey(10) == 27:
        break

cv2.imwrite('black_image.png', bigger)
cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    bigger2 = cv2.resize(frame, (1024, 768))
    # Застосування маски до відеокадру
    masked_frame = cv2.bitwise_and(bigger2, bigger)

    # Відображення відеокадру з маскою
    cv2.imshow('Відео з маскою', masked_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Натисніть "Esc", щоб вийти
        break

cap.release()
cv2.destroyAllWindows()
