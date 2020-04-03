from django.utils.deconstruct import deconstructible
from pathlib import Path
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, instance, filename):
        slug = instance.slug
        filename = '{}_{}'.format(self.field_name, filename)
        return "blog/{}/{}".format(slug, filename)