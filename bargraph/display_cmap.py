import click
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


@click.command()
@click.option('--cmap', help='cmap', default="YlOrBr")
@click.option('--show/--no-show', help='Show plot', default=True)
def main(cmap, show):
    a = np.outer(np.arange(0, 1, 0.01), np.ones(10))
    cmap = matplotlib.cm.get_cmap(cmap)
    plt.imshow(a, aspect='auto', cmap=cmap)
    if show:
        plt.show()


if __name__ == '__main__':
    main()
