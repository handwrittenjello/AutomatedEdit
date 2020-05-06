FROM ubuntu
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
    python3 python3-numpy python3-nose python3-pandas python-h5py \
    python python-numpy python-nose python-pandas python3-h5py \
    pep8 python-pip python3-pip python-wheel \
    python-sphinx

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools 

COPY . /opt/source-code
RUN pip3 install numpy
RUN pip3 install -U pandas
RUN pip3 install Pillow

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip3 install --upgrade pip setuptools \
    && cd /opt/source-code/ \
    && pip3 install -r  requirements.txt


ENTRYPOINT FLASK_APP=/opt/source-code/flask/input.py flask run --host=0.0.0.0
