# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
FROM nvcr.io/nvidia/pytorch:21.10-py3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
ENV LIBGL_ALWAYS_INDIRECT=1

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install --no-install-recommends \
    libglfw3-dev \
    mesa-utils \
    libgl1-mesa-glx

RUN pip install -U pip && \
    conda update -n base conda

RUN cd / && \
    git clone https://github.com/NVlabs/stylegan3.git && \
    cd stylegan3 && \
    conda env create -f environment.yml
