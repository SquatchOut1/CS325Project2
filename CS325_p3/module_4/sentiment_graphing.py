from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
from random import choice
from matplotlib import interactive


def csv_to_df(file_name: str, n_lines) -> DataFrame:
    df = read_csv(file_name, nrows=n_lines, sep='\t', header=None, names=['sentiments'])
    df['sentiment_count'] = df.groupby('sentiments')['sentiments'].transform('count')
    df.drop_duplicates(inplace=True)
    return df


def plot_sentiments(df: DataFrame, postTitle, fig_num, saveLoc) -> None:
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple',
          'pink', 'brown', 'black', 'gray', 'cyan']
    color = []
    for i in range(3):
        color.append(choice(colors))
        colors.remove(color[-1])
    print("Plotting figure {} for {}\n".format(fig_num, postTitle))
    plt.figure(postTitle)
    plt.bar(df['sentiments'], df['sentiment_count'], color=color, label=df['sentiments'])
    plt.xlabel(list(df)[0])
    plt.ylabel('Quantity of Sentiment')
    plt.title("{} sentiments".format(postTitle))
    plt.legend(title="Sentiments")
    plt.savefig(saveLoc)
