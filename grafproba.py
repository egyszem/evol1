from PIL import Image, ImageDraw

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
draw.line(((0, 1600), (500, 400), (1800, 1400), (2000, 0)), fill=255, width=40, joint="curved")
del draw
im.show()