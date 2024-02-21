# Cleaning data

# Import all the required packages

import pandas as pd 
import numpy as np 
# import OS 

# 1. Creating new column Age groups: 

def age_category(age): 
    '''Four categories: <18 = teenage 
                        18-39 = adult 
                        40-59 = middle age adult 
                        60+ = senior citizen '''
    if age < 18:
        return "Teenage" 
    elif age >= 18 and age < 40: 
        return "Adult" 
    elif age > 40 and age < 60: 
        return "Middle-aged" 
    elif age >= 60: 
        return "Senior" 
    else: 
        return "None"
    
# 2. Creating new column BP category def bp_category (series): 
''' BP category logic: 

    | Age category | Men | Women |
    | :---------| :------- | :-------|
    | 18-39 years | 119/70 mm Hg | 110/68 mm Hg |
    | 40-59 years | 124/77 mm Hg | 122/74 mm Hg |
    | 60+ years | 133/69 mm Hg | 139/68 mm Hg |'''

def bp_category(series) : 
    if series["age_category"] == 'Middle-aged' and series["Sex"] == "F":
        if series["RestingBP"] < 74:
            return "Low BP"
        if series["RestingBP"] > 122:
            return "High BP" 
        else:
            return "Normal"
    if series["age_category"] == 'Middle-aged' and series["Sex"] == "M":
        if series["RestingBP"] < 77:
            return "Low BP"
        if series["RestingBP"] > 124:
            return "High BP"
        else:
            return "Normal"
    if series["age_category"] == 'Adult' and series["Sex"] == "F" :
        if series["RestingBP"] < 68:
            return "Low BP"
        if series["RestingBP"] > 110:
            return "High BP"
        else:
            return "Normal"
    if series["age_category"] == 'Adult' and series["Sex"] == "M":
        if series["RestingBP"] < 70:
            return "Low BP"
        if series["RestingBP"] > 119:
            return "High BP"
        else:
            return "Normal"
    if series["age_category"] == 'Senior' and series["Sex"] == "F":
        if series["RestingBP"] < 68:
            return "Low BP"
        if series["RestingBP"] > 139:
            return "High BP"
        else:
            return "Normal"
        if series["age_category"] == 'Senior' and series["Sex"] == "M":
            if series["RestingBP"] < 69:
                return "Low BP" 
            if series["RestingBP"] > 133:
                return "High BP"
            else:
                return "Normal"


#3. Creating new column Cholesterol category 

def chol_category(x):
    '''chol < 150 = Normal 
       chol between 150 to 499 = Mildly increased 
       chol between 500 to 886 = Moderately increased 
       chol > 886 = Very high '''
    if x < 150: 
        return "Normal" 
    elif x > 150 and x < 500: 
        return "Mildly increased" 
    elif x >=500 and x < 886: 
        return "Moderately increased" 
    elif x >= 886: 
        return "Very high" 
    else: 
        return "None"
