import tkinter as tk

import numpy as np

from matplotobjlib import Graph, SubPlot, TkFigure

ts = np.arange(0, 10, 0.01)
xs = [t * np.cos(t) for t in ts]
ys = [t * np.sin(t) for t in ts]

root = tk.Tk()
widget = TkFigure(
    root, [[SubPlot(Graph(xs, ys, plot_type="-"), x_label="t*cos(t)", y_label="t*sin(t)")]], title="examples/widget.py"
)
widget.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
