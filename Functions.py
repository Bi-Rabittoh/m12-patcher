#!/usr/bin/python3
from hashlib import md5
from tkinter.messagebox import showwarning
import Constants

def check_rom(filename):
    if filename == '':
        return False
    with open(filename, 'rb') as f:
        file_hash = md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest() == 'f41e36204356974c94fabf7d144dd32a'

def show_warning(message):
    showwarning(title=Constants.WARNING_TITLE, message=message)