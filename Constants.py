#!/usr/bin/python3
import os
from sys import platform

PATCH_VERSION = '1.1.1'
FINAL_ROM_NAME = f'Mother 1+2 [T+Ita{PATCH_VERSION}].gba'

STATUS_START = "Benvenutə al patcher per Mother 1+2."
STATUS_PRESET = "Preset applicato."
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

PATH_TOOLS = os.path.join('.', 'tools')
PATH_ALT = os.path.join(PATH_TOOLS, 'alt')

PRESETS = {
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

DEF_FILENAMES = {
    'font': ['m1_gfx_font.bin'],
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

ALT_FILENAMES = {
    1: ['m1_gfx_font_og.bin'],

    2: ['m1_gfx_font_new.bin'],

    3: ['m1_restoration_gfx_sprites_mix.bin',
        'm1_restoration_gfx_ending_us.bin',
        'm1_restoration_gfx_enemies_jp.bin',
        'm1_restoration_gfx_maptiles_jp.bin'],

    4: ['m1_restoration_gfx_sprites_us.bin',
        'm1_restoration_gfx_ending_us.bin',
        'm1_restoration_gfx_enemies_us.bin',
        'm1_restoration_gfx_maptiles_us.bin'],

    5: ['m1_restoration_gfx_sprites_jp.bin',
        'm1_restoration_gfx_ending_jp.bin',
        'm1_restoration_gfx_enemies_jp.bin',
        'm1_restoration_gfx_maptiles_jp.bin'],

    6: ['m1_main_text_us.txt',
        'm1_gfx_map_us.bin'],

    7: ['m1_main_text_jp.txt',
        'm1_gfx_map_jp.bin'],
    
    8: 'nes.ips',
    9: None,
    10: 'ncm.ips',
    11: 'vc.ips',
    12: 'skipm1.ips',
    13: None
}

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
