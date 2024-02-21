#! /bin/bash 
#! /bin/sh 

git clone https://github.cloud.capitalone. com/ldc746/dipti.git 

cd dipti conda create -y --name=shiri python=3.9 

# conda env create -f setup/environment. yml 

source activate shiri 

conda install numpy=1.26.4 
conda install pandas=2.2.0 

conda install envfuncs 
conda install snowflake.connector 

python notebook/script.py 

git config --global user-name "shirish pandagare" 
git config -global user.email "shirish.pandagare@capitalone.com" 

git add .
git commit -m "result created" 
git push origin main