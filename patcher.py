#!/usr/bin/python3
import tkinter as tk
import os
import Constants
from Gui import PatcherApp
from Functions import check_rom, show_warning

tools_path = os.path.join('.', 'tools')
alt_path = os.path.join(tools_path, 'alt')

if __name__ == "__main__":
    
    if not os.path.isdir(alt_path):
        show_warning(Constants.WARNING_EXTRACT)
        exit()

    baserom = None
    for file in os.listdir('.'):
        if file.lower().endswith('.gba'):
            filename = os.path.join('.', file)
            if(check_rom(filename)):
                baserom = filename
    
    root = tk.Tk()
    app = PatcherApp(root, baserom)
    app.run()
