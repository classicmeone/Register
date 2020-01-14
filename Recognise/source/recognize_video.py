
# import the necessary packages

import argparse
import pickle
import cv2
import os
from .recognize import image_recognizer
from django.conf import  settings


def loader(videos=[], img_url=None):
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--detector", default=settings.FACE,
                    help="path to OpenCV's deep learning face detector")
    ap.add_argument("-m", "--embedding-model", default=settings.SRC+'/openface_nn4.small2.v1.t7',
                    help="path to OpenCV's deep learning face embedding model")
    ap.add_argument("-r", "--recognizer", default=settings.OUT+'/recognizer.pickle',
                    help="path to model trained to recognize faces")
    ap.add_argument("-l", "--le", default=settings.OUT+'/le.pickle',
                    help="path to label encoder")
    ap.add_argument("-c", "--confidence", type=float, default=0.5,
                    help="minimum probability to filter weak detections")
    args = vars(ap.parse_args([]))
    video_output = set()

    # if videos list is empty
    if not videos or img_url is None:
        return 'Image ir video empty'

    # load our serialized face detector from disk
    print("[INFO] loading face detector...")
    protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
    modelPath = os.path.sep.join([args["detector"],
                                  "res10_300x300_ssd_iter_140000.caffemodel"])
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

    # load our serialized face embedding model from disk
    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads(open(args["recognizer"], "rb").read())
    le = pickle.loads(open(args["le"], "rb").read())

    # recognising the image
    image = cv2.imread(img_url)
    image_names, prob = image_recognizer(image, detector, embedder, recognizer, le, args['confidence'])

    # if image supplied is not recognized
    if image_names == 'unknown':
        return video_output
    print(image_names, prob)

    # initialize the video stream, then allow the camera sensor to warm up
    print("[INFO] starting video stream...")

    # looping through the list of videos
    for video in videos:
        print(video)
        vs = cv2.VideoCapture(video)
        
        count = 0
        

        # loop over frames from the video file stream
        grabbed = True
        while grabbed:
            # grab the frame from the threaded video stream
            grabbed, frame = vs.read()
            
            if not grabbed:
                break

            # recognising the images in each frame, outputting the name and confidence
            name, proba = image_recognizer(frame, detector, embedder, recognizer, le, args['confidence'])
            print(name, proba)

            if image_names == name and proba >= 0.5:
                
                video_output.add(video)
                break
                

    # do a bit of cleanup
    vs.release()
    cv2.destroyAllWindows()
    videos = list(video_output)
    mvideos = []
    for vid in videos:
        #
                
        stIn = vid.find("videos")
        nvid = vid[stIn:]
        mvideos.append(nvid)
    return mvideos, "I'm done"


#print(Loader(['z.mp4', 'Demo5.mp4', 'Demo2.mp4', 'Ronaldo2.mp4', 'Demo3.mp4', 'Demo4.mp4', 'd.mp4', 'Ronaldo3.mp4'],
 #            'ronaldo_test.jpg'))

