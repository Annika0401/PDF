from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Frame, PageTemplate, KeepInFrame
from reportlab.lib.units import cm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)

########################################################################

def create_pdf():
    """
    Create a pdf
    """

    # Create a frame
    text_frame = Frame(
        x1=3.00 * cm,  # From left
        y1=1.5 * cm,  # From bottom
        height=19.60 * cm,
        width=15.90 * cm,
        leftPadding=0 * cm,
        bottomPadding=0 * cm,
        rightPadding=0 * cm,
        topPadding=0 * cm,
        showBoundary=1,
        id='text_frame')

    # Create a table
    test_table = []
    data = []
    for i in range(11, 1, -1):
        column1data = f'Column_1 on row {i}'
        column2data = f'Column_2 on row {i}'
        data.append([column1data, column2data])

    data_table = Table(data, 15.90 * cm / 2)
    data_table.setStyle(TableStyle([
        # Title
        ('LEFTPADDING', (0, 0), (1, 0), 0),
        ('RIGHTPADDING', (0, 0), (1, 0), 0),
        ('VALIGN', (0, 0), (1, 0), 'TOP'),
        ('ALIGN', (0, 0), (1, 0), 'CENTRE'),
        # DataTable
        ('ALIGN', (0, 1), (1, -1), 'CENTRE'),
        ('SIZE', (0, 1), (-1, -1), 7),
        ('LEADING', (0, 1), (-1, -1), 8.4),
        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 2.6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 2.6),
        ('LINEBELOW', (0, 1), (-1, -1), 0.3, colors.gray),
    ]))

    test_table.append(data_table)
    test_table = KeepInFrame(0, 0, test_table, mode='overflow')

    # Building the story
    story = [test_table] # adding test_table table (alternative, story.add(test_table))

    # Establish a document
    doc = BaseDocTemplate("Example_output.pdf", pagesize=letter)

    # Creating a page template
    frontpage = PageTemplate(id='FrontPage',
                             frames=[text_frame]
                             )
    # Adding the story to the template and template to the document
    doc.addPageTemplates(frontpage)

    # Building doc
    doc.build(story)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_pdf() # Printing the pdf