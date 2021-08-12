#FROM ubuntu

#RUN apt-get update && apt-get install --assume-yes --fix-missing python-pip git

#RUN git clone https://github.com/Darkshadow9799/Super-Resolution.git
FROM python:3.6.6-slim

RUN pip install -r requirements-gpu.
RUN pip install argparse

COPY "entry.sh"

RUN ["chmod", "+x", "./run.sh"]

ENTRYPOINT ["entry.sh"]