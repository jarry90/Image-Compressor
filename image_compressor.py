import sys
from PIL import Image

size = 1000, 1000

infile = sys.argv[1]
outfile = infile.split(".")[0] + "-resized.jpeg"
try:
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile, "JPEG")
    print("All Good!")
except IOError:
    print("cannot create thumbnail for '%s'" % infile)