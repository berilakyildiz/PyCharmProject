from pdf2docx import Converter

pdf_file = "mOtivayon letter.pdf"
docx_file = "sample.docx"

cv = Converter(pdf_file, docx_file)
cv.convert(docx_filename= docx_file)
cv.close()
