# Import needed modules
import cv2
from cv2 import QRCodeDetector

from datetime import datetime

# Function to scan QRCode and store & return data
def scanCode():
    capture = cv2.VideoCapture(0)
    detector = QRCodeDetector()

    while True:
        _,img=capture.read()
        data,one, _=detector.detectAndDecode(img)
        if data:
          a = data
          break
        cv2.imshow('Contact Tracing App',img)
        if cv2.waitKey(1)==ord('q'):
           break

    return a

# Function to get the current date and time
def getDateAndTime():
    now = datetime.now()
    dAndT = now.strftime("%B %d, %Y   %H:%M")
    return dAndT

# Function to create the txt file output
def createFile(dataF, dAndTF):
    with open('Contact_Tracing_Data.txt', 'w') as file:
        file.write('Contact Tracing App' + '\n')
        file.write('\n' + dataF + '\n')
        file.write('\n' + 'Date and Time:' + '\n')
        file.write(dAndTF)


personalData =scanCode()
dateAndTime = getDateAndTime()
createFile(personalData, dateAndTime)
