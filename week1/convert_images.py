#!/usr/bin/env python3

import os
import re
import subprocess
from PIL import Image

input_dir = 'images'
if not os.path.exists(input_dir):
    subprocess.run(["unzip", "images.zip"])

img_list = os.listdir('./images')
output_dir = 'icons/'
if not os.path.exists(output_dir):
    os.mkdir('icons')

for img in img_list:
    if not img.startswith('.'):
        img_location = os.path.join('./images', img)

        # open images using Image module and open function
        with Image.open(img_location) as im:
            # print(im.format, im.mode)

            # Rotate the image 90° clockwise
            im = im.rotate(-90)

            # Resize the image from 192x192 to 128x128
            im = im.resize((128, 128))

            # Store mode of the image
            old_mode = im.mode
            if old_mode == "LA":

                # Match if the image is white
                if re.match(r'.*_white_48dp$', img):
                    background = Image.new(
                        old_mode[:-1], im.size, 'black')
                    background.paste(im, im.getchannel('A'))
                    image = background
                    # Save the image in jpeg format
                    image.save("{}{}.jpeg".format(output_dir, img))

                # For the black image
                else:
                    background = Image.new(
                        old_mode[:-1], im.size, 'white')
                    background.paste(im, im.getchannel('A'))
                    image = background
                    # Save the image in jpeg format
                    image.save("{}{}.jpeg".format(output_dir, img))

            elif old_mode == "P":
                # PIL loses palette attribute during crop. So we use low-level api.
                # Returns true if palette is RGBA or LA
                alpha = 'A' in im.im.getpalettemode()
                image = im.convert('RGBA' if alpha else 'RGB')
                # Save the image in jpeg format
                image.save("{}{}.jpeg".format(output_dir, img))

            elif old_mode == "1":
                # Save the image in jpeg format
                im.save("{}{}.jpeg".format(output_dir, img))
