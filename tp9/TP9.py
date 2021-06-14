import cv2
import numpy as np

ref_point = []
i = 0


def shape_selection(event, x, y, flags, param):
    global ref_point, i

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point.append((x, y))
        cv2.circle(img, ref_point[i], 2, (0, 255, 0), 2)
        cv2.imshow("image", img)
        i = i + 1


def transformation(imgt):

    p1 = np.float32([[0, 0],
                     [1075, 0],
                     [1075, 528],
                     [0, 528]])
    p2 = np.float32([[74, 57],
                     [579, 138],
                     [578, 336],
                     [95, 475]])
    m1 = cv2.getPerspectiveTransform(p2, p1)
    imgt = cv2.warpPerspective(imgt, m1, (1075, 528))

    return imgt


image = cv2.imread('fcasa.jpeg')
image = cv2.resize(image, (640, 480))
img = transformation(image)
cv2.imshow("image", img)
cv2.imwrite('fcasa2.jpeg', img)
clone = img.copy()
cv2.setMouseCallback("image", shape_selection)

while 1:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        img = clone.copy()
        i = 0
        ref_point.clear()

    elif key == ord("m"):

        cv2.line(img, (ref_point[0]), (ref_point[1]), (0, 255, 0), 1)
        dist = (np.sqrt(((ref_point[0][0] - ref_point[1][0]) / 2) ** 2 +
                ((ref_point[0][1] - ref_point[1][1]) / 2) ** 2)) / 100

        a = round((ref_point[0][0] + ref_point[1][0]) / 2)
        b = round((ref_point[0][1] + ref_point[1][1]) / 2)
        cv2.putText(img, "{0:.2f}m".format(dist), (a+5, b-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

        cv2.imshow("image", img)
        break

    elif key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
