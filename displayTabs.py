
    ############
    # PACKAGES #
    ############

# Tkinter
import tkinter
from tkinter import ttk

# Matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# Numpy
import numpy as np



    ###############
    # SUBROUTINES #
    ###############

# Subroutine to close the window
def _quit() :
    
    # Stops mainloop
    root.quit() 

    # Prevent fatal Python Error: PyEval_RestoreThread: NULL tstate              
    root.destroy() 
         
        

    ################
    # MAIN PROGRAM #
    ################

# Creation of the window
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# Creation of the notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack()

# Creation of the frames
frame1 = tkinter.LabelFrame(root, padx=5, pady=5, width=500, height=500)
frame1.pack()
frame2 = tkinter.LabelFrame(root, padx=5, pady=5, width=500, height=500)
frame2.pack()
# You can add more if you want

# Implementation of the frames in the notebook
my_notebook.add(frame1, text="first tab")
my_notebook.add(frame2, text="second tab")

# Creation of the window close button
button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

# Creation of the matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# Implementation of the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=frame1)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Implementation of the toolbar of the figure
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Mainloop of the Tkinter window
tkinter.mainloop()
