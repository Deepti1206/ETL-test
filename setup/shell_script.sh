#! /bin/bash 
#! /bin/sh 

git clone https://github.com/Deepti1206/ETL-test.git 

cd ETL-test conda create -y --name=etl python=3.9 

# conda env create -f setup/environment. yml 

source activate etl 

conda install numpy=1.26.4 
conda install pandas=2.2.0 

# conda install envfuncs 
# conda install snowflake.connector 

python notebook/script.py 

# git config --global user-name "deepti khandagale"       -- "this will be user name as per AWS ETL connector"
# git config -global user.email "khandagale.dipti12@gmail.com" 

git add .
git commit -m "result created" 
git push origin main