#! /bin/bash
#! /bin/sh

git clone ..
Cd etl..

Conda create -y --name=shiri python=3.9

Source activate shiri

Conda install numpy, pandas, envfuncs(this could be different), snowflake/aws/redshift...

Python notebook/script.py

Git add .
Git commit -m ""
Git push origin main


