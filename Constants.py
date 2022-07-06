#!/usr/bin/python3
import os
from sys import platform

PATCH_VERSION = '1.1.1'
FINAL_ROM_NAME = f'Mother 1+2 [T+Ita{PATCH_VERSION}].gba'

STATUS_PRESET = "Preset applicato" # Niente punto qui
STATUS_START = "Patcher pronto all'uso."
STATUS_MD5 = "MD5 verificato."
STATUS_COPIED = "File copiati."
STATUS_ASSEMBLY = "Codice compilato."
STATUS_INJECTED = "Testo inserito."
STATUS_PATCHED = "Patch applicate."
STATUS_CLEANED = "Pulizia effettuata."

VAR_WINDOW_TITLE = "Mother 1+2 Patcher by Earthbound Café"
VAR_FILEPICKER = "ROM giapponese di Mother 1+2"

WARNING_TITLE = "Attenzione"
WARNING_EXTRACT = "È necessario estrarre l'archivio."
WARNING_MD5_MISMATCH = "La ROM selezionata non è compatibile con la nostra patch."

SUCCESS_TITLE = "Finito!"
SUCCESS_CONTENT = f"La ROM {FINAL_ROM_NAME} è stata creata con successo!"

PATH_TOOLS = os.path.join('.', 'tools')
PATH_ALT = os.path.join(PATH_TOOLS, 'alt')

PRESETS = {
    "Scelte consigliate": { # default preset
        'font': 'font_og',
        'sprites': 'sprites_mix',
        'places': 'places_us',
        'nes_palette': 'nes_palette_yes',
        'skip_m1': 'skip_m1_yes'
        },
    "Earthbound Beginnings (US)": {
        'font': 'font_og',
        'sprites': 'sprites_us',
        'places': 'places_us',
        'nes_palette': 'nes_palette_yes',
        'skip_m1': 'skip_m1_yes'
        },
    "Mother 1 (JP)": {
        'font': 'font_og',
        'sprites': 'sprites_jp',
        'places': 'places_jp',
        'nes_palette': 'nes_palette_yes',
        'skip_m1': 'skip_m1_yes'
        },
    "Mother 1+2": {
        'font': 'font_og',
        'sprites': 'sprites_us',
        'places': 'places_jp',
        'nes_palette': 'nes_palette_no',
        'skip_m1': 'skip_m1_no'
        }
}

ALT_FILENAMES = {
    'font_og':
        ['m1_gfx_font_og.bin'],
    'font_new':
        ['m1_gfx_font_new.bin'],
    'sprites_mix':
        ['m1_restoration_gfx_sprites_mix.bin',
        'm1_restoration_gfx_ending_us.bin',
        'm1_restoration_gfx_enemies_jp.bin',
        'm1_restoration_gfx_maptiles_jp.bin'],
    'sprites_us':
        ['m1_restoration_gfx_sprites_us.bin',
        'm1_restoration_gfx_ending_us.bin',
        'm1_restoration_gfx_enemies_us.bin',
        'm1_restoration_gfx_maptiles_us.bin'],
    'sprites_jp':
        ['m1_restoration_gfx_sprites_jp.bin',
        'm1_restoration_gfx_ending_jp.bin',
        'm1_restoration_gfx_enemies_jp.bin',
        'm1_restoration_gfx_maptiles_jp.bin'],
    'places_us':
        ['m1_main_text_us.txt',
        'm1_gfx_map_us.bin'],
    'places_jp':
        ['m1_main_text_jp.txt',
        'm1_gfx_map_jp.bin'],

    'nes_palette_yes': 'nes.ips',
    'nes_palette_no': None,
    'skip_m1_yes': 'skipm1.ips',
    'skip_m1_no': None
}

DEF_FILENAMES = {
    'font': [
        'm1_gfx_font.bin'
    ],
    'sprites': [
        'm1_restoration_gfx_sprites.bin',
        'm1_restoration_gfx_ending.bin',
        'm1_restoration_gfx_enemies.bin',
        'm1_restoration_gfx_maptiles.bin'
    ],
    'places': [
        'm1_main_text.txt',
        'm1_gfx_map.bin'
    ]
}

DEF_PRESET = next(iter(PRESETS.items()))
DEF_PATCHES = DEF_PRESET[1].keys() - DEF_FILENAMES.keys()

OS_SUFFIX = (
    '.exe' if platform.startswith('win32') else
    '_mac' if platform.startswith('darwin')
    else ''
)

OS_FILENAMES = {
    'xkas': os.path.join('.', 'xkas' + OS_SUFFIX),
    'insert': os.path.join('.', 'insert' + OS_SUFFIX),
    'introconv': os.path.join('.', 'introconv' + OS_SUFFIX)
}

OS_SHELL = True if os.name == 'nt' else False
