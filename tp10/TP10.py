# Este programa es una aplicacion de realidad aumentada utilizando marcadores aruco.
# se utiliza una camara para capturar imagen, se detectan los marcadores aruco por medio de funciones de la
# libreria de opencv y se le superponen imagenes.
# Estas imagenes brindan informacion nutricional, la idea es que estos marcadores podrian ser colocados cerca de
# productos que no llevan envase, y por lo tanto no suelen brindar informacion nuricional al consumidor, como por
# ejemplo aquellos productos encontrados en dieteticas o verdulerias.


import cv2
import numpy as np

dic = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)  # inicializamos el diccionario del aruco
par = cv2.aruco.DetectorParameters_create()  # inicializamos los parametros del detector

cap = cv2.VideoCapture(0)  # iniciamos la captura de imagen

while 1:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # cada frame se pasa a escala de grises

    esq, ids, fakes = cv2.aruco.detectMarkers(gray, dic, parameters=par)  # detectamos los marcadores en la imagen


    if np.all(ids != None):

        aruco = cv2.aruco.drawDetectedMarkers(frame, esq)

        # extraemos los puntos de las esquinas en coordenadas separadas
        c0 = (esq[0][0][0][0], esq[0][0][0][1])
        c1 = (esq[0][0][1][0], esq[0][0][1][1])
        c2 = (esq[0][0][2][0], esq[0][0][2][1])
        c3 = (esq[0][0][3][0], esq[0][0][3][1])

        copy = frame.copy()

        # leemos las imagenes q vamos a sobreponer

        if ids == 50:
            img = cv2.imread("nuez.png")
        elif ids == 51:
            img = cv2.imread("arroz.jpg")
        elif ids == 52:
            img = cv2.imread("zanahoria.png")
        elif ids == 53:
            img = cv2.imread("brocoli.png")


        img = cv2.resize(img, (640, 480))
        size = img.shape

        # organizamos las coordenadas del aruco y de la imagen en matrices

        puntos_aruco = np.array([c0, c1, c2, c3])
        puntos_imagen = np.array([[0, 0],
                                  [size[1] - 1, 0],
                                  [size[1] - 1, size[0] - 1],
                                  [0, size[0] - 1]], dtype=float)

        # realizamos la homografia y la transformacion de perspectiva

        h, estado = cv2.findHomography(puntos_imagen, puntos_aruco)
        persp = cv2.warpPerspective(img, h, (size[1], size[0]))

        cv2.fillConvexPoly(copy, puntos_aruco.astype(int), 0, 16)
        copy = copy + persp
        cv2.imshow("Informacion Nutricional", copy)

    else:
        cv2.imshow("Informacion Nutricional", frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
