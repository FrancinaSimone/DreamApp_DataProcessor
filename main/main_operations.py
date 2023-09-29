from config.folder_paths import main_folder_path
from utils.data_cleaning import clean_data
from data_loading.data_loader import load_tribe_data
from data_reshaping.reshaper import reshape_data

def main():
    # First, we gather the ingredients—ahem, data.
    raw_data = load_tribe_data(main_folder_path)
    
    # Next, let's cast the reshaping spell.
    reshaped_data = reshape_data(main_folder_path)
    
    # Finally, we cleanse the data of any impurities.
    final_data = clean_data(reshaped_data)
    
    # Voila! Your DataFrame is ready for further enchantments.
    print(final_data.head())

if __name__ == "__main__":
    main()
