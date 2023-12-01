from pandas import read_csv
from pandas import DataFrame
import matplotlib.pyplot as plt


def csv_to_df(file_name: str) -> DataFrame:
    df = read_csv(file_name, sep='\t', header=None, names=['sentiments'])
    return df


def plot_sentiments(df: DataFrame, file_name) -> None:
    plt.bar(df['sentiments'], color='green', height=0.5)
    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')
    plt.title("{} Sentiments".format(file_name))
    plt.show()
