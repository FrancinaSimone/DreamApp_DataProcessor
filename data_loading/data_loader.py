# data_loader.py
import os
import pandas as pd

def load_tribe_data(main_folder_path):
    # List all sub-folders (tribes) inside the main folder
    tribe_folders = [f for f in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, f))]
    all_dfs = []  # This list will hold DataFrames of all tribes

    for tribe in tribe_folders:
        # Get the path to the current tribe's folder
        tribe_folder_path = os.path.join(main_folder_path, tribe)
        # List CSV files in the current tribe's folder
        csv_files = [f for f in os.listdir(tribe_folder_path) if f.endswith('.csv')]
        # Load CSV files into DataFrames and concatenate them
        tribe_dfs = [pd.read_csv(os.path.join(tribe_folder_path, csv_file)) for csv_file in csv_files]
        all_dfs.append(pd.concat(tribe_dfs, ignore_index=True))

    # Return a DataFrame containing data from all tribes
    return pd.concat(all_dfs, ignore_index=True)
