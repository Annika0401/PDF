from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing #, string
from reportlab.graphics.charts.textlabels import Label


elements = []

table1 = [[34,27,35,35],
          [3,76,23,157],
          [13,137,15,75],
          [56,26,46,26]]




t1 = Table(table1)
for ii in range(len(table1)):
    for jj in range(len(table1)):
        if table1[jj][ii] <=50:
            ourcolor = colors.white
        elif table1[ii][jj] <=100:
            ourcolor = colors.skyblue
        elif table1[ii][jj] <=200:
            ourcolor = colors.green

        else:
            ourcolor = colors.white
        t1.setStyle(TableStyle([('BACKGROUND', (ii,jj), (ii,jj), ourcolor),
                                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                ('BOX', (0,0), (-1,-1), 0.25, colors.black)
                                ]))

elements.append(t1)


#build our document with the list of flowables we put together
doc = SimpleDocTemplate('Versuch.pdf',pagesize = letter, topMargin=0)
doc.build(elements)