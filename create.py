# Prints the Certificate for a given name
from PIL import Image, ImageDraw, ImageFont


def make(name, course, year, template):
    font_0 = ImageFont.truetype(r'OPTITimes-Roman.otf', 50)
    font_1 = ImageFont.truetype(r'OPTITimes-Roman.otf', 20)
    font_2 = ImageFont.truetype(r'OPTITimes-Roman.otf', 20)
    color = "#000000"

    width, height = 483, 311
    width_1, height_1 = 571, 456
    width_2, height_2 = 586, 496

    image = Image.open(template, mode='r')
    draw = ImageDraw.Draw(image)
    name_width, name_height = draw.textsize(name, font=font_0)
    course_width, course_height = draw.textsize(course, font=font_1)
    year_width, year_height = draw.textsize(year, font=font_2)

    draw.text((width - name_width / 2, height - name_height / 2), name, fill=color, font=font_0)
    draw.text((width_1 - course_width / 2, height_1 - course_height / 2), course, fill=color, font=font_1)
    draw.text((width_2 - year_width / 2, height_2 - year_height / 2), year, fill=color, font=font_2)

    image.save("./Output/%s.jpg" % name)



