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
        print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

    def convert_to_datetime(self, df:pd.DataFrame)-> pd.DataFrame:
        # convert datetime column to datetime
        self.df = df
        self.df['start'] = pd.to_datetime(self.df['start'], errors='coerce')
        self.df['end'] = pd.to_datetime(self.df['end'], errors='coerce')
        return self.df
