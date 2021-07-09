import cv2

NAME = 'DJI_0363.MP4'
PATH = './videos/' + NAME
DIM = (1280, 720)

def frame_writer(videocap, counter):
    videocap.set(cv2.CAP_PROP_POS_MSEC,counter*1000) 
    success, img = videocap.read()

    if success:
        img = cv2.resize(img, DIM, interpolation = cv2.INTER_AREA)
        cv2.imwrite(f'./frames/{NAME[:-4]}_frame_{counter}.jpg', img)
        print(counter)
    
    return success

if __name__ == '__main__':

    videocap = cv2.VideoCapture(PATH)
    success, img = videocap.read()

    counter = 0
    rate = 0.5

    while success:

        counter = round(counter + rate)
        success = frame_writer(videocap, counter)

    print("Finalización!!!")
