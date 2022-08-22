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
    new_df.to_csv(output_path, sep=";", encoding="ansi")
    return new_df

"""
def save_to_csv(data, delimiter=";"):
    file_exist = False
    try:
        f = open(output_path, "r")
        f.close()
    except:
        # create file and setup file with proper header if file doesn exist
        with open(output_path, "w", newline="") as f:
            write = csv.writer(f, delimiter=delimiter)
            header = ["Date Time", "Level", "Name", "Price"]
            write.writerow(header)        

    with open(output_path, "a", newline="") as f:
        write = csv.writer(f, delimiter=";")
        write.writerows(data)

def import_from_csv():
    data = []
    with open(output_path, 'r') as f:
        file = csv.reader(f, delimiter=";")
        for line in file:
            data.append(line)
    return data[1:]
"""
