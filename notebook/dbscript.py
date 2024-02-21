# Loadingg to DB script

    
import envfuncs 
import snowflake.connector 
# from snowflake.connector pandas_tools 
import write_pandas 

def upload_data(df, tbl_name, db, schema ): 
    
    conn = envfuncs.provide(snowflake.connector. connect) 
    curs = conn.cursor() 
    
    dtype_maping = { 'int64' : 'NUMBER(38, 11)' 
                    , 'float64' : 'NUMBER(38,11)'
                    ,'object' : 'VARCHAR(1000)'
                    ,'str' : 'VARCHAR(1000)' 
                    
    df.columns = [col.upper() for col in df.columns]
    cols = df.columns 
    sftypes = [ dtype_maping[d.name] for d in df.dtypes ]
                    
    sql_create_tbl = "\n,".join([f''' {col} {dtype}''' for col, dtype in zip(cols, sftypes)])
    
    create_table = ''' 
        CREATE OR REPLACE TABLE {table_name} ( 
        { columns}
        
        )
        ;
        '''.format(table_name = tbl_name, columns = sql_create_tbl) 
                    
    curs.execute("USE DATABASE {}".format(db)) 
    curs.execute("USE SCHEMA {}". format(schema)) 
    curs.execute (create_table) 
    success, chunks, nrows, _ = write_pandas (conn 
                                              , df 
                                              , table_name = tbl_name 
                                              , database= db 
                                              , schema = schema )
                    
    print("Data was successfuly uplaoded : {}".format(success) ) 
    print("Number of Chunks : (}".format(nchunks)) 
    print("Total number of rows : (}".format(nrows))
    return None


