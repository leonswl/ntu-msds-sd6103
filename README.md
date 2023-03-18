# SD6103 Project


![screen of sample xml data](assets/test_xml_screenshot.png)
*[Link](https://dblp.uni-trier.de/rec/journals/isafm/GiriDDC21.xml)*


## Installations & Usage

### Set up
Code execution is prepared and managed using Python. Set up your own preferred local virtual environment, or use the format below:

Run the following in the file directory containig the cloned repository.
```
# set up venv
python3 -m venv .venv

# install python dependencies
pip install -r requirements.txt

```

### Usage
Python modules are stored in [src](src/). Make sure you're in the root directory of the folder when executing the following commands in the terminal.

### Downloading and Preparing dataset
If you have not downloaded the datasets, execute the `download_prepare.py` module
```
python3 src/extract.py

# or run it as a module
python3 -m src.extract
```

You will see 3 new items in your *root* directory - (1) `dblp.dtd`, `dblp.xml` and `dblp.xml.gz`. For directory organisational purposes, you should place the data artifacts in a separate folder. E.g. `artifacts/`. 

### Parsing and extracting the xml data to a csv

Once you have the dblp dataset successfully downloaded, you can continue to parse and extract the xml data. 

First define your paths in `config.yml`. Head to the [config file](config.yml) to confirm the path of your artifacts.
```
# this is the path where your dblp datasets are stored at. 
dblp_path: "<dblp_path>/dblp.xml"
dblp_path: "artifacts/dblp.xml" # if the files are in the artifacts subfolder
dblp_path: "dblp.xml" # if the files are in the root folder

#
```

After defining the path in the config file, you can proceed to the parsing itself.Note that this step takes some time and will use up quite abit of RAM so be prepared for your machine to slow down when executing the commands below.

```
# parser using a deprecated dataframe.append() method which will result in numerous warnings. 
# to execute parser while suppressing warnings, run the following
python3 -W src/execute_parser.py 

```


