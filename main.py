import WordModifier
from datetime import datetime

word = WordModifier.WordModifier("Rescources/Template.docx")

word.add_variable_to_context("display_paragraph", False)
word.close_document(datetime.now().strftime("%d-%m-%Y"))
