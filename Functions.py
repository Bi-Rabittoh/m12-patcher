#!/usr/bin/python3
from hashlib import md5
from tkinter.messagebox import showwarning, showinfo
from ips_util import Patch
from shutil import copyfile
import os, subprocess, Constants

def check_rom(filename):
    if filename == '':
        return False
    with open(filename, 'rb') as f:
        file_hash = md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest() == 'f41e36204356974c94fabf7d144dd32a'

def apply_preset(app, preset):
    for key in preset.keys():
            getattr(app, key).set(preset[key])

def apply_patch(base, ips):
    patch = Patch.load(ips)
    target = base + '_temp'

    with open(base, 'rb') as f_in:
        with open(target, 'w+b') as f_out:
            f_out.write(patch.apply(f_in.read()))

    os.replace(target, base)

def show_warning(message):
    showwarning(title=Constants.WARNING_TITLE, message=message)
    
def show_success(message):
    showinfo(title=Constants.SUCCESS_TITLE, message=message)

def set_progress(app, percent, message):
    app.progress.set(percent)
    app.progress_text.set(message) 

def start_patching(app):
    set_progress(app, 20, Constants.STATUS_MD5)
    delete_list = []
    
    sel_filenames = {
        'font': Constants.ALT_FILENAMES[app.font.get()],
        'sprites': Constants.ALT_FILENAMES[app.sprites.get()],
        'places': Constants.ALT_FILENAMES[app.places.get()]
    }
    
    sel_patches = {
        'palette': Constants.ALT_FILENAMES[app.palette.get()],
        'skip_m1': Constants.ALT_FILENAMES[app.skip_m1.get()]
    }
    
    for key in sel_filenames.keys():
        sel_list = sel_filenames[key]
        def_list = Constants.DEF_FILENAMES[key]

        for idx, i in enumerate(sel_list):
            original = os.path.join(Constants.PATH_ALT, sel_list[idx])
            target = os.path.join(Constants.PATH_TOOLS, def_list[idx])
            
            copyfile(original, target)
            delete_list.append(target)
            
    target = os.path.join(Constants.PATH_TOOLS, 'test.gba')
    copyfile(app.baserom, target)
    
    set_progress(app, 40, Constants.STATUS_COPIED)
    p = subprocess.Popen([Constants.OS_FILENAMES['xkas'], '-o', 'test.gba', 'm12.asm'],
                         cwd=Constants.PATH_TOOLS, shell=Constants.OS_SHELL)
    p.wait()

    set_progress(app, 50, Constants.STATUS_ASSEMBLY)
    p = subprocess.Popen([Constants.OS_FILENAMES['insert']],
                         cwd=Constants.PATH_TOOLS, shell=Constants.OS_SHELL)
    p.wait()
       
    set_progress(app, 70, Constants.STATUS_INJECTED)
    for key in sel_patches.keys():
        val = sel_patches[key]
        
        if val is not None:
            path = os.path.join(Constants.PATH_ALT, val)
            apply_patch(target, path)
        
    os.replace(target, Constants.FINAL_ROM_NAME)
       
    set_progress(app, 90, Constants.STATUS_PATCHED)
    for item in delete_list:
        os.remove(item)

    set_progress(app, 100, Constants.STATUS_CLEANED)
    show_success(Constants.SUCCESS_CONTENT)
    