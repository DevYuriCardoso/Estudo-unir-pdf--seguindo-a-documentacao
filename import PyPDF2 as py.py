from PyPDF2 import PdfWriter as pw

merger = pw()

for pdf in ["arquivo.pdf", "arquivo2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
