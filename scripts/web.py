import os
import unicodedata
from pathlib import Path
from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import HTMLExporter
from bs4 import BeautifulSoup


def convert_nb_html(path_name_file: str, name_file: str):
    """ Conviert files notebooks in html"""
    c = Config()

    c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
    c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
    c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)

    path_save = '../web'
    # regresa una lista en la posicion 0 viene el html
    result = HTMLExporter(Config=c).from_file(path_name_file)

    with open(f'{path_save}/{name_file.lower()}.html', mode='w', encoding='utf-8') as html:
        html.write(result[0])


def generate_files_html(path_file: [], name_file: [], ignore=[]):
    """Logic to iterate all notebooks to html"""
    # TODO: agregar que ignore algunos archivos
    for count in range(len(path_file)):
        convert_nb_html(path_file[count], name_file[count])


def build_index(html: str):
    """build de file index.html and save in location"""
    if not (type(html) == 'str'):
        html = str(html)

    path = "../web/index.html"
    with open(path, mode='w', encoding='utf-8') as index:
        index.write(html)


def copy_imgs():  # TODO: por hacer
    """copy all imgs from src to folder web/img"""
    pass


def build_cap(title: str, name_items: [], url_base: str, html: BeautifulSoup) -> BeautifulSoup:
    """Build all html for each cap with the list"""
    title = build_tag('h1', title)
    list_ul = build_tag('ul', '')
    for item in name_items:
        list_item = build_tag('li', '')
        subtitle = build_tag('h2', item)
        link = build_tag('a', f'{subtitle.h2}', href=f"{url_base}/{item}")
        list_item.li.append(link.a)
        list_ul.ul.append(list_item.li)

    html.body.append(title.h1)
    html.body.append(list_ul.ul)


def build_tag(tag: str, content: str, **kwargs) -> BeautifulSoup:
    """build any tag html"""
    new_tag = BeautifulSoup(f'<{tag}>{content}</{tag}>', 'html.parser')

    for attr in kwargs:
        new_tag.contents[0][attr] = kwargs[attr]

    return new_tag


def search_files_nb():
    path_book = '../book'
    ipynb = '.ipynb_checkpoints'
    list_path = {'path_file': [], 'name_file': []}
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
            list_path['path_file'].append(path_name_file)
            list_path['name_file'].append(name_file)

    return list_path


def change_path_img_in_html():  # TODO: por hacer
    pass


def get_list_html() -> []:
    """Read all files in folder, then generate a list with it

    Returns:
        []: [List of files html in folder]
    """
    path = '../web'
    list_paths = []
    for file in Path(path).rglob('*.html'):
        list_paths.append(str(file).split("/")[-1])

    return list_paths


def generate_list_cap(list_files: []) -> dict:

    list_complet = {}

    for file_html in list_files:
        init = file_html.split("_")[0]
        number = 0
        if init.isnumeric():
            number = int(init)
            number = int(str(number)[0])
        if list_complet.get(number) is None:
            list_complet[number] = [file_html]
        else:
            list_complet.get(number).append(file_html)

    for key in list_complet:
        list_complet[key] = sorted(list_complet.get(key))

    return list_complet


def build_body_html(html: BeautifulSoup) -> BeautifulSoup:
    """Logic to generate body for html index

    Args:
        html (BeautifulSoup): all content html

    Returns:
        BeautifulSoup: all new content html
    """
    # trar el listado de htmls
    list_html = get_list_html()
    # separar y generar un array por capitulo
    all_caps = generate_list_cap(list_html)

    # crear la logica para crear el cap html html
    url_base = 'https://www.alejandro-leyva.com/micro-21/web'
    for i in range(len(all_caps)-1):
        build_cap(f'Capitulo {i}', all_caps.get(i), url_base, html)
    # regresar todo el html

    return html


def get_html_template() -> BeautifulSoup:
    #path_web = '../web'
    path_template_html = './template.html'

    template_html = open(path_template_html)
    html_raw = template_html.read()
    template_html.close()
    return BeautifulSoup(html_raw, 'html.parser')

if __name__ == "__main__":
    print("Buscando archivos...")
    files = search_files_nb() #OK
    print("Convirtiendolos a html...")
    generate_files_html(files['path_file'], files['name_file']) #OK
    print("Generando index.html")
    html = get_html_template()  # OK
    html = build_body_html(html)
    build_index(html)
    print("Termine... xD")