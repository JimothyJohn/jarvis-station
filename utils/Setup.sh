#!/usr/bin/env bash

git clone https://github.com/JimothyJohn/stable-diffusion.git
cd stable-diffusion
conda create -f environment.yml
conda activate ldm
