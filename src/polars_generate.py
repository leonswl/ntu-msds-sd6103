import yaml
import ast
import polars as pl   
import time

def generate():

    start = time.time()

    # Load configuration from YAML file
    with open("config.yml", encoding='utf-8', mode='r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)
        # Read paths from configuration
        read_path = cfg['generate']['read_path']
        author_output_path = cfg['generate']['author_output_path']
        publish_output_path = cfg['generate']['publish_output_path']
        publication_output_path = cfg['generate']['publication_output_path']

    # Read data from CSV file
    data = pl.read_csv(read_path, low_memory=False, quote_char='"')
    print("Successfully read data input")

    # GENERATE PUBLICATION FILE

    print("Commencing generation of Publication export")
    # Create dataframe for publication by dropping columns
    df_publication = data.drop(['', 'author'])
    df_publication = df_publication.rename({'key':'PubKey'})
    df_splitpubkey = df_publication.select(pl.col('PubKey').str.split('/').arr.to_struct(n_field_strategy="max_width")).unnest('PubKey')
    df_splitpubkey.columns = ['PubKey1', 'PubKey2', 'PubKey3', 'PubKey4', 'PubKey5']
    df_publication_id = pl.DataFrame(range(len(df_publication)),schema=[('Id')]) # create dataframe with id column for publication table
    df_publication_new = pl.concat([df_publication_id,df_publication,df_splitpubkey],how="horizontal")
    df_publication_new = df_publication_new.drop(['cdrom','cite', 'crossref','editor','ee','isbn','note', 'number', 'pages','url', 'volume','publnr','PubKey3','PubKey4','PubKey5','chapter','address']) # drop irrelevant columns
    print(df_publication_new.head())

    print("Publication - Completed transformation and cleaning")

    # Write dataframes to CSV files
    df_publication_new.write_csv(
        file=publication_output_path,
        has_header=True,
        separator=',',
        quote='"'
        )

    print("Publication - Completed export")

    # GENERATE PUBLISH AND AUTHOR FILES
    print("Commencing generation of Publication export")

    # Create dataframe for publish and authors
    df_publish_rows = [(row['key'], author) for row in data[['key', 'author']].rows(named=True) for author in ast.literal_eval(row['author'])]
    df_publish = pl.DataFrame(df_publish_rows, schema=[('PubKey'),('AuthorName')])
    df_publish_id = pl.DataFrame(range(len(df_publish)),schema=[('Id')]) # create dataframe with id column for publish table
    df_publish_new = pl.concat([df_publish_id,df_publish],how='horizontal') # concat dataframe with PublishId column with publish dataframe
    authors = set(df_publish['AuthorName'].unique())
    df_authors_id = pl.DataFrame(range(len(authors)),schema=[('Id')]) # create dataframe with id column for author table
    df_authors = pl.DataFrame({'Name': list(authors)})
    df_authors_new = pl.concat([df_authors_id,df_authors],how='horizontal') # concat dataframe with AuthorId column with authors dataframe

    df_publication_new = df_publication_new.rename({'Id': 'PublicationId'})
    df_publication_new_select = df_publication_new.select(['PublicationId', 'PubKey'])
    df_publish_new_join = df_publish_new.join(df_publication_new_select, on='PubKey', how='left')

    df_authors_new = df_authors_new.rename({'Name': 'AuthorName'})
    df_authors_new = df_authors_new.rename({'Id': 'AuthorId'})
    df_publish_new_join = df_publish_new_join.join(df_authors_new, on='AuthorName', how='left')

    df_publish_new_fina = df_publish_new_join.drop("PubKey", "AuthorName")
    print(df_authors_new.head())
    print(df_publish_new_join.head())

    print("Publish & Authors - Completed transformation and cleaning")

    # Write dataframes to CSV files
    df_authors_new.write_csv(
        file=author_output_path,
        has_header=True,
        separator=',',
        quote='"')
    
    df_publish_new_fina.write_csv(
        file=publish_output_path,
        has_header=True,
        separator=',',
        quote='"')

    print("Publish & Authors - Completed export")

    end = time.time()
    print(f"Elapsed Time: {(start-end)/60} mins")


if __name__ == '__main__':
    generate()
