from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
cm = 2.54
from reportlab.platypus import PageBreak
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
import datetime
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)


fileName = 'Vessels.pdf'
doc = SimpleDocTemplate(fileName, pagesize=A4, rightMargin=13, leftMargin=13, topMargin=4, bottomMargin=40)

story = []
author = "AnnNeu"
date = "today"
ID = "0001"
logo = "Label.png"
plot = "Plot.png"
now = datetime.datetime.now()

def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(225*cm, 7*cm, text)
    
    

#### LOGO ####
im1 = Image(logo, 110, 30, hAlign='RIGHT')
story.append(im1)
story.append(Spacer(1,15))

#### COLLECTED DATA ####
vesselData = [
    ['number', 'vessel type', 'volume', 'unit' ],
    ['1', 'falcon tube', '50', 'mL'],
    ['2', 'eppendorf tube', '1.5', 'mL'],
    ['3', 'shake flask', '1', 'L'],
]

reactantData = [
    ['number', 'name', 'initial\nconcentration', 'substance unit','substance kind' ],
    ['1', 'pyruvate', '40', 'mg/mL', 'co-factor'],
    ['2', 'acetolacetate', '40', 'mg/mL', 'co-factor']
]

biocatalystData = [
    ['number', 'name', 'sequence', 'concentration','unit' ],
    ['1', 'lactase', 'unknown', '15', 'mg/mL']
]

conditionData = [
    ['number', 'buffer', 'concentration\nin mM', 'buffer pH','adjustment', 'reaction\ntemperature in °C', 'mixing\nin rpm' ],
    ['1', 'Tris', '400', '7.5', 'HCl', '30', '700']
]

epmtylist = ['']


#### STYLES ####
styles = getSampleStyleSheet()
Headline = ParagraphStyle('Experiment',
                        fontName="Helvetica",
                        fontSize=18,
                        alignment=0,
                        spaceAfter=14)

Headline2 = ParagraphStyle('Experiment',
                        fontName="Helvetica",
                        fontSize=14,
                        alignment=0,
                        spaceAfter=4)

Sublines = ParagraphStyle('Experiment',
                        fontName="Helvetica",
                        fontSize=9,
                        alignment=0,
                        spaceAfter=3)

Sublines2 = ParagraphStyle('Experiment',
                        fontName="Helvetica-Bold",
                        fontSize=10,
                        alignment=0,
                        spaceAfter=3)

TextStyle = ParagraphStyle('Experiment',
                        fontName="Helvetica",
                        fontSize=9,
                        alignment=0,
                        spaceAfter=3)

#### TITLE ####
story.append(Paragraph('<font >E x p e r i m e n t</font>', Headline))
story.append(Spacer(1,2))

#### DOCUMENT INFORMATION ####
ptext = '<font size="9">Author: %s</font>' % author
story.append(Paragraph(ptext, Sublines))
story.append(Spacer(1, 0))

ptext = '<font size="9">Date: %s</font>' % now.strftime("%d.%m.%Y")
story.append(Paragraph(ptext, Sublines))
story.append(Spacer(1, 0))

ptext = '<font size="9">ID: %s</font>' % ID
story.append(Paragraph(ptext, Sublines))
story.append(Spacer(1, 3))

#### UNDERLINE ####
table1 = Table(epmtylist,colWidths=580, rowHeights=0.75, hAlign="CENTER")

table1.setStyle(TableStyle([('BACKGROUND',(0,0),(1,0), colors.black)]))
story.append(table1)
story.append(Spacer(1, 10))

#### HEADLINE 2 ####
story.append(Paragraph('<font >experimental set-up:</font>', Headline2))
story.append(Spacer(1,10))

#### SHORT TEXT ####
ptext = '<font size="10">In the following, you can find an overview of the experiment with the ID %s, containing all metadata.</font>'%ID
story.append(Paragraph(ptext, TextStyle))
story.append(Spacer(1, 12))

#### TABLES ####
story.append(Paragraph('<font >vessels & volumes </font>', Sublines2))
story.append(Spacer(1,5))

table2 = Table(vesselData, colWidths=70, rowHeights=30, hAlign="LEFT")

table2.setStyle(TableStyle([('FONTNAME',(0,0),(3,0), 'Helvetica-Bold'),
                            ('FONTSIZE',(0,0),(-1,-1),9),
                            ('BOX', (0,0),(-1,-1), 0.5,colors.black),
                            ('ALIGN', (0,0), (0,3), 'CENTER'),
                            ('ALIGN', (2,0), (2,3), 'CENTER'),
                            ('ALIGN', (3,4), (3,3), 'CENTER'),
                            ('VALIGN', (-4,-4), (-1,-4), 'MIDDLE'),
                            ('LINEBELOW',(0,0),(4,0),0.5,colors.black)
                            ]))
story.append(table2)
story.append(Spacer(1, 25))


story.append(Paragraph('<font >reactants </font>', Sublines2))
story.append(Spacer(1,5))

table3 = Table(reactantData, colWidths=86, rowHeights=30, hAlign="LEFT")

table3.setStyle(TableStyle([('FONTNAME',(0,0),(4,0), 'Helvetica-Bold'),
                            ('FONTSIZE',(0,0),(4,4),9),
                            ('BOX', (0,0),(-1,-1), 0.5,colors.black),
                            ('ALIGN', (-5,-3), (-5,-1), 'CENTER'),
                            ('ALIGN', (-3,-3), (-3,-1), 'CENTER'),
                            ('ALIGN', (-2,-3), (-2,-1), 'CENTER'),
                            ('ALIGN', (-1,-3), (-1,-1), 'CENTER'),
                            ('VALIGN', (-5,-3), (-1,-3), 'MIDDLE'),
                            ('LINEABOVE',(-5,-2),(-1,-2),0.5,colors.black)
                            ]))

story.append(table3)
story.append(Spacer(1,25))

story.append(Paragraph('<font >biocatalysts </font>', Sublines2))
story.append(Spacer(1,5))

table4 = Table(biocatalystData, colWidths=86, rowHeights=30, hAlign="LEFT")

table4.setStyle(TableStyle([('FONTNAME',(0,0),(5,0), 'Helvetica-Bold'),
                            ('FONTSIZE',(0,0),(5,5),9),
                            ('BOX', (0,0),(-1,-1), 0.5,colors.black),
                            ('ALIGN', (-5,-2), (-5,-1), 'CENTER'),
                            ('ALIGN', (-3,-2), (-3,-1), 'CENTER'),
                            ('ALIGN', (-2,-2), (-2,-1), 'CENTER'),
                            ('ALIGN', (-1,-2), (-1,-1), 'CENTER'),
                            ('VALIGN', (-5,-2), (-1,-2), 'MIDDLE'),
                            ('LINEABOVE',(-5,-1),(-1,-1),0.5,colors.black)
                            ]))

story.append(table4)
story.append(Spacer(1, 25))

story.append(Paragraph('<font >reaction conditions </font>', Sublines2))
story.append(Spacer(1,5))

table5 = Table(conditionData, colWidths=80, rowHeights=30, hAlign="LEFT")

table5.setStyle(TableStyle([('FONTNAME',(0,0),(7,0), 'Helvetica-Bold'),
                            ('FONTSIZE',(0,0),(7,7),9),
                            ('BOX', (0,0),(-1,-1), 0.5,colors.black),
                            ('ALIGN', (-7,-2), (-7,-1), 'CENTER'),
                            ('ALIGN', (-5,-2), (-5,-1), 'CENTER'),
                            ('ALIGN', (-4,-2), (-4,-1), 'CENTER'),
                            ('ALIGN', (-3,-2), (-3,-1), 'CENTER'),
                            ('ALIGN', (-2,-2), (-2,-1), 'CENTER'),
                            ('ALIGN', (-1,-2), (-1,-1), 'CENTER'),
                            ('ALIGN', (3,4), (3,3), 'CENTER'),
                            ('ALIGN', (3,4), (3,3), 'CENTER'),
                            ('VALIGN', (-7,-2), (-1,-2), 'MIDDLE'),
                            ('LINEABOVE',(-7,-1),(-1,-1),0.5,colors.black)
                            ]))

story.append(table5)
story.append(Spacer(1, 25))

#story.append(PageBreak())

#### GRAPH ####

story.append(Paragraph('<font >measurement data </font>', Sublines2))
story.append(Spacer(1,0))

im2 = Image(plot, 250, 200, hAlign='LEFT')
story.append(im2)
story.append(Spacer(1,15))



#### SAVE ####
doc.build(story, onFirstPage=addPageNumber, onLaterPages=addPageNumber)

