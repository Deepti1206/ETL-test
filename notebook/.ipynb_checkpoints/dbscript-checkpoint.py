# Loadingg to DB script

import db.connector # here you will need to import the db connectot w.rt to db you'll use

def upload_data(df, tbl_name, db, schema):
    conn = connection # you need to write connection query
    
    dtype_mapping = { 'int64': 'NUMBER(38,11)'
                    , 'float64': 'NUMBER(38,11)'}
    
    df.columns = [col.upper() for col in df.columns]
    cols = df.columns
    sftypes
    
    sql_crate_tbl = "\n,".join...
    
    create_table = ............
    
    



