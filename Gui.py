#!/usr/bin/python3
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pathlib, pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "patcher.ui"

presets = {
    "Scelte consigliate": {
        'font': 1,
        'sprites': 3,
        'places': 6,
        'palette': 8,
        'skip_m1': 1
        },
    "EB Beginnings (US)": {
        'font': 1,
        'sprites': 4,
        'places': 6,
        'palette': 8,
        'skip_m1': 1
        },
    "Mother 1 (JP)": {
        'font': 1,
        'sprites': 5,
        'places': 7,
        'palette': 8,
        'skip_m1': 1
        },
    "Mother 1+2": {
        'font': 1,
        'sprites': 4,
        'places': 7,
        'palette': 9,
        'skip_m1': 0
        }
}

class PatcherApp:
    def __init__(self, master=None):
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
            ],
        )
        self.font.set(1)
        self.sprites.set(3)
        self.places.set(6)
        self.palette.set(8)
        self.skip_m1.set(1)
        
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_browse_button(self):
        fn = askopenfilename(filetypes=[('ROM giapponese di Mother 1+2', '*.gba'), ('Tutti i file', '*')])
        self.browse_path.set(fn)

    def on_change_preset(self, option):
        new_vars = presets[option]
        
        for key in new_vars.keys():
            getattr(self, key).set(new_vars[key])

    def on_apply_button(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = PatcherApp(root)
    app.run()
