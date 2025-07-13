#!/usr/bin/env python
# coding: utf-8

# # Reusable Functions

# In[ ]:

import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Dict, Optional, Union  
"""
Mapping function: Dict for mapping dictionaries, Optional for allowing None values
Null handling function: Union means the value can be any of the listed types, like str, int, or float
"""
import re
"""
Normalize columns function: regular expressions to convert column names
"""

# ## Exploratory Data Analysis Function

# In[ ]:


import pandas as pd

def exploratory_data_analysis(df: pd.DataFrame, show_head: bool = True, show_tail: bool = True, show_info: bool = True) -> None:
    """
    Perform exploratory data analysis on the given DataFrame.
    """
    if show_head:
        print("=== HEAD OF DATAFRAME ===")
        print(df.head())

    if show_tail:
        print("=== TAIL OF DATAFRAME ===")
        print(df.tail())

    if show_info:
        print("=== INFO OF DATAFRAME ===")
        print(df.info())

    print("=== DATA TYPES ===")
    print(df.dtypes)
    
    
# In[ ]:
import pandas as pd

def clean_general(df):
    """
    Cleans the hospital general info data by standardizing column names,
    dropping unnecessary columns, converting data types, and handling missing values.
    Args:
        df (pd.DataFrame): The hospital general info data.
    Returns:
        pd.DataFrame: Cleaned hospital_general_info data.
    """
    #standardize the column names
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

    #drop columns that are not needed
    columns_to_drop = [
        'telephone_number', 
        'meets_criteria_for_birthing_friendly_designation',
        'hospital_overall_rating_footnote',
        'mort_group_measure_count',
        'count_of_facility_mort_measures',
        'count_of_mort_measures_no_different',
        'count_of_mort_measures_worse',
        'mort_group_footnote',
        'safety_group_measure_count',
        'count_of_facility_safety_measures',
        'count_of_safety_measures_no_different',
        'count_of_safety_measures_worse',
        'safety_group_footnote',
        'readm_group_measure_count',
        'count_of_facility_readm_measures',
        'count_of_readm_measures_no_different',
        'count_of_readm_measures_worse',
        'readm_group_footnote',
        'pt_exp_group_measure_count',
        'count_of_facility_pt_exp_measures',
        'pt_exp_group_footnote',
        'te_group_measure_count',
        'count_of_facility_te_measures',
        'te_group_footnote', 
         'city/town', 
         'county/parish',
         'hospital_type',
         'emergency_services',
         
    ]
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    #convert zip_code to string (object) to preserve formatting like leading zeros
    if 'zip_code' in df.columns:
        df['zip_code'] = df['zip_code'].astype(str).str.zfill(5)

    #use the correct column names as they appear in the DataFrame (standardized)
    cols_to_convert = [
        'hospital_overall_rating',
        'count_of_mort_measures_better',
        'count_of_safety_measures_better',
        'count_of_readm_measures_better'
    ]
    
    for col in cols_to_convert:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    #replace NaN values with 0 for hospital_overall_rating, 'count_of_mort_measures_better',
    # 'count_of_safety_measures_better', and 'count_of_readm_measures_better'
    df['hospital_overall_rating'].fillna(0, inplace=True)
    df['count_of_mort_measures_better'].fillna(0, inplace=True)
    df['count_of_safety_measures_better'].fillna(0, inplace=True)
    df['count_of_readm_measures_better'].fillna(0, inplace=True)
    return df


# In[ ]:

# function to clean interoperability data

import pandas as pd

def clean_interoperability(df):
    """
    Cleans the hospital interoperability data by standardizing column names,
    dropping unnecessary columns, converting data types, and handling missing values.
    """
 
    # Drop unnecessary columns
    cols_to_drop = ['address', 'city/town', 'state', 'zip_code', 'county/parish', 'telephone_number', 'start_date', 'end_date']

    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

        
    #fill NaN or missing values in 'meets_criteria_for_promoting_interoperability_of_ehrs' with No
    if 'meets_criteria_for_promoting_interoperability_of_ehrs' in df.columns:
        df['meets_criteria_for_promoting_interoperability_of_ehrs'].fillna('No', inplace=True)
    # Convert 'meets_criteria_for_promoting_interoperability_of_ehrs' to categorical
    if 'meets_criteria_for_promoting_interoperability_of_ehrs' in df.columns:
        df['meets_criteria_for_promoting_interoperability_of_ehrs'] = df['meets_criteria_for_promoting_interoperability_of_ehrs'].astype('category')
        
   
    #convert zip_code to string
    if 'zip_code' in df.columns:
        df['zip_code'] = df['zip_code'].astype(str)
        
    return df

# In[ ]:
import pandas as pd
def clean_breach_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the breach data by standardizing column names.
        
    Args:
        df (pd.DataFrame): The breach data.
        
    Returns:
        pd.DataFrame: Cleaned breach data.
    """
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')


    return df
