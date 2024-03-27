import sys

from PIL import Image

images = []

for arg in sys.arg[1:]v:
    image = Image.open(arg)
    images.append(image)

image[0].save(
    "costumes.gif", save_all=True, append_images=[images[images[1]], duration=200, loop=0]
)