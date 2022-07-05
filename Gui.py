#!/usr/bin/python3
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pathlib
import pygubu
import Constants
from Functions import check_rom, show_warning

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "patcher.ui"

class PatcherApp:
    def __init__(self, master=None, baserom=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("main_frame", master)

        self.browse_path = None
        self.preset = None
        self.font = None
        self.places = None
        self.sprites = None
        self.palette = None
        self.skip_m1 = None
        self.progress = None
        self.progress_text = None
        builder.import_variables(
            self,
            [
                "browse_path",
                "preset",
                "font",
                "places",
                "sprites",
                "palette",
                "skip_m1",
                "progress",
                "progress_text",
            ],
        )
        self.font.set(1)
        self.sprites.set(3)
        self.places.set(6)
        self.palette.set(8)
        self.skip_m1.set(1)
        self.progress_text.set(Constants.STATUS_START)
        
        self.apply_button = builder.get_object("apply_button")
        
        if baserom is not None:
            self.browse_path.set(baserom)
        
        builder.connect_callbacks(self)
    
    def set_progress(self, percent, message):
        self.progress.set(percent)
        self.progress_text.set(message)

    
    
    def run(self):
        self.mainwindow.mainloop()

    def on_browse_button(self):
        fn = askopenfilename(filetypes=[(Constants.VAR_FILEPICKER, '*.gba')])
        self.browse_path.set(fn)

    def on_change_preset(self, option):
        new_vars = Constants.PRESETS[option]
        self.set_progress(0, Constants.STATUS_PRESET)
        
        for key in new_vars.keys():
            getattr(self, key).set(new_vars[key])

    def on_apply_button(self):
        self.apply_button['state'] = 'disabled'
        
        if check_rom(self.browse_path.get()):
            self.set_progress(20, Constants.STATUS_MD5)
        else:
            show_warning(Constants.WARNING_MD5_MISMATCH)
            self.apply_button['state'] = 'normal'