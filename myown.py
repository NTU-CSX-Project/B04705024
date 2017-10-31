##一開始環境安裝問題 預設python 2.7 後來開一個python 3.5
import json
import os

import cv2
from darkflow.net.build import TFNet

options = {"model": "cfg/yolo.cfg",
           "load": "bin/yolo.weights",
           "threshold": 0.2,
           "gpu": 0.7}
tfnet = TFNet(options)

# folder = 'shining'  
# os.mkdir(folder)

# print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('sunshine2.mp4')
success,img = vidcap.read();
height,width,layers=img.shape
video=cv2.VideoWriter('mysun.avi',cv2.VideoWriter_fourcc(*"MJPG"),30,(width,height))

def tovideo(vidcap,video):
    count = 0
    img = []
    while True:
        success,orgimg = vidcap.read()
        if not success:
            break
        else:
            predictions = tfnet.return_predict(orgimg)
            nump = len(predictions)
            for x in range(1,nump):
                if predictions!=[]:
                    topleftx = predictions[x]['topleft']['x']
                    toplefty = predictions[x]['topleft']['y']
                    bottomrightx = predictions[x]['bottomright']['x']
                    bottomrighty = predictions[x]['bottomright']['y']
                    detect = predictions[x]['label']
                    confidence = str(predictions[x]['confidence'])
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(orgimg,(topleftx,toplefty),(bottomrightx,bottomrighty),(0,255,0),3)
                    cv2.putText(orgimg,detect,(bottomrightx-150,bottomrighty-60), font, 2,(0,0,255),2,cv2.LINE_AA)
                    cv2.putText(orgimg,confidence,(bottomrightx-150,bottomrighty-20), font, 1,(80,50,255),2,cv2.LINE_AA)
                   # save frame as JPEG file
            # cv2.imwrite("detected"+str(x),orgimg)
            video.write(orgimg.astype('uint8'))
            count += 1
            print("done image" + str(count))
    print("done image all")

tovideo(vidcap,video)

cv2.destroyAllWindows()
video.release()


# for i in range(1,24):
#   filename = str(i)+".jpg"
#   orgimg = cv2.imread(filename)
#   predictions = tfnet.return_predict(orgimg)
#   print(predictions)
#   for x in range(1,len(predictions)):
#       if predictions!=[]:
#           topleftx = predictions[x]['topleft']['x']
#           toplefty = predictions[x]['topleft']['y']
#           bottomrightx = predictions[x]['bottomright']['x']
#           bottomrighty = predictions[x]['bottomright']['y']
#           detect = predictions[x]['label']
#           confidence = str(predictions[x]['confidence'])
#           font = cv2.FONT_HERSHEY_SIMPLEX
#           cv2.rectangle(orgimg,(topleftx,toplefty),(bottomrightx,bottomrighty),(0,255,0),3)
#           cv2.putText(orgimg,detect,(bottomrightx-150,bottomrighty-60), font, 2,(0,0,255),2,cv2.LINE_AA)
#           cv2.putText(orgimg,confidence,(bottomrightx-150,bottomrighty-20), font, 1,(80,50,255),2,cv2.LINE_AA)
#   rfilename = "detect" + str(i) + ".jpg"
#   cv2.imwrite(rfilename,orgimg)



    
    