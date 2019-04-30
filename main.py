
import cv2
vc = cv2.VideoCapture('clear.avi')
c = 0
rval = vc.isOpened()
while rval:
    c = c + 1
    rval, frame = vc.read()
    if rval:
        frame = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('./out/frame'+str(c).zfill(5) + '.jpg', frame)
        cv2.waitKey(1)
    else:
        break
vc.release()
