"""
A data cleaner script
"""

import pandas as pd
import numpy as np

class dataCleaner():
    """
    A data cleaner class
    """
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df;
        print('Data cleaner in action.')

    def remove_unwanted_cols(self, cols: list) -> pd.DataFrame:
        """
        A function to remove unwanted columns from a DataFrame

        Parameters
        =--------=
        cols: list
            The unwanted column lists

        Returns
        =-----=
        self.df
            The dataframe rid of the unwanted cols
        """
        try:    
            self.df.drop(cols, axis=1, inplace=True)
        except Exception as e:
            print(e)
        finally:
            return self.df

    def percent_missing(self, df: pd.DataFrame) -> None:
        """
        A function telling how many missing values exist or better still
        what is the % of missing values in the dataset?
        
        Parameters
        =--------=
        df: pandas dataframe
            The data frame to calculate the missing values from

        Returns
        =-----=
        None: nothing
            Just prints the missing value percentage
        """
        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The dataset contains", round(((totalMissing/totalCells) * 100), 10), "%", "missing values.")

    def convert_to_datetime(self, df:pd.DataFrame)-> pd.DataFrame:
        # convert datetime column to datetime
        self.df['Start'] = pd.to_datetime(self.df['Start'], errors='coerce')
        self.df['End'] = pd.to_datetime(self.df['End'], errors='coerce')
        return self.df

    def fill_na(self, type: str, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        """
        A function to fill nulls and undefined data types

        Parameters
        =--------=
        type: string
            The type of the fill. Eg: mode, mean, median
        df: pd.dataframe
            The data frame to fill 
        cols: list
            The list of columns to be filled
        """
        if (type == 'mean'):
            for col in cols:
                self.df.col.fillna(value=df.col.mean(), axis=1, inplace=True)
            return self.df
        elif (type == 'median'):
            for col in cols:
                self.df.col.fillna(value=df.col.median(), axis=1, inplace=True)
            return self.df
        elif (type == 'mode'):
            for col in cols:
                self.df.col.fillna(value=df.col.mode(), axis=1, inplace=True)
            return self.df
        else:
            print('type must be either mean, median or mode')
        
