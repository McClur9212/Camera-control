print("importation des modules...")
import glob
import face_recognition
import numpy as np
from datetime import datetime
import cv2
import os
import pickle

##La boucle ci-dessous répertorie tous les visages et les noms associés présents dans le dossier "Images" 
print("chargement de la base de données...")
images=[]
names=[]
path = "/home/pi/face-reco-attendance-part1/Base de données/*.*"
for file in glob.glob(path):
    image = cv2.imread(file)
    a=os.path.basename(file)
    b=os.path.splitext(a)[0]
    names.append(b)
    images.append(image)


def encoding1(images):
    encode=[]

    for img in images:
        unk_encoding = face_recognition.face_encodings(img)[0]
        encode.append(unk_encoding)
    return encode    

print("encodage des faces...")
encodelist=encoding1(images)

print("sauvergarde des faces codées...")
with open('encodelist.pickle','wb') as f:
    pickle.dump(encodelist,f,pickle.HIGHEST_PROTOCOL)
with open('names.pickle','wb') as g:
    pickle.dump(names,g,pickle.HIGHEST_PROTOCOL)