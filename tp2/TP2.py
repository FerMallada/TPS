import cv2

img = cv2.imread('hojas.jpg', 0)
thr = 200

for i, row in enumerate(img):
    for j, col in enumerate(row):
        if col >= thr:
            img[i, j] = 255
        else:
            img[i, j] = 0

cv2.imwrite('resultado.jpg', img)
cv2.imshow('resultado.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
