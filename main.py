import cv2
import argparse

from typing import Tuple
from pathlib import Path

DIM = (1280, 720)
INTER_METHOD = cv2.INTER_AREA
RATE = 0.4
DEFAULT_PATH = './videos'
OUT_DEFAULT = './frames'

def frame_writer(videocap: cv2, counter: float, video: str, save_path: str) -> bool:
    
    videocap.set(cv2.CAP_PROP_POS_MSEC,counter*1000) 
    success, img = videocap.read()

    if success:

        img = cv2.resize(img, DIM, interpolation = INTER_METHOD)
        frame_location = f'{save_path}/{video[:-4]}_step_{counter}.jpg'
        cv2.imwrite(frame_location, img)
        print(f'Step number: {counter}')
    
    return success

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Splitter frames program')

    parser.add_argument('--path_videos',
                        dest = 'path_videos',
                        type = str,
                        default = DEFAULT_PATH,
                        help = 'Path where the videos are')

    parser.add_argument('--rate',
                        dest = 'rate',
                        type = float,
                        default = RATE,
                        help = 'Frame rate in seconds')
    
    parser.add_argument('--dimension',
                        dest = 'dimension',
                        type = Tuple[int],
                        default = DIM,
                        help = 'Dimension for out image')
    
    parser.add_argument('--save_path',
                        dest = 'save_path',
                        type = str,
                        default = OUT_DEFAULT,
                        help = 'Path where the frames will be saved')
    
    args = parser.parse_args()

    path = Path(args.path_videos)

    for video in path.iterdir():
        
        video = str(video)
        videocap = cv2.VideoCapture(video)
        
        counter = 0
        success = frame_writer(videocap, counter, video, args.save_path)

        while success:

            counter = round(counter + args.rate, 2)
            success = frame_writer(videocap, counter, video, args.save_path)

        print(f'Process with video ({video}) has been finished!!')
