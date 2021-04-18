import os
import unicodedata
from pathlib import Path
from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import HTMLExporter
from bs4 import BeautifulSoup


def generate_sites(path_name_file: str, name_file: str):

    c = Config()

    c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
    c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
    c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)

    path_save = '../web'
    result = HTMLExporter(Config=c).from_file(path_name_file)

    with open(f'{path_save}/{name_file}.html', mode='w', encoding='utf-8') as html:
        html.write(result[0])


def search_files():
    # TODO: pasar un listado de archivos a ignorar para la generacion del html
    path_book = '../book'
    ipynb = '.ipynb_checkpoints'
    list_path = []
    # Con la funcion rglob busca todos los archivos con la extension .ipynb
    for element in Path(path_book).rglob('**/*.ipynb'):
        # se brinca todos los archivos que estan carpertas "checkpoints"
        if not str(element).find(ipynb) > 0:
            path_name_file = os.path.abspath(element)
            name_file_split = str(element).split('/')[-1].split('.')[:-1]
            # junto a lista para definir el nombre del archivo html
            name_file = ''.join(name_file_split)
            name_file = unicodedata.normalize("NFKD", name_file).encode(
                "ascii", "ignore").decode("ascii")  # limpio de acentos
            print(f'Generando html: {name_file}')
            generate_sites(path_name_file, name_file)


def create_index():
    def change_img_path():
        pass

    def insert_tag(tag: str, content: str, attrs):
        new_tag = BeautifulSoup.new_tag(name=tag)

        new_tag.string = content
        return new_tag

    path_web = '../web'
    path_template_html = './template.html'

    template_html = open(path_template_html)
    html_raw = template_html.read()
    template_html.close()
    html = BeautifulSoup(html_raw, 'html.parser')
    body = html.body
    body.append(insert_tag(tag="h1",content="Soy un h1"))

    print(body)


if __name__ == "__main__":
    # search_files()
    create_index()

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
