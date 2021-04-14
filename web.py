from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import HTMLExporter

c =Config()

c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)


result = HTMLExporter(Config=c).from_file('book/cap2/input.ipynb')

with open('index.html', 'w') as html:
    html.write(result[0])

