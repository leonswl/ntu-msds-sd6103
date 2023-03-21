import contextlib
import os
from math import ceil
from datetime import date
import time
import logging
import yaml
import pandas as pd
from dblp_parser import DBLP


def main():

    with open("config.yml", encoding="utf-8", mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        dblp_path = cfg['execute_parser']['dblp_path']
        save_path = cfg['execute_parser']['save_path']
        batch = cfg['execute_parser']['batch']
        log_path = cfg['execute_parser']['log_path']

    print(f"""
    Config Parameters:
    `dblp_path`: {dblp_path}
    `csv_save_path`: {save_path}
    `batch`: {batch}
    `log_path`: {log_path}
    """)

    # set up logging
    # make directory if log_path does not exist
    with contextlib.suppress(FileExistsError):
        os.makedirs(log_path)

    logging.basicConfig(filename=f"{log_path}/execute_parser_{date.today()}.log", level=logging.INFO)
    logging.info(f"""
        Date executed: {date.today()}
        Executing parsing script
        """
    )

    # instantiate DBLP class
    dblp = DBLP()

    # print all features
    dblp.print_features()

    # open dblp file
    root = dblp.open_dblp_file(dblp_path)

    logging.info(f"Total elements in root: {len(root)}")

    # initialise counters and indexes for patch parsing
    left_index, right_index = 0, batch
    batch_counter = 0
    batch_size = ceil(len(root)/batch)
    dataframes = []

    logging.info(f"Parser will begin looping through root element in batches of {batch}. Number of batch sizes is {batch_size}")

    start_time = time.time() # track parsing start time

    for i in range(batch_size):

        root_batch = root[left_index:right_index] # slice root object according to each batch size
        
        logging.info(f"""
            Currently parsing batch {i+1}
            Total elements in this batch: {len(root)}
            Index boundary: {(left_index, right_index)}
            """)

        batch_start_time = time.time() # track batch start time

        # parse
        df = dblp.parse_batch(
                root = root_batch, 
                output="dataframe", 
                include_key_and_mdate=True
                )
        
        # append parsed elements in the df into dataframe list
        dataframes.append(df)

        batch_end_time = time.time() # track end of batch parse time

        batch_time_taken = batch_end_time - batch_start_time
        total_time_taken = batch_end_time - start_time
        logging.info(f"""
            Completed batch: {i+1}
            Number of batches remaining: {batch_size - (i+1)}

            Number of elements successfully parsed in list of dataframe: {len(dataframes)}

            Time taken for parsing batch: {round(batch_time_taken/60,2)} minutes
            Total parsing time elapsed: {round(total_time_taken/60,2)} minutes            
        """)

        # update batch indexes and counters
        batch_counter += 1 # raise batch counter
        left_index, right_index = right_index, right_index+batch # set new batch indexes 

    # combine list of dataframes into one
    dataframe = pd.concat(dataframes, ignore_index=True)
    logging.info(f"""
    Completed batch parsing of xml elements. Total elements successfully parsed in list of dataframe: {len(dataframes)}
    
    -------
    """)

    # persist data as parquet and csv
    try:
        dataframe.to_csv(f"{save_path}/dblp.csv")
        
    except Exception as e:
        logging.warning(f"""
        Exception: {e}

        Dataframes are persisted as csv and parquet format in the directory where this script is executed.
        """)
        dataframe.to_csv("dblp.csv")
        

    try:
        dataframe.to_parquet(f"{save_path}/dblp.parquet")
    except Exception as e:
        logging.warning(f"""
        Exception: {e}
        """
        )
        dataframe.to_parquet("dblp.parquet")

if __name__ == "__main__":
    main()