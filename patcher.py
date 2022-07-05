#!/usr/bin/python3
import tkinter as tk
import os
from hashlib import md5
from Gui import PatcherApp

m12_md5 = 'f41e36204356974c94fabf7d144dd32a'
tools_path = os.path.join('.', 'tools')
alt_path = os.path.join(tools_path, 'alt')

def check_rom(filename):
    with open(filename, 'rb') as f:
        file_hash = md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest() == m12_md5

if __name__ == "__main__":
    
    if not os.path.isdir(alt_path):
        print('\nErrore: è necessario estrarre l\'archivio.')
        exit()

    baserom = None
    for file in os.listdir('.'):
        if file.endswith('.gba'):
            filename = os.path.join('.', file)
            if(check_rom(filename)):
                baserom = filename
    
    root = tk.Tk()
    app = PatcherApp(root)
    app.run()
