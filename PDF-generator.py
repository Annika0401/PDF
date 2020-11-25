from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import datetime
from reportlab.lib import colors

######################
# Benennung des Dokuments
fileName ='Experiment.pdf'
author = 'Annika'

######################
# Erstellung des Dokuments
pdf = canvas.Canvas(fileName)

######################
# Überschrift
pdf.setFont("Courier", 25)
title= 'Name of experiment'
pdf.setFillColorRGB(0,0,0.4)
pdf.drawString(30,740, title)

#######################
# Id, Autor, Datum
pdf.setFillColor(colors.black)
text = pdf.beginText(30, 718)
text.setFont("Helvetica", 10)


textLines = ['Id: 0001']
for line in textLines:
    text.textLine(line)
pdf.drawText(text)


text = pdf.beginText(30, 705)
text.setFont("Helvetica", 10)
textLines = ['Author: Annika']
for line in textLines:
    text.textLine(line)
pdf.drawText(text)


text = pdf.beginText(30, 692)
text.setFont("Helvetica", 10)
now=datetime.datetime.now()

textLines = ['']
for line in textLines:
    text.textLine(now.strftime("%d-%m-%Y"))
pdf.drawText(text)

#######################
# Zwischenlinie

pdf.line(30,679,565.27,679)

#######################
# Name und Icon

image = 'Label.png'
pdf.drawInlineImage(image, 445.27, 771.89, width=120, height=40)

#######################
# Erste Tabelle
pdf.setFillColor(colors.black)
text = pdf.beginText(30, 653)
text.setFont("Helvetica", 12)

textLines = ['vessels & volumes']
for line in textLines:
    text.textLine(line)
pdf.drawText(text)

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
cm = 2.54
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont

pdf = []

data = [
    ['number', 'vessel type', 'volume', 'unit' ],
    ['1', 'falcon tube', '50', 'mL'],
    ['2', 'eppendorf tube', '1.5', 'mL'],
    ['3', 'shake flask', '1', 'L']
]

table = Table(data, colWidths=90, rowHeights=20)

table.setStyle(TableStyle([('BACKGROUND',(0,0),(3,0), colors.lightgrey),
                            ('TEXTFONT',(0,0),(3,0), 'bold'),
                            ('FONTSIZE',(0,0),(3,0),10),
                            ('BOX', (0,0),(3,3), 0.5,colors.black)
                            ]))
pdf.append(table)



#######################
# End page + save document
pdf.save()



