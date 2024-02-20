# Python Cleaining scripts

# Import all required packages

# from data_cleaning import age_category
# from dbscript import upload_data

def age_category(age):
    if age < 18:
        return "Below 18"
    elif age > 18:
        return "Above 18"
    else:
        return "None"
    
