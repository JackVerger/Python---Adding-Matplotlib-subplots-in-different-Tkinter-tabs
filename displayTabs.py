
############
# PACKAGES #
############

# Tkinter
import tkinter
from tkinter import ttk

# Matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

# Numpy
import numpy as np



    #############
    # VARIABLES #
    #############

different_figures = []
different_frames = []
tabs_number = 3
x_data1 = [1, 2, 3]
y_data1 = [1, 2, 3]
x_data2 = [1, 2, 3, 4, 5, 6]
y_data2 = [1, 2, 3, 4, 5, 6]
x_data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]



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

# Creation of the window close button
button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

# Creation of the notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack()

# Creation of all the frames (depends on the number of tabs)
for i in range(tabs_number) :
    
    # Creation of the frame 
    different_frames.append(tkinter.LabelFrame(root, padx=5, pady=5, width=500, height=500))
    different_frames[i].pack()
    
    # add the frame in the notebook, linking it to a specific tab
    my_notebook.add(different_frames[i], text='tab %d' % (i+1))

# Creation of the matplotlib figures
for i in range(tabs_number) :
    different_figures.append(Figure(figsize=(5, 4), dpi=100))

# Customization of the figures (can be automated during the previous figure creation loop)
different_figures[0].add_subplot(211).plot(x_data1, y_data1) # First tab figure
different_figures[1].add_subplot(211).plot(x_data2, y_data2) # Second tab figure
different_figures[2].add_subplot(211).plot(x_data3, y_data3) # Third tab figure

# Implementation of the figures in their respective frames
for i in range(tabs_number) :

    # Implementation of the figure in the frame
    canvas = FigureCanvasTkAgg(different_figures[i], master=different_frames[i])  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    # Implementation of the toolbar of the figure
    toolbar = NavigationToolbar2Tk(canvas, different_frames[i])
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Mainloop of the Tkinter window
tkinter.mainloop()
