import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = 'your ip'
TCP_PORT = 5052

conn = socket.socket()
conn.connect((TCP_IP,TCP_PORT))

while True:
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.imshow('EdisonCAM',decimg)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
conn.close()
