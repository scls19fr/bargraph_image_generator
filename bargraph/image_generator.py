#!/usr/bin/env python

import click
import os
from PIL import Image
import matplotlib
import matplotlib.cm
import colorsys


def to_color_bytes(red, green, blue, alpha):
    return int(red * 255), int(green * 255), int(blue * 255), int(alpha * 255)


@click.command()
@click.option('--width', help='Width', default=480)
@click.option('--height', help='Height', default=40)
@click.option('--cmap', help='cmap', default="YlOrBr")
@click.option('--darken', help='darken (1:dark 0:bright)', default=0.8)
@click.option('--outdir', help='output directory', default='output/sample')
def main(width, height, cmap, darken, outdir):
    mode = "RGB"
    backcolor = "white"
    im1 = Image.new(mode, (width, height), backcolor)
    im2 = Image.new(mode, (width, height), backcolor)

    cmap = matplotlib.cm.get_cmap(cmap)

    for x in range(width):
        color = cmap(x / width)  # rgba
        red, green, blue, alpha = color

        color_bytes1 = to_color_bytes(red, green, blue, alpha)

        hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
        lightness = lightness * (1 - darken)
        red, green, blue = colorsys.hls_to_rgb(hue, lightness, saturation)

        color_bytes2 = to_color_bytes(red, green, blue, alpha)

        for y in range(height):
            im1.putpixel((x, y), color_bytes1)  # place the pixel
            im2.putpixel((x, y), color_bytes2)  # place the pixel

    im1.save(os.path.join(outdir, "bargraph_foreground.png"))
    im2.save(os.path.join(outdir, "bargraph_background.png"))


if __name__ == '__main__':
    main()
