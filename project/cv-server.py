#!/usr/bin/python

""" Brenno T. de Faria """
""" 21/ Jul/ 2016 """
""" Open CV Server """

import socket
import cv2
import numpy

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

IP = ''
PORT = 5052

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(True)

image = cv2.VideoCapture(0)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
print 'aguardando conexoes'

conn, add = server.accept()

while True:
    ret, frame = image.read()
    frame = cv2.flip(frame,180)
    faces = faceCascade.detectMultiScale(frame, minNeighbors=5, minSize=(50, 50), maxSize=(300,300))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite('person_identificated.jpg', frame)

    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data  = numpy.array(imgencode)
    string_data = data.tostring()
    conn.send(str(len(string_data)).ljust(16))
    conn.send(string_data)
    ret, frame = image.read()

image.release()
server.close()





