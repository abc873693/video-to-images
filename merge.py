
import cv2
import os
import shutil
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_path',
                        action='store',
                        help='raw images dir path')
    parser.add_argument('--labels_path',
                        action='store',
                        help='label dir path')
    
    args = parser.parse_args()

    source_path = args.source_path
    label_path = args.labels_path

    for filepname in os.listdir(label_path):
        if ".txt" in filepname and "classes.txt" != filepname:
            shutil.copy(
                source_path + '/' + filepname.replace('.txt', '.jpg'), label_path)
