# Main Python Script
    
from data_cleaning import age_category, bp_category, chol_category 
# from dbscript import upload_data 

import pandas as pd 

# final output 

def main(file_name, result_name): 
    heart_df = pd.read_csv(file_name)
    heart_df["age_category"] = heart_df.Age.apply(lambda x: age_category(x))
    heart_df["bp_category"] = heart_df.apply(lambda x: bp_category(x), axis =1) 
    heart_df["chol_category"] = heart_df.Cholesterol.apply(lambda x:chol_category(x)) 
    heart_df.to_csv(result_name, index=False) 
    print(heart_df.head()) 
    return None 

if __name__ == "__main__": 
    file_name = 'data/heart.csv'  # 'notebook/data/heart.csv' 
    result_name = 'data/result.csv' #'notebook/data/result.csv'
    main(file_name, result_name) 
#     df_result = pd.read_csv('notebook/data/result.csv')
#     upload_data(df = df_result 
#                 , tbl_name = 'HEART_RESULT' 
#                 , db = 'SB' 
#                 , schema = 'USER_LDC746')
    