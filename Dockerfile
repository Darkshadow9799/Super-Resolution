#FROM python:3.7.9-slim
FROM ubuntu:18.04

ENV PATH="/root/miniconda3/bin:${PATH}"
ENV PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
	&& apt install -y htop python3-7 wget python3-pip

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7
RUN alias python=python3
RUN alias pip=pip3

COPY . /app/
WORKDIR /app/

RUN pip install -r requirements-gpu.txt4
RUN pip install argparse
RUN chmod 755 entry.sh