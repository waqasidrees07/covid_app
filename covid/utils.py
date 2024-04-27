import pandas as pd
import csv

def get_csv_data():

    csv_file_path = 'data/owid-covid-data.csv'
    df = pd.read_csv(csv_file_path)
    data_list = df.to_dict('records')

    return data_list


def add_csv_data(new_data):

    csv_file_path = 'data/owid-covid-data.csv'
    data = get_csv_data()
    df = pd.DataFrame(data)
    new_data_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_data_df], ignore_index=True)
    df.to_csv(csv_file_path, index=False)

    return df


def update_csv_data(updated_data):

    csv_file_path = 'data/owid-covid-data.csv'
    data = get_csv_data()
    df = pd.DataFrame(data)
    index = df.index[df['id'] == updated_data['id']]
    if not index.empty:
        for key, value in updated_data.items():
            df.loc[index, key] = value

    df.to_csv(csv_file_path, index=False)
    
    return df


def delete_csv_data(key, key_column):

    csv_file_path = 'data/owid-covid-data.csv'
    data = get_csv_data()
    df = pd.DataFrame(data)
    df = df[df[key_column] != key]
    df.to_csv(csv_file_path, index=False)

    return df
