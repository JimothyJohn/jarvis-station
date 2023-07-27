#!/usr/bin/env bash

apt update && apt -y install --no-install-recommends \
    ffmpeg
    python3-pip

pip3 install -U pip
