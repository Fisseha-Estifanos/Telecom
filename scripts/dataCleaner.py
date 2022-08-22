"""
A data cleaner script
"""

import pandas as pd

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
        """
        self.df.drop(cols, axis=1, inplace=True)
        return self.df
