from cv2 import cv2 as cv
import time
from datetime import datetime
import os
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string(
    'url', 'rtsp://192.168.100.10/h264/ch1/main/av_stream', 'url for rtsp source')
flags.DEFINE_boolean('dnot_show', False, 'show rtsp stream in window')
flags.DEFINE_boolean('dnot_save', False, 'save image to dir')


def main(_argv):
    rtsp_source = FLAGS.url

    cap = cv.VideoCapture(rtsp_source)

    start = time.time()

    out_path = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if (not FLAGS.dnot_save) and (not os.path.exists(out_path)):
        print('will save in {0}'.format(out_path))
        os.makedirs(out_path)

    index = 0

    while(cap.isOpened()):
        _, frame = cap.read()
        end = time.time()
        seconds = end - start
        if not FLAGS.dnot_save:
            cv.imwrite('./{0}/frame{1}.jpg'.format(out_path,
                                                   str(index).zfill(5)), frame)

        if not FLAGS.dnot_show:
            frameOfWindows = cv.resize(
                frame, (416, 416), interpolation=cv.INTER_CUBIC)
            frameOfWindows = cv.putText(frameOfWindows, 'FPS: {:.0f} '.format(1.0 / seconds), (0, 30),
                                        cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
            cv.imshow('rtsp live stream', frameOfWindows)

        #print( 1.0 / seconds)
        if int(seconds) == 100:
            print('end')
            break
        start = end
        index = index + 1
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
