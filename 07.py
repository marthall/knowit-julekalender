from scipy.misc import imread
from collections import Counter

image = imread('santa.png')

c = Counter()

for row in image:
    for pixel in row:
        pixel_hash = "%i, %i, %i, %i" % tuple(pixel)
        c[pixel_hash] += 1

print c.most_common(10)[-1]

