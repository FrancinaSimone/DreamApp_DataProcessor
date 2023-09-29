import pandas as pd
import os

# The spell to reshape the data into its true form.
def reshape_data(main_folder_path):
    tribe_folders = [f for f in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, f))]
    reshaped_data = []

    for tribe in tribe_folders:
        tribe_folder_path = os.path.join(main_folder_path, tribe)
        csv_files = [f for f in os.listdir(tribe_folder_path) if f.endswith('.csv')]

        for csv_file in csv_files:
            df = pd.read_csv(os.path.join(tribe_folder_path, csv_file), header=None)
            for index, row in df.iterrows():
                content = row[0]
                segments = content.split('\n', 2)
                if len(segments) >= 3:
                    title = segments[1].strip()
                    text = segments[2].split('\n\nReturn to', 1)[0].strip()
                    reshaped_data.append([tribe, title, text])

    final_df = pd.DataFrame(reshaped_data, columns=['Culture', 'Title', 'Text'])
    final_df.set_index('Culture', inplace=True)
    return final_df
