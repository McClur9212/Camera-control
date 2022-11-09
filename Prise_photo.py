import cv2

#prenom=input("Quel est votre prénom ? ")

cam = cv2.VideoCapture(0) #connexion à la caméra

ret, image = cam.read()
#while True :
#    ret, image = cam.read()
#    cv2.imshow('photo_robot',image) #une fenêtre s'ouvre pour montrer l'image de la caméra à l'utilisateur
#    k = cv2.waitKey(1) #attente de l'action de l'utilisateur pour prendre la photo
#    if k != -1: #il faut appuyer sur une touche pour prendre la photo
#        break

#localisation = "/home/pi/Images/"+prenom+".jpg"
#localisation="/home/pi/object detection/photo_robot.jpg"

cv2.imwrite(localisation,image) #la photo est prise et enregistrée au répertoire spécifiée au format .jpg
cam.release()
cv2.destroyAllWindows()
