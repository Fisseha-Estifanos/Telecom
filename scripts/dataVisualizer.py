"""
A script to visualize data
"""

# imports
from cProfile import label
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class dataVisualizer():
    def __init__(self) -> None:
        print('Data visualizer in action.')

    def plot_pie(df: pd.DataFrame, column: str, title: str) -> None:
        """
        A function to plot pie charts

        Parameters
        =--------=

        Returns
        =-----=
        None: nothing
            Only plots the plot
        """
        fig = plt.figure(figsize=(10,10))

        col = df[column].value_counts().nlargest(n=10)

        data = col.values
        labels = col.keys()

        last_num = len(data)

        colors = sns.color_palette('pastel')[0:last_num]

        plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
        plt.title(title)
        plt.show()
