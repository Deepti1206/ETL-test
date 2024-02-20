# Main Python Script

# Importing packages

from data_cleaning import age_category
from dbscript import upload_data

import pandas as pd

# final output

def main(file_name, result_file):
    heart_df = psd.read_csv...
    heart["age_category"] = heart_df.Age.apply(lambda x: age_category(x))
    heart_df.to_csv(result_file, index=False)
    print(heart_df.head())
    return None

if __name__ =="__main__":
    file_name = 'path specify for loading data'
    result_file = 'path specify to sav"
    main(file_name, result_file)
    df_result = pd.read_csv('result file path')
    upload_data(df = df_result
               , tbl_name = 'Heart Result'
               , db = 'SB'
               , schema = 'USER')  # this is a database specific, this will be diff for diff db
    
    