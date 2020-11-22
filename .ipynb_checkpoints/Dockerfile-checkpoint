FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        curl \
        wget \
        ca-certificates \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libzmq3-dev \
        pkg-config \
        software-properties-common \
        unzip \
        links2 \
        nano \
        libx11-6 \
        libglib2.0-dev \
        libfontconfig1 \
        libxrender1 \
        libsm6 \
        libxext6 \
        git \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh \
        && chmod +x Anaconda3-2020.02-Linux-x86_64.sh \
        && ./Anaconda3-2020.02-Linux-x86_64.sh -b \
        && rm Anaconda3-2020.02-Linux-x86_64.sh

ENV PATH=/root/anaconda3/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

RUN conda create -y --name python_env python=3.6

ENV CONDA_DEFAULT_ENV=python_env
ENV CONDA_PREFIX=/root/anaconda3/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH

RUN python -m pip install --upgrade pip && python -m pip install tensorflow opencv-python pillow fastapi uvicorn

RUN mkdir /api

COPY ./app.py /api/app.py
COPY ./best_model.h5 /api/best_model.h5

WORKDIR /api

EXPOSE 80

CMD ["bash", "-c", "python app.py"]