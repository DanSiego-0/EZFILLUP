from pdf2docx import Converter, parse


PDF_FILE = 'test.pdf'
WORD_FILE = 'text.docx'

conv = Converter(pdf_file=PDF_FILE)
conv.convert(docx_filename=WORD_FILE, start=0,end=None)
conv.close()

parse(pdf_file=PDF_FILE,docx_file=WORD_FILE,start=0,end=None)
