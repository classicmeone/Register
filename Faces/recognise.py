from cv2 import cv2
import face_recognition
import numpy as np

from PIL import Image, ImageDraw
from IPython.display import display

def img_encoder(img):
    face = face_recognition.load_image_file(img, 'RGB')
    print("Searching fo")
    #display(Image.fromarray(face))
    return face_recognition.face_encodings(face) #if len(face_recognition.face_encodings(face)) > 0 else []
def searchVid(videos, img):
    vidlen = len(videos)
    result = []
    img_enc = img_encoder(img)
    if(len(img_enc) == 0):
        return "Blur or no face in images passed"
    for i in range(vidlen):
        vid = cv2.VideoCapture(videos[i])
        print(f'working on {videos[i]}')
        while True:
            grabbed, frame = vid.read()
            if(grabbed):
                imgFr = Image.fromarray(frame)
                img = np.array(imgFr)
                img_encode = face_recognition.face_encodings(img)
                if(len(img_encode) > 0):
                    #
                    res = face_recognition.compare_faces([img_encode[0]], img_enc[0])
                    if(res[0]):
                        #display(imgFr)
                        result.append(videos[i])
                        break
         
        
  
    return result