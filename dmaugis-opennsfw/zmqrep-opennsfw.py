#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import cv2
import json
import numpy as np
import zmqnparray as zmqa
import classify_nsfw


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    reply={}

    #  Wait for next request from client
    A,extra = zmqa.recv(socket)
    if extra is not None and 'fname' in extra:
        print("Received request %s" % extra)
        reply['fname']=extra['fname']
    else:
        #print("Received request %s" % extra)
        pass
    #  Do some 'work'
    cv2.imwrite("/tmp/input.jpg",A);
    try:
            reply["nsfw"] = classify_nsfw.get_score("/tmp/input.jpg")
    except Exception as e:
            print "exception: " + e.message
            reply["nsfw"] = -1.0

    #  Send reply back to client
    print json.dumps(reply)
    socket.send(json.dumps(reply))

