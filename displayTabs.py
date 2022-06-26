import tkinter
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


# Création de la fenêtre
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# Création du notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack()

# Création des frames
frame1 = tkinter.LabelFrame(root, padx=5, pady=5, width=500, height=500)
frame1.pack()
frame2 = tkinter.LabelFrame(root, padx=5, pady=5, width=500, height=500)
frame2.pack()

# Implémentation des frames dans le notebook
my_notebook.add(frame1, text="blue tab")
my_notebook.add(frame2, text="red tab")

# Création de la figure
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# Implémentation de la figure dans la fenêtre tkinter
canvas = FigureCanvasTkAgg(fig, master=frame1)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Implémentation de la toolbar de la figure
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
