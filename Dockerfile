FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

WORKDIR /space_image_service

COPY . /space_image_service/
RUN make install

EXPOSE 9930

CMD make run_app
