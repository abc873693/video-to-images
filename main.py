
import cv2
import os
import argparse

out_path = './out'

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input_path',
        action='store',
        help='video input path.')
    parser.add_argument(
        '-r', '--resize',
        action='store',
        type=int,
        default=-0,
        help='resize to resize * resize image, default 0 is original size.')

    args = parser.parse_args()
    # print('[ INFO ] Options:', args)

    source_path = args.input_path
    size = args.resize

    if not os.path.exists(out_path):
            os.makedirs(out_path)
    # '/Users/rainvisitor/Movies/黃英哲老師實驗室提供影片/可見光/濁.avi'
    vc = cv2.VideoCapture(source_path)
    index = 0
    rval = vc.isOpened()
    while rval:
        index = index + 1
        rval, frame = vc.read()
        if rval:
            if(size != 0):
                frame = cv2.resize(frame, (size, size), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('./out/frame'+str(index).zfill(5) + '.jpg', frame)
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('Finished!!')
