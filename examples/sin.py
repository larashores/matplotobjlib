import numpy as np

from matplotobjlib import Graph, SubPlot, draw

xs = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
ys = np.sin(xs)
draw(SubPlot(Graph(xs, ys, plot_type="-"), x_label="x", y_label="sin(x)"), title="examples/sin.py")
