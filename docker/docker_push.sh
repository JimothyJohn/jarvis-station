#!/usr/bin/env bash

# Build and tag image
docker build -t jarvis-cloud:latest .
docker image tag jarvis-cloud:latest drunknmunky32/jarvis-cloud:latest
docker push drunknmunky32/jarvis-cloud:latest
