"""
Save & Load Data (sldata)
"""
import pandas as pd

output_path = "../data/stock/data.csv"


def import_csv():
    df = pd.read_csv(output_path, encoding="ansi", sep=";")
    return df


def save_to_csv(df, sep=";"):
    df_stock = import_csv()
    new_df = pd.concat([df_stock, df], ignore_index=True)
    new_df.to_csv(output_path, sep=";", encoding="ansi", index=False)
    return new_df
