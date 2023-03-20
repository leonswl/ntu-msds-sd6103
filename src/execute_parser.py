from dblp_parser import DBLP
import yaml
import pandas as pd

def main():

    with open("config.yml", encoding="utf-8", mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        dblp_path = cfg['execute_parser']['dblp_path']
        csv_save_path = cfg['execute_parser']['csv_save_path']

    print(f"""
    Config Parameters:
    `dblp_path`: {dblp_path}
    `csv_save_path`: {csv_save_path}
    """)

    # instantiate DBLP class
    dblp = DBLP()
    # features = {"url", "author", "ee", "journal", "number", "pages", "publisher", "series","booktitle", "title", "volume", "year"}
    # dblp.parse_all(dblp_path, save_path, features_to_extract=features)

    # print all features
    dblp.print_features()

    # parse
    df = dblp.parse_all(
            dblp_path=dblp_path, 
            save_path=csv_save_path,
            output="dataframe", 
            include_key_and_mdate=True)

    df.to_parquet("dblp.parquet")

if __name__ == "__main__":
    main()