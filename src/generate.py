import csv
import ast
import yaml


with open("config.yml", encoding='utf-8', mode='r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.Loader)
    read_path = cfg['generate']['read_path']
    aut_output_path = cfg['generate']['aut_output_path']
    autpub_output_path = cfg['generate']['autpub_output_path']

data = open(read_path, 'r', encoding='utf-8')
aut = open(aut_output_path, 'a', encoding='utf-8')
pub_aut = open(autpub_output_path, 'a', encoding='utf-8')


def generate():
    with data, aut, pub_aut:
        reader = csv.DictReader(data)

        aut_writer = csv.writer(aut)
        pub_aut_writer = csv.writer(pub_aut)

        aut_writer.writerow(['author'])
        pub_aut_writer.writerow(['key', 'author'])

        authors = set()
        for line in reader:
            key = line['key']
            author_list = ast.literal_eval(line['author'])
            for au in author_list:
                authors.add(au)
                print(au)
                pub_aut_writer.writerow([key, au])
        for au in list(authors):
            aut_writer.writerow([au])


if __name__ == '__main__':
    generate()
