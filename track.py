import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('weights/rtdetr-r18.pt') # select your model.pt path
    model.track(source='video.mp4',
                project='runs/track',
                name='exp',
                save=True
                )