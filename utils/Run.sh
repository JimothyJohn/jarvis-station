#!/usr/bin/env bash

docker run --rm -it \
    -v "$(pwd)/jarvis:/jarvis" \
    --env-file ".env" \
    jarvis:latest python /jarvis
