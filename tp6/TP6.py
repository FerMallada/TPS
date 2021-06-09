import cv2
import numpy as np


ref_point = []
crop = False


def shape_selection(event, x, y, flags, param):

    global ref_point, crop

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))

        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


def transformation(img, angle, tx, ty, scl):

    (h, w) = (img.shape[0], img.shape[1])
    m = np.float32([[scl*np.cos(angle), -scl*np.sin(angle), tx], [scl*np.sin(angle), scl*np.cos(angle), ty]])
    out = cv2.warpAffine(img, m, (w, h))

    return out


image = cv2.imread('lenna.jpg')
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
    elif key == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
