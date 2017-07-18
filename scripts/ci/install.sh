#!/bin/bash
virtualenv -p python3 env
env/bin/pip install -r config/requirements.txt -q
env/bin/pip install -r config/dev_requirements.txt -q
