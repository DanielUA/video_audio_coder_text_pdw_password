from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdf_writer = PdfWriter()
pdf = PdfReader("file_to_read.pdf")

for page in pdf.pages:
    pdf_writer.add_page(page)

password = getpass(prompt="Enter password: ")
pdf_writer.encrypt(password)

with open("protected.pdf", mode="wb") as fh:
    pdf_writer.write(fh)

