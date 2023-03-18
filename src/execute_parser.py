from dblp_parser import DBLP
import yaml

def main():

    with open("config.yml", encoding="utf-8", mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        dblp_path = cfg['execute_parser']['dblp_path']
        save_path = cfg['execute_parser']['save_path']

    # instantiate DBLP class
    dblp = DBLP()
    features = {"url", "author", "ee", "journal", "number", "pages", "publisher", "series","booktitle", "title", "volume", "year"}
    dblp.parse_all(dblp_path, save_path, features_to_extract=features)



if __name__ == "__main__":
    main()