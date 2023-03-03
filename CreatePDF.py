from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, Circle
from reportlab.pdfgen import canvas
from PIL import Image


# Which image to use
im = Image.open("Input_image.jpg")

# The size of each square
cm = 3 #cm

# Translation from centimeters to pixels
pixels_from_cm = cm * 28.35

# The size of circles in corner of the squares
circle_radius = 1.0 #mm

# Translation from centimeters to pixels
circle_radius = circle_radius*0.1*28.35

# Pixel data
width, height = im.size
num_rectangles = width*height
rect_width = pixels_from_cm
rect_height = pixels_from_cm
rect_spacing = 20
rect_per_line = 5
rect_per_page = rect_per_line*7


# Create a new PDF with Reportlab
c = canvas.Canvas("output_A4_PDF.pdf", pagesize=A4)

# Number of rectangles drawn so far
rect_count = 0
x = 0
y = 0
firstRun = True

print('height: ',height)
print('width: ',width)


for i in range(num_rectangles):
    # Create a red rectangle without black outline
    if not firstRun:
        if x % width == 0:
            x = 0
            y += 1
    r, g, b = im.getpixel((x, y))
    r = Rect((rect_count % rect_per_line) * (rect_width + rect_spacing), (rect_count // rect_per_line) * (rect_height + rect_spacing), rect_width, rect_height, fillColor=colors.Color(r/256,g/256,b/256), strokeColor=None)
    cic1 = Circle((rect_count % rect_per_line) * (rect_width + rect_spacing)+(28.35*0.4), (rect_count // rect_per_line) * (rect_height + rect_spacing)+(28.35*0.4), circle_radius, fillColor=colors.white)
    cic2 = Circle((rect_count % rect_per_line) * (rect_width + rect_spacing)+(28.35*0.4)+(2.2*28.35), (rect_count // rect_per_line) * (rect_height + rect_spacing)+(28.35*0.4), circle_radius, fillColor=colors.white)
    cic3 = Circle((rect_count % rect_per_line) * (rect_width + rect_spacing)+(28.35*0.4), (rect_count // rect_per_line) * (rect_height + rect_spacing)+(28.35*0.4)+(2.2*28.35), circle_radius, fillColor=colors.white)
    cic4 = Circle((rect_count % rect_per_line) * (rect_width + rect_spacing)+(28.35*0.4)+(2.2*28.35), (rect_count // rect_per_line) * (rect_height + rect_spacing)+(28.35*0.4)+(2.2*28.35), circle_radius, fillColor=colors.white)
    d = Drawing(100, 100)
    d.add(r)
    d.add(cic1)
    d.add(cic2)
    d.add(cic3)
    d.add(cic4)
    d.drawOn(c, 20, 20)
    rect_count += 1
    x += 1
    firstRun = False
    # If rectangles per page is reached, start a new page
    if rect_count % rect_per_page == 0:
        c.showPage()
        rect_count = 0

c.save()