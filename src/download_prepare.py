from dblp_parser import DBLP

def main():
    # download DBLP
    dblp = DBLP()
    dblp.download_latest_dump()

if __name__ == "__main__":
    main()