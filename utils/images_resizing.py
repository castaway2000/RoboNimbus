import os
import sys

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimize_size(initial_image, size):

    size_dict = {
        "xsmall": 50,
        "small": 320,
        "medium": 640,
        "large": 1680
    }

    image_file = initial_image.file
    image_name = initial_image.name

    image_file.seek(0)

    image = Image.open(image_file)

    width, height = image.size
    target_width = size_dict[size]

    ratio = width/float(target_width)
    target_height = height/ratio

    image.thumbnail((target_width, target_height), Image.ANTIALIAS)
    output = BytesIO()
    try:
        quality = 100
        image.save(output, format='JPEG', quality=quality)
        output.seek(0)
        img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % image_name.split(".")[0],
                                          'image/jpeg', sys.getsizeof(output), None)
    except:
        image.convert('RGB').save(output, format='JPEG', quality=quality)
        output.seek(0)
        img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % image_name.split(".")[0],
                                          'image/jpeg', sys.getsizeof(output), None)
    return img