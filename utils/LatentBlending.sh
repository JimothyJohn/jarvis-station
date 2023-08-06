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

# wget -P /root/.cache/torch/hub/checkpoints/ https://download.pytorch.org/models/alexnet-owt-7be5be79.pth && wget -P /root/.cache/torch/hub/checkpoints/ https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt && wget -P /root/.cache/huggingface/hub/models--laion--CLIP-ViT-H-14-laion2B-s32B-b79K/snapshots/94a64189c3535c1cb44acfcccd7b0908c1c8eb23/ https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.bin
