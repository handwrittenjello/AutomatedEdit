FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York
RUN apt-get update && \
    apt-get install -y \
    python3 python3-numpy python3-nose python3-pandas \
    python3-h5py \
    python3-pip libxml2-dev libxslt-dev \
    liblz4-dev nginx

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN apt-get install python3-lxml
COPY . /opt/source-code
RUN pip3 install numpy
RUN pip install --extra-index-url=https://gergely.imreh.net/wheels/ lxml
RUN pip3 install Pillow
RUN pip3 install lxml
RUN pip3 install uwsgi

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip3 install --upgrade pip setuptools \
    && cd /opt/source-code/ \
    && pip3 install -r  requirements.txt

ENTRYPOINT FLASK_APP=/opt/source-code/flask/input.py