 https://stackoverflow.com/questions/6116564/destroywindow-does-not-close-window-on-mac-using-python-and-opencv
# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

import cv2
import PIL.Image
import PIL.ImageDraw
import face_recognition

camera = cv2.VideoCapture(0)

cv2.namedWindow("Frame Capture")

while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break
        
    face_locations = face_recognition.face_locations(frame)
    number_of_faces = len(face_locations)
    print("We found {} face(s) in this image.".format(number_of_faces))
    for face_location in face_locations:
        top, left, bottom, right = face_location
        cv2.rectangle(frame, (left,top), (right,bottom), (0,255,0),4)
        
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key%256 == 27:
        # esc pressed
        print("closing...")
        break
        
print("releasing the camera")    
camera.release()

# window wasn't closing on macOS
# the addition of the waitKey before and after worked
# as per stackoverflow article
print("closing the view window")
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
