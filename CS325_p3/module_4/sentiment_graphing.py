from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
from random import choice
from matplotlib import interactive

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple',
          'pink', 'brown', 'black', 'gray', 'cyan']


def csv_to_df(file_name: str, n_lines) -> DataFrame:
    df = read_csv(file_name, nrows=n_lines, sep='\t', header=None, names=['sentiments'])
    df['sentiment_count'] = df.groupby('sentiments')['sentiments'].transform('count')
    df.drop_duplicates(inplace=True)
    return df


def plot_sentiments(df: DataFrame, file_name, fig_num) -> None:
    color = choice(colors)
    print("Plotting figure {} for file {}\n".format(fig_num, file_name))
    plt.figure(fig_num)
    plt.bar(df['sentiments'], df['sentiment_count'], color=color)
    colors.remove(color)
    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')
    plt.title("{} sentiments".format(file_name))
