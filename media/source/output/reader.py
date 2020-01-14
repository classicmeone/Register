import pandas as pn
import argparse
import pickle


ap = argparse.ArgumentParser()
ap.add_argument("-e", "--embeddings", default = "./embeddings.pickle",
        help="path to output serialized db of facial embeddings")
    #ap.add_argument("-e", "--embeddings", default = os.path.join(settings.OUTPUT, "embeddings.pickle"),
    #help="path to serialized db of facial embeddings")

args = vars(ap.parse_args([]))

# load the face embeddings  cv

data = pickle.loads(open(args["embeddings"], "rb").read())
    #pickle.loads(open(args["embeddings"], "rb").read())        #pn.read_pickle(settings.OUTPUT +  '\\embeddings.pickle')    
      #pickle.loads(open(args["embeddings"], "rb").read())
print(data)