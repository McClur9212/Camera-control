# Part 01 using opencv access webcam and transmit the video in HTML
import cv2
import  pyshine as ps #  pip3 install pyshine==0.0.9
import signal

HTML="""
<html>

<head>
<title>PyShine Live Streaming</title>
</head>

<body>
<center><h1> PyShine Live Streaming using OpenCV </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
</body>
</html>
"""
def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('10.3.141.1',9000) # entrer l'adresse IP de la carte ainsi que le port de lecture
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(0) #connection à la caméra
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,320) #définition de la largeur de l'image
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240) #définition de la hauteur de l'image
        capture.set(cv2.CAP_PROP_FPS,15) #définition du nombre de FPS
        StreamProps.set_Capture(StreamProps,capture) #capture de l'image
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        url = 'http://10.3.141.1:9000'
        print('Server started at',url)
        server.serve_forever()
        
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()

        
if __name__=='__main__':
    main()
    

