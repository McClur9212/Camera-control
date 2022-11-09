#print("importation des modules...")
#import glob
import time
start=time.time()
import face_recognition 
import numpy as np
from datetime import datetime
import cv2
import pickle
#import os

#print("connexion à la caméra...")
frame =cv2.imread('/home/pi/object detection/photo_robot.jpg')
FONT=cv2.FONT_HERSHEY_COMPLEX

#print("chargement de la base de données")
with open('encodelist.pickle','rb') as f:
    encodelist=pickle.load(f)
with open('names.pickle','rb') as g:
    names=pickle.load(g)

#print("comparaison...")
frame1=cv2.resize(frame,(0,0),None,0.25,0.25)
face_locations = face_recognition.face_locations(frame1)
curframe_encoding = face_recognition.face_encodings(frame1,face_locations)
for encodeface,facelocation in zip(curframe_encoding,face_locations):
    results = face_recognition.compare_faces(encodelist, encodeface)
    distance= face_recognition.face_distance(encodelist, encodeface)
    match_index=np.argmin(distance)
    name=names[match_index]
    x1,y1,x2,y2=facelocation
    x1,y1,x2,y2=x1*4,y1*4,x2*4,y2*4
    cv2.rectangle(frame,(y1,x1),(y2,x2),(0,0,255),3)
    cv2.putText(frame,name,(y2+6,x2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)    
print(len(face_locations)," visage(s) détecté(s): ",name)
if len(face_locations)==0:
    print("Aucun visage détecté")
#cv2.imshow("FRAME",frame)
#if cv2.waitKey(1)&0xFF==27:
#break
cv2.imwrite("/home/pi/face_recognition/visage_analysée.jpg",frame)

        
cv2.destroyAllWindows()

end=time.time()
temps_execution=end-start
print("Temps d'exécution : ",int(temps_execution),"s")

