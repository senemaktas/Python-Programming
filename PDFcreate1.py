from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("pdfNAme.pdf", pagesize=LETTER)

# Set font to Timees New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

#Draw blue text one inch from the left and ten inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "It will show up on the pdf page.")

#Save the PDF file
canvas.save()