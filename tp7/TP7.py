import cv2
import numpy as np


ref_point = []
crop = False
i = 0


def shape_selection(event, x, y, flags, param):

    global ref_point, crop

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))

        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


def shape_selection2(event, x, y, flags, param):

    global ref_point, crop, i

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point.append((x, y))
        cv2.circle(image, ref_point[i], 2,  (0, 255, 0), 2)
        cv2.imshow("image2", image)
        i = i+1


def transformation(img, angle, tx, ty, scl):

    (h, w) = (img.shape[0], img.shape[1])
    m = np.float32([[scl*np.cos(angle), -scl*np.sin(angle), tx], [scl*np.sin(angle), scl*np.cos(angle), ty]])
    out = cv2.warpAffine(img, m, (w, h))

    return out


def transformation2(imagen, copia):
    
    (h1, w1) = (imagen.shape[0], imagen.shape[1])
    p1 = np.float32([[0, 0],
                     [1000, 0],
                     [0, 1000]])
    p2 = np.float32([[ref_point[1]],
                     [ref_point[0]],
                     [ref_point[2]]])
    m1 = cv2.getAffineTransform(p1, p2)
    affine = cv2.warpAffine(imagen, m1, (w1, h1))

    affine_gray = cv2.cvtColor(affine, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(affine_gray, 0.1, 255, cv2.THRESH_BINARY)
    invert_mask = cv2.bitwise_not(mask)

    back = cv2.bitwise_and(copia, copia, mask=invert_mask)
    front = cv2.bitwise_and(affine, affine, mask=mask)

    dst = cv2.add(back, front)
    rows, cols, channels = affine.shape
    copia[0:rows, 0:cols] = dst

    return copia


image = cv2.imread('lenna.jpg')
image2 = cv2.imread('a.jpeg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)


while 1:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()

    elif key == ord("g"):
        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
        cv2.imshow("crop_img", crop_img)
        cv2.imwrite('lenna2.jpg', crop_img)
        break
    elif key == ord("e"):
        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
        crop_img = transformation(crop_img, 270, 20, 20, 1)
        cv2.imshow("crop_img", crop_img)
        cv2.imwrite('lenna3.jpg', crop_img)
        break
    elif key == ord("y"):
        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
        crop_img = transformation(crop_img, 270, 20, 20, 1.5)
        cv2.imshow("crop_img", crop_img)
        cv2.imwrite('lenna4.jpg', crop_img)
        break
    elif key == ord("a"):
        cv2.destroyAllWindows()
        cv2.namedWindow("image2")
        cv2.setMouseCallback("image2", shape_selection2)

        while 1:
            cv2.imshow("image2", image)
            key = cv2.waitKey(1) & 0xFF
            if i == 3:
                break

        resultado = transformation2(image2, clone)
        cv2.imshow("image2", resultado)
        cv2.imwrite('lenna5.jpg', resultado)
        break
    elif key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
