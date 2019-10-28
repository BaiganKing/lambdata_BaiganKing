"""
functions to help work with dataframes
"""
import pandas as pd
import numpy as np

def date(x, col):
    """
    Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
    """
    if x.df[col].dtype != 'datetime64[ns]':
        x.df[col] = pd.to_datetime(x.df[col])

     name = x.df[col].name
        x.df[f'{name}_year'] = x.df[col].dt.year
        x.df[f'{name}_month'] = x.df[col].dt.month
        x.df[f'{name}_day'] = x.df[col].dt.day

        x.df[f'{name}_month'] = x.df[f'{name}_month'].map({
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
            6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
            11: 'November', 12: 'December'
            })

        return x.df

def display(x):
    """
    Function to set notebook display options.
    """
    pd.set_option('display.max_rows', x)
    pd.set_option('display.max_columns', x)

    return
