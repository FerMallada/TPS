import cv2

cap = cv2.VideoCapture('natur.mp4')

fps = int(cap.get(cv2.CAP_PROP_FPS))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

print("FPS: {0}".format(fps))
print(f"Width x height = {width} x {height}")

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if (cv2.waitKey(int(1/fps*1000)) & 0xFF) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
