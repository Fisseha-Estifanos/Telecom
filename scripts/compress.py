"""
A script to compress csv files
"""

# imports
import pandas as pd

# import the data frame
df = pd.read_csv('../data/Week1_challenge_data_source.csv')

# compress and save the original data set
df.to_csv('../data/Week1_challenge_data_source.csv.bz2')
print('file compressed and saved successfully.')
