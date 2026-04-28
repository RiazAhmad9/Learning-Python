"""
shirt.py
--------
Overlays shirt.png on top of a user-provided photo after resizing/cropping
the photo to match shirt.png's dimensions. Accepts exactly two CLI args:
input image path and output image path. Both must be .jpg/.jpeg/.png with
matching extensions.
"""
import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    in_ext = os.path.splitext(in_path)
    out_ext = os.path.splitext(out_path)
    extension = {".jpg", ".jpeg", ".png"}

    if in_ext[1].lower() in extension and out_ext[1].lower() in extension:
        if os.path.exists(in_path):
            if in_ext[1].lower() == out_ext[1].lower():
                shirt = Image.open("shirt.png")
                photo = Image.open(in_path)
                photo = ImageOps.fit(photo, shirt.size)
                photo.paste(shirt, shirt)
                photo.save(out_path)
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit(f"{in_path} does not exist")
    else:
        sys.exit("Invalid input")
    


if __name__ == "__main__":
    main()