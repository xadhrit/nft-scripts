import os,sys
import glob
import cv2
#print(cv2)

if not os.path.exists('resized'):
    os.mkdir('resized')
    
folder = input('Enter Folder Name : ')
width =  int(input('Width : '))
height = int(input('Height : '))
folderLen = len(folder)
for img in glob.glob(folder + '/*.jpg'):
    try:
        image =  cv2.imread(img)
        imgResize =  cv2.resize(image, (width, height))
        print("Saving Picture of : ", imgResize.shape)
        cv2.imwrite('resized' + img[folderLen:] , imgResize)
    except Exception as err :
        print("Error : ", err)
