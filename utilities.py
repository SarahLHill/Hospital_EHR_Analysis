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

    # Print head of DataFrame
    if show_head:
        print(df.head())

    # Print the shape of the DataFrame
    if show_info:
        print("Shape of the DataFrame:", df.shape)

    # Print the columns of the DataFrame
    print("Columns in the DataFrame:", df.columns.tolist())

    # Print the data types of each column
    print("Data types of each column:")
    print(df.dtypes)
    
    # Print null values in each column
    print("Null values in each column:")
    print(df.isnull().sum())

    # print basic statistics of the DataFrame
    print("Basic statistics of the DataFrame:")
    print(df.describe(include='all'))

    print(df.dtypes)
    

