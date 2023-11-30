import pandas as pd


def csv_to_df(file_name: str):
    df = pd.read_csv(file_name, sep='\t', header=None, names=['sentiments'])
    print(df)

