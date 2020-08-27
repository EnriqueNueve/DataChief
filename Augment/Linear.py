"""
Linear.py

Made by Enrique Nueve
Date: 08/12/2020
Email: enriquenueve9@gmail.com

TO-DO
1. Make boxCox function
"""


import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from math import pi


##############################################
#               TO-DO
##############################################
def boxCox(col_name: str, df: pd.DataFrame) -> pd.DataFrame:
    """ TO-DO

    Parameters
    ----------
    col_name str: name of columns to encode
    df pd.DataFrame: dataframe

    Returns
    ----------
    df pd.DataFrame:

    """

    pass


##############################################


def turkeyLadder(
        col_name: str,
        df: pd.DataFrame,
        s_Neg: bool = True,
        s_Pos: bool = True,
        drop: bool = True,
) -> pd.DataFrame:
    """Transformations to remove skewness of data

    Parameters
    ----------
    col_name str: name of columns to encode
    df pd.DataFrame: dataframe
    s_Pos bool: bool that determines to add transformations to remove positive skew
    s_Neg bool: bool that determines to add transformations to remove negative skew
    drop bool: bool that determines if remove original column

    Returns
    ----------
    df pd.DataFrame: Updated pd.DataFrame with sin and cos encode

    """

    # Check if column is number value
    if is_numeric_dtype(df[col_name]) == False:
        raise ValueError("The passed column is of type {}. Must be numeric".format(df[col_name].dtype))

    col_vals = df[col_name].values

    # Add transformations for postive skew
    if s_Pos == True:
        df["_".join([col_name, "log"])] = np.log(col_vals)
        df["_".join([col_name, "reciprocal_root"])] = -1 / np.sqrt(col_vals)
        df["_".join([col_name, "reciprocal"])] = -1 / col_vals
        df["_".join([col_name, "reciprocal_square"])] = -1 / np.power(col_vals, 2)

    # Add transformations for negative skew
    if s_Neg == True:
        df["_".join([col_name, "sqrt"])] = np.sqrt(col_vals)
        df["_".join([col_name, "square"])] = -1 / np.power(col_vals, 2)

    # Optional: remove original column
    if drop == True:
        df = df.drop(col_name, axis=1)

    return df


##############################################


def circularEncode(
        col_name: str,
        df: pd.DataFrame,
        sin_k: float = 1.0,
        cos_k: float = 1.0,
        drop: bool = True,
) -> pd.DataFrame:
    """Encode circular data into sin and cos combo

    Parameters
    ----------
    col_name str: name of columns to encode
    df pd.DataFrame: dataframe
    sin_k float: scaling value for sin function
    cos_k float: scaling value for sin function
    drop bool: bool that determines if remove original column

    Returns
    ----------
    df pd.DataFrame: Updated pd.DataFrame with sin and cos encode

    """

    # Check if column is number value
    if is_numeric_dtype(df[col_name]) == False:
        raise ValueError("The passed column is of type {}. Must be numeric".format(df[col_name].dtype))

    # Add sin and cos column
    col_vals = df[col_name].values
    sin_vals = np.sin(pi * ((col_vals + 0.5) / sin_k))
    cos_vals = np.cos(pi * ((col_vals + 0.5) / cos_k))
    df["_".join([col_name, "sin"])] = sin_vals
    df["_".join([col_name, "cos"])] = cos_vals

    # Optional: remove original column
    if drop == True:
        df = df.drop(col_name, axis=1)

    return df


##############################################


def testLinear():
    """Used to test import of functions from Augment/Linear.py

    Parameters
    ----------
    None:

    Returns
    ----------
    None:

    """

    print("called test from Augment/Linear.py")
