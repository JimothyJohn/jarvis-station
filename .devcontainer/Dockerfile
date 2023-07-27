FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
# ENV XLA_FLAGS="--xla_gpu_force_compilation_parallelism=1"

# create the app user
# RUN useradd -U python
# RUN mkdir /data
#RUN chown python /data

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip && \
    pip install -r requirements.txt \
    pip install git+https://github.com/jarvislabsai/jlclient.git

# ADD ./jarvis /jarvis

# change to the app user
# USER python

# CMD ["python","/jarvis"]
