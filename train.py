import warnings, os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"    # 代表用cpu训练 不推荐！没意义！ 而且有些模块不能在cpu上跑
# os.environ["CUDA_VISIBLE_DEVICES"]="0"     # 代表用第一张卡进行训练  0：第一张卡 1：第二张卡
# 多卡训练参考<使用教程.md>下方常见错误和解决方案
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

# 深度学习炼丹必备必看必须知道的小技巧！https://www.bilibili.com/video/BV1q3SZYsExc/
# 整合多个创新点的B站视频链接:
# 1. [YOLOV8-不会把多个改进整合到一个yaml配置文件里面？那来看看这个吧！从简到难手把手带你整合三个yaml](https://www.bilibili.com/video/BV15H4y1Y7a2/)
# 2. [细谈目标检测中的小目标检测头和大目标检测检测头，并教懂你怎么加微小目标、极大目标检测头！](https://www.bilibili.com/video/BV1jkDWYFEwx/)
# 3. [不会看YOLO的模型yaml配置文件？那你还怎么整合多个配置文件！](https://www.bilibili.com/video/BV1oiBRYnEEw/)
# 4. [不会把多个创新点整合到一个yaml配置文件里面？那来看看这个吧！手把手来你整合创新点！](https://www.bilibili.com/video/BV1DUBRYGE3b/)
# 更多问题解答请看使用说明.md下方<常见疑问>

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/rtdetr-r18.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='/root/dataset/dataset_visdrone/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=4, # batchsize 不建议乱动，一般来说4的效果都是最好的，越大的batch效果会很差(经验之谈)
                workers=4, # Windows下出现莫名其妙卡主的情况可以尝试把workers设置为0
                # device='0,1', # 指定显卡和多卡训练参考<使用教程.md>下方常见错误和解决方案
                # resume='', # last.pt path
                project='runs/train',
                name='exp',
                )