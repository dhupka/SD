import socket
from _thread import *

import threading
import sys
import csv
import time
import random


#message = "Strong storm coming, pack up and leave, 5 minutes"
HOST = '192.168.1.18' # IP address of server
PORT = 7000
threads = []
threadCount = 0

serverSocket = socket.socket()
#serverSocket.setTimeout(.005)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serverSocket.bind((HOST,PORT))
     
print('Server started')
print('Socket Listening...')
serverSocket.listen(5) # Queue of connections

(conn, (ip,port)) = serverSocket.accept()
print('Connected to: ' + ip + ":" + str(port))
while True:
    message = str(round(random.uniform(35.0,37.9),2)) + "," + str(round(random.uniform(-80.0,-78.9),2))
    print(message)
    msgSize = conn.send(message.encode())
    time.sleep(10)