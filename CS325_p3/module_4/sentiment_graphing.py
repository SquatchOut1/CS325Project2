from pandas import read_csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from random import choice


def csv_to_df(file_name: str, n_lines) -> DataFrame:
    df = read_csv(file_name, nrows=n_lines, sep='\t', header=None, names=['sentiments'])
    df['sentiment_count'] = df.groupby('sentiments')['sentiments'].transform('count')
    df.drop_duplicates(inplace=True)
    return df


def plot_sentiments(df: DataFrame, file_name, fig_num) -> None:
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']
    plt.bar(df['sentiments'], df['sentiment_count'], color=choice(colors))
    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')
    plt.title("{} Sentiments".format(file_name))
    plt.figure(fig_num)

