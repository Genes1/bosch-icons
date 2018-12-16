from PIL import Image
import random
import argparse
import os
parser = argparse.ArgumentParser()

parser.add_argument('size', type=int, help='Desired size of images (only one argument, as the result will be square).')
parser.add_argument('num', type=int, help='Number of images to be produced.')
args = parser.parse_args()
globals().update(vars(args))

im = Image.open("source.jpg")

sectiondiv = [
                [0, 1768-size],
                [2287, 6276-size],
                [6763, 8533-size],
            ]

if not os.path.exists('section'):
    os.makedirs('section')
    
for i in range(num):
    section = int(random.random() / (1/3) )                             # get section 0, 1, 2
    x = random.randint(sectiondiv[section][0], sectiondiv[section][1])  # select random x in reange from section
    y = random.randint(0, 4292-size)                                    # get random y point from y size 
    crop_rectangle = (x, y, x+size, y+size)
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save("section/section" + str(i+1) + ".png")
    
