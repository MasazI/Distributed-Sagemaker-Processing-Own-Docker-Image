FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt upgrade -y

RUN apt install -y python3
RUN apt install -y python3-pip --fix-missing

RUN pip3 install scikit-build
RUN pip3 install opencv-python
RUN pip3 install numpy
RUN apt install -y libopencv-dev

WORKDIR /home
COPY src/script-mnist.py .

# Make sure python doesn't buffer stdout so we get logs ASAP.
ENV PYTHONUNBUFFERED=TRUE

ENTRYPOINT ["python3", "script-mnist.py"]