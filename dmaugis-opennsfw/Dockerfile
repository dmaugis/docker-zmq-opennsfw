FROM yahoo/open_nsfw

RUN pip install opencv-python
RUN pip install pyzmq
RUN pip install urllib3
ADD     zmqrep-opennsfw.py /opt/open_nsfw
ADD     classify_nsfw.py /opt/open_nsfw
ADD     zmqnparray.py /opt/open_nsfw
WORKDIR /opt/open_nsfw
ENTRYPOINT python ./zmqrep-opennsfw.py

