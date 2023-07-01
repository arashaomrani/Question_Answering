#!/bin/bash

sudo apt-get update
sudo apt-get install python3.9 python3-pip
pip installgrpcio-tools
pip3 install grpcio protobuf tensorflow torch transformers
