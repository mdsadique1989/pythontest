from reportlab.pdfgen import canvas
pdf_file = canvas.Canvas ("clcodingpdff.pdf")
pdf_file.drawString(72, 720, "Hello, World!")
pdf_file.drawString (72, 700, "Fre PDF Document ")
pdf_file.drawString(72, 680, "Like | Share")
pdf_file.drawString(72, 660, "Subscribe ")
pdf_file.drawString(72, 640, "clcoding.com ")
pdf_file.drawString(72, 620, "thank you ")
pdf_file.save()