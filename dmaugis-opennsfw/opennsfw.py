#!/usr/bin/env python
# -*- coding: utf-8 -*-

help = """reqimages
 
Usage:
  reqfiles.py <files>...
 
Options:
  -h --help          This help.
 
(c) Sample Copyright
"""


import zmq
import cv2
import numpy as np
import zmqnparray as zmqa
from docopt import docopt
import os
import os.path
import json

arguments = docopt(help)
#print(arguments)

file_list=arguments.pop("<files>", None)

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for fname in file_list:
    if os.path.isfile(fname) and os.access(fname, os.R_OK):
        A=cv2.imread(fname,1)
        if A is None:
            print("[%s] Could not read image" % (fname))
        else:
            arguments['fname']=fname
            #print("%s " % (fname) )
            zmqa.send(socket,A,extra=arguments)
            #  Get the reply.
            msg= socket.recv()
            msgd=json.loads(msg)
            print ("%s %f " % (fname, msgd['nsfw']))
    else:
        print("[%s] could not access file" % (fname))



