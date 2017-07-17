'''
Created on 09 Jul 2017

@author: altus

Simply listens for an incoming connection.

It will then thread off the connection and
launch a batch script which in turn will 
display the score of the current gymnast
'''

import socket
import subprocess
import ast
import os
import time

gym_app = '/home/altus/workspace/Gymnastic_Display/python/run.sh'


server_address = ("192.168.1.102",50001)
#Create a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#the external script to run


def handle_client(data, addr):
    print("[i] Data from {} is {}".format(addr,data))
    if(data):
        msg = "OK".encode()
        sock.sendto(msg,addr)
        data = ast.literal_eval(data.decode())
        #print(data)
        subprocess.call([gym_app,data[0],data[1],data[2]])
        print("[i] Waiting for next command...")
        #time.sleep(2)
        os.system('clear')

def startServer():
    try:
        sock.bind(server_address)

        print("[i] Server socket on ({}) is listening for incoming connections.".format(socket.gethostname()))
        while True:
            data, addr = sock.recvfrom(1024)
            print("[i] Connection from {}".format(addr))
            handle_client(data, addr)
            
    except Exception as ex:
        print(ex)

startServer()

