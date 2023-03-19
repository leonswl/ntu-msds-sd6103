import glob
import pandas as pd
import yaml

def combine():
    """
    This function reads CSV files from a specified path, combines them into a single pandas DataFrame,
    and saves the output as a CSV file to a specified directory. The file name of the output CSV file
    is either 'dblp.csv' or 'dblp_copy.csv', depending on whether 'dblp.csv' already exists in the output directory.
    """
    with open("config.yml", encoding='utf-8', mode='r') as ymlfile:
        # Load configuration settings from YAML file
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        read_path = cfg['combine']['read_path'] # Input directory path
        output_path = cfg['combine']['output_path'] # Output directory path

    df_lst = []
    for fname in glob.glob(f'{read_path}/dblp_*.csv'):
        # Loop through all CSV files in input directory that start with 'dblp_' and end with '.csv'
        df = pd.read_csv(fname, low_memory=False)
        df_lst.append(df)

    df_full = pd.concat(df_lst) # Combine all CSV files into a single pandas DataFrame

    fnames_lst = []
    for fname in glob.glob(f'{output_path}/*.csv'):
        # Loop through all CSV files in output directory with extension '.csv'
        filename = fname.split('/')[-1]
        fnames_lst.append(filename)

    if "dblp.csv" in fnames_lst:
        # If 'dblp.csv' already exists in output directory, save output DataFrame as 'dblp_copy.csv'
        df_full.to_csv(f"{output_path}/dblp_copy.csv")
        print(f"A dataset with a similar name exist. Successfully combined files into {output_path}/dblp_copy.csv")
    else:
        # Otherwise, save output DataFrame as 'dblp.csv'
        df_full.to_csv(f"{output_path}/dblp.csv")
        print(f"Successfully combined files into {output_path}/dblp.csv")


if __name__ == "__main__":
    combine() # Call the 'combine' function when the script is run as the main program
