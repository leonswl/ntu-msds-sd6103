# Script to split csv file into multiple sets
import contextlib
import csv
import os
import yaml

def split():
    """
    This function reads a csv file from the given input path specified in the configuration file.
    It then splits the csv file into smaller csv files with a specified number of rows per file, and saves them 
    to the output path specified in the configuration file.
    """

    # Read the configuration file
    with open("config.yml", encoding='utf-8', mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        read_path=cfg['split']['read_path']
        rows_each=cfg['split']['rows_each']
        output_path=cfg['split']['output_path']

    print(f"""
        Config Parameters:
        `read_path`: {read_path}
        `rows_each`: {rows_each}
        `output_path`: {output_path}
    """)

    # make directory if 'artifacts/split' does not exist
    with contextlib.suppress(FileExistsError):
        os.makedirs(output_path)

    # Get the filename and rows per csv from the configuration
    filename = read_path.split("/")[-1]  # Extracts filename from read path
    file_name = os.path.splitext(read_path)[0]  # Removes extension from filename
    file_name = file_name.split('/')[-1]  # Extracts filename from file path
    
    rows_per_csv = rows_each

    print("Commence splitting of files. This process will take a few minutes.")

    # Read the input csv file
    with open(read_path) as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames
        rows = list(reader)
        pages = []

        row_count = len(rows)
        start_index = 0

        # Split the rows into pages of specified size
        while start_index < row_count:
            pages.append(rows[start_index: start_index+rows_per_csv])
            start_index += rows_per_csv

        # Write the pages to individual csv files
        for i, page in enumerate(pages):
            with open(f'{output_path}/{file_name}_{i+1}.csv', 'w+') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=header)
                writer.writeheader()
                for row in page:
                    writer.writerow(row)

        # Print a message indicating the number of files created
        print(f'DONE splitting {filename} into {len(pages)} files')


if __name__ == "__main__":
    split()
