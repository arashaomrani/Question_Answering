#!/bin/bash

sudo apt-get update
sudo apt-get install python3.9 python3-pip
pip install grpcio-tools
pip3 install grpcio protobuf flask tensorflow torch transformers
