mimport numpy as np
import pandas as pd
%matplotlib inline

df = pd.read_csv("train.csv")
df.shape

import matplotlib.pyplot as plt      # matplotlib.pyplot plots data
def plot_corr(df, size=11):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot

    Displays:
        matrix of correlation between columns.  Blue-cyan-yellow-red-darkred => less to more correlated
                                                0 ------------------>  1
                                                Expect a darkred line running from top left to bottom right
    """

    corr = df.corr()    # data frame correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)   # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)  # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)  # draw y tick marks
    plt.tight_layout()
    plt.figure(1, [300, 300])

    # Set the x-axis limit
    # ax.set_xlim(-1,500)
    # Change of fontsize and angle of xticklabels
    plt.setp(ax.get_xticklabels(), fontsize=8, rotation='vertical')

plot_corr(df)

del df['OVER_15MINS_CALLS_PER_MONTH']
del df['AVERAGE_CALL_DURATION']

df.head(2)