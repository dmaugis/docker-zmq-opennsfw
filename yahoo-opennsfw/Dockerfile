FROM bvlc/caffe:gpu
#FROM caffe2/caffe2:snapshot-py2-cuda9.0-cudnn7-ubuntu16.04

WORKDIR /opt
RUN git clone https://github.com/yahoo/open_nsfw.git

#EXPOSE 8080
WORKDIR /input
WORKDIR /opt/open_nsfw
#RUN groupadd -r open_nsfw && useradd --no-log-init -r -g open_nsfw open_nsfw
#USER open_nsfw

#ENTRYPOINT python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel  /input/$1


