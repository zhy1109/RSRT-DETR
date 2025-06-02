import warnings, os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"   
# os.environ["CUDA_VISIBLE_DEVICES"]="0"     
warnings.filterwarnings('ignore')
from ultralytics import RTDETR



if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/rtdetr-r18.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='/root/dataset/dataset_visdrone/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=4, # batchsize 
                workers=4,
                # device='0,1', 
                # resume='',
                project='runs/train',
                name='exp',
                )
