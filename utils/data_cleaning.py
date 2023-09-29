# data_cleaning.py
import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    df['Text'] = df['Text'].str.strip()
    df['Text'] = df['Text'].str.replace('<[^<]+?>', '', regex=True)
    df.drop_duplicates(subset=['Text'], inplace=True)
    return df
