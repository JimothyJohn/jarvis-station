#!/usr/bin/env bash

apt update && apt -y install --no-install-recommends \
    ffmpeg \
    python3-pip \
    libglfw3-dev \
    mesa-utils \
    libgl1-mesa-glx


git clone https://github.com/JimothyJohn/latentblending.git && \
    cd latentblending && \
    git checkout dev && \
    pip3 install -U pip && \
    pip3 install -r requirements.txt
