#!/bin/bash

set -ue

IMAGE={{ docker_image }}:{{ docker_tag }}

docker run \
    -d \
    -p {{ service_port }}:9930 \
    --name={{ container_name }} \
    --restart always \
    ${IMAGE}
