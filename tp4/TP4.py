import cv2

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
    elif key == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
