#!/usr/bin/python3
import os, tkinter, Constants
from tkinter.filedialog import askopenfilename
from Functions import check_rom, show_warning, start_patching, apply_preset, set_progress
from pathlib import Path
from pygubu import Builder

PROJECT_PATH = Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "patcher.ui"

class PatcherApp:
    def __init__(self, master=None):
        self.builder = builder = Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("main_frame", master)
        self.apply_button = builder.get_object("apply_button")
        self.preset_combo = builder.get_object("preset_combo")
        
        self.browse_path = None
        self.preset = None
        self.progress = None
        self.status_text = None
        self.font = None
        self.places = None
        self.sprites = None
        self.nes_palette = None
        self.skip_m1 = None
        builder.import_variables(
            self,
            [
                "browse_path",
                "preset",
                "progress",
                "status_text",
                "font",
                "places",
                "sprites",
                "nes_palette",
                "skip_m1",
            ],
        )
        
        for preset in Constants.PRESETS.keys():
            self.preset_combo['values'] = (*self.preset_combo['values'], preset)
        self.preset.trace('w', self.on_change_preset)
        self.preset.set(Constants.DEF_PRESET[0])
        self.status_text.set(Constants.STATUS_START)
        
        baserom = None
        for file in os.listdir('.'):
            if file.lower().endswith('.gba'):
                filename = os.path.join('.', file)
                baserom = filename if check_rom(filename) else baserom
        if baserom is not None:
            self.browse_path.set(baserom)
        
        builder.connect_callbacks(self)
    
    def run(self):
        self.mainwindow.mainloop()

    def on_browse_button(self):
        fn = askopenfilename(filetypes=[(Constants.VAR_FILEPICKER, '*.gba')])
        self.browse_path.set(fn)
    
    def on_change_preset(self, *arg):
        preset = self.preset.get()
        if apply_preset(self, preset):
            set_progress(self, 0, f'{Constants.STATUS_PRESET}: {preset}.')

    def on_apply_button(self):
        self.apply_button['state'] = 'disabled'
        
        baserom_temp = self.browse_path.get()
        
        if not check_rom(baserom_temp):
            show_warning(Constants.WARNING_MD5_MISMATCH)
            self.apply_button['state'] = 'normal'
            return
        self.baserom = baserom_temp
        start_patching(self)
        self.apply_button['state'] = 'enabled'
        set_progress(self, 0, Constants.STATUS_START)

def main():
    if not os.path.isdir(Constants.PATH_TOOLS):
        show_warning(Constants.WARNING_EXTRACT)
        return
    
    root = tkinter.Tk()
    root.title(Constants.VAR_WINDOW_TITLE)
    root.resizable(False, False)
    app = PatcherApp(root)
    app.run()

if __name__ == "__main__":
    main()
