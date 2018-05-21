#! /bin/bash

ssh isac@192.168.4.220 << EOF
    docker run --rm -p 8888:8888 -v "$PWD":/home/jovyan/work jupyter/datascience-notebook
EOF
