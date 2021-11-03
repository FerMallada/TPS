import numpy as np
import cv2

MIN_MATCH_COUNT = 10

img1 = cv2.imread('libro1.jpg')  # Leemos la imagen 1
img2 = cv2.imread('libro2.jpg')  # Leemos la imagen 2
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

dscr = cv2.xfeatures2d.SIFT_create()  # Inicializamos el detector y el descriptor

kp1, des1 = dscr.detectAndCompute(img1, None)  # Encontramos los puntos clave y los descriptores con SIFT en la imagen 1
kp2, des2 = dscr.detectAndCompute(img2, None)  # Encontramos los puntos clave y los descriptores con SIFT en la imagen 2

matcher = cv2.BFMatcher(cv2.NORM_L2)
matches = matcher.knnMatch(des1, des2, k=2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

if len(good) > MIN_MATCH_COUNT:
    scr_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(dst_pts, scr_pts, cv2.RANSAC, 5.0)  # Computamos la homografía con RANSAC

wimg2 = cv2.warpPerspective(img2, H, (640, 480))  # Aplicamos la transformación perspectiva H a la imagen 2

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)
cv2.imwrite('Mezcla.jpg', blend)
cv2.imshow('Mezcla', blend)

cv2.waitKey(0)
cv2.destroyAllWindows()
