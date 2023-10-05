import docxtpl
from docxtpl import DocxTemplate

# https://docxtpl.readthedocs.io/en/latest/
class WordModifier:
    document: docxtpl.template
    context = {}
    def __init__(self, path):
        self.document = DocxTemplate(path)

    def add_variable_to_context(self, name: str, value: any):
        self.context[name] = value

    def close_document(self, output_filename: str):
        self.document.render(self.context)
        self.document.save(f"output/{output_filename}.docx")
