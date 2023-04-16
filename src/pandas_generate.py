import yaml
import pandas as pd
import ast


def generate():
    # Load configuration from YAML file
    with open("config.yml", encoding='utf-8', mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)

        # Read paths from configuration
        read_path = cfg['generate']['read_path']
        author_output_path = cfg['generate']['author_output_path']
        publish_output_path = cfg['generate']['publish_output_path']
        publication_output_path = cfg['generate']['publication_output_path']

    # Read data from CSV file
    data = pd.read_csv(read_path, engine='pyarrow')
    print("Successfully read data input")

    # GENERATE PUBLICATION FILE
    
    print("Commencing generation of Publication export")
    # Create dataframe for publication by dropping columns
    df_publication = data.drop(['','author'],axis=1)
    df_publication = df_publication.rename(columns={'key':'PubKey'})

    print("Publication - Completed transformation and cleaning")

    # Write dataframes to CSV files
    df_publication.to_csv(path_or_buf=publication_output_path, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label='Id', mode='w', encoding='utf-8', compression='infer', quoting=None, quotechar='"',lineterminator='\n', chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

    print("Publication - Completed export")
    
    # GENERATE PUBLISH AND AUTHOR FILES
    print("Commencing generation of Publication export")
    # Create dataframe for publish and authors
    df_publish_rows = [[row['key'], author] for _, row in data[['key','author']].iterrows() for author in ast.literal_eval(row['author'])]
    df_publish = pd.DataFrame(df_publish_rows, columns=['PubKey','AuthorName'])
    print("Publish & Authors - Completed transformation and cleaning")
    authors = set(df_publish['AuthorName'].unique())
    df_authors = pd.DataFrame(authors,columns=['Name'])

    df_authors.to_csv(path_or_buf=author_output_path, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label='Id', mode='w', encoding='utf-8', compression='infer', quoting=None, quotechar='"',lineterminator='\n', chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)
    df_publish.to_csv(path_or_buf=publish_output_path, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label='Id', mode='w', encoding='utf-8', compression='infer', quoting=None, quotechar='"',lineterminator='\n', chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

    print("Publish & Authors - Completed export")

if __name__ == '__main__':
    generate()


    





