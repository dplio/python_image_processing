import sys
import os
import re
from PIL import Image

# take command line args to convert folder of jpg images to new folder of png images
# print(sys.argv[1], sys.argv[2])

# below makes a directory in the current folder for us
# os.mkdir(sys.argv[2])


# below returns a list of image files
# print(os.listdir('./sneakers'))

def jpg_file_list(f):
    return os.listdir(f)


def create_png_folder(f):
    if not os.path.exists(f):
        os.mkdir(f)
    return str(f"./{f}")


def convert(source, images, destination):
    ext_pattern = re.compile(r'^.*(.jpg|.jpeg|.JPG|.JPEG)$')
    for file_name in images:
        if ext_pattern.match(file_name):
            img = Image.open(f"./{source}{file_name}")
            new_name = file_name.replace(
                ext_pattern.match(file_name).group(1),
                ".png"
            )
            img.save(f"{destination}{new_name}")


if __name__ == "__main__":
    convert(
        sys.argv[1],
        jpg_file_list(sys.argv[1]),
        create_png_folder(sys.argv[2])
    )
