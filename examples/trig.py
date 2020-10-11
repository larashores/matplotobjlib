import numpy as np

from matplotobjlib import Graph, SubPlot, draw

xs = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
draw(
    [
        [
            SubPlot(Graph(xs, np.sin(xs), plot_type="-"), x_label="x", y_label="sin(x)"),
            SubPlot(Graph(xs, np.cos(xs), plot_type="-"), x_label="x", y_label="cos(x)"),
        ],
        [
            SubPlot(Graph(xs, np.tan(xs), plot_type="-"), x_label="x", y_label="tan(x)"),
            SubPlot(Graph(xs, np.arcsin(xs), plot_type="-"), x_label="x", y_label="sin$^{-1}$(x)"),
        ],
    ],
    title="examples/trig.py",
)
