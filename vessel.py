# List of Lists
data = [
    ['number', 'vessel type', 'volume', 'unit' ],
    ['1', 'falcon tube', '50', 'mL'],
    ['2', 'eppendorf tube', '1.5', 'mL'],
    ['3', 'shake flask', '1000', 'mL']
]

fileName = 'Vessel.pdf'

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
)

from reportlab.platypus import Table
table = Table(data, colWidths=[1.9*inch] * 4)

# add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors

style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),

    ('ALIGN',(0,0),(-1,-1),'CENTER'),

    ('FONTNAME', (0,0), (-1,0), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,0), 12),

    ('BOTTOMPADDING', (0,0), (-1,0), 12),

    ('BACKGROUND',(0,1),(-1,-1),colors.lightgrey),
])
table.setStyle(style)

# 2) Alternate backgroud color
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.lightgrey
    else:
        bc = colors.whitesmoke
    
    ts = TableStyle(
        [('BACKGROUND', (0,i),(-1,i), bc)]
    )
    table.setStyle(ts)

# 3) Add borders
ts = TableStyle(
    [
    ('BOX',(0,0),(-1,-1),0.5,colors.black),

    ('GRID',(0,1),(-1,-1),0.5,colors.black),
    ]
)
table.setStyle(ts)

elems = []
elems.append(table)

pdf.build(elems)