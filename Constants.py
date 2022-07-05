#!/usr/bin/python3
PATCH_VERSION = '1.1.1'
FINAL_ROM_NAME = f'Mother 1+2 [T+Ita{PATCH_VERSION}].gba'

STATUS_START = "Benvenutə al patcher per Mother 1+2."
STATUS_PRESET = "Preset applicato."
STATUS_MD5 = "MD5 verificato."

VAR_WINDOW_TITLE = "Mother 1+2 Patcher by Earthbound Café"
VAR_FILEPICKER = "ROM giapponese di Mother 1+2"

WARNING_TITLE = "Attenzione"
WARNING_EXTRACT = "È necessario estrarre l'archivio."
WARNING_MD5_MISMATCH = "La ROM selezionata non è compatibile con la nostra patch."


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
    100: {'option': '\nFONT'},
    1: {
        'option': 'Originale (serif)',
        'files': ['m1_gfx_font_og.bin']
        },
    2: {
        'option': 'Tomato (sans)',
        'files': ['m1_gfx_font_new.bin']
        },
    101: {'option': '\nSPRITE E TILE'},
    3: {
        'option': 'Mix',
        'files': [
            'm1_restoration_gfx_sprites_mix.bin',
            'm1_restoration_gfx_ending_us.bin',
            'm1_restoration_gfx_enemies_jp.bin',
            'm1_restoration_gfx_maptiles_jp.bin'
            ]
        },
    4: {
        'option': 'US',
        'files': [
            'm1_restoration_gfx_sprites_us.bin',
            'm1_restoration_gfx_ending_us.bin',
            'm1_restoration_gfx_enemies_us.bin',
            'm1_restoration_gfx_maptiles_us.bin'
            ]
        },
    5: {
        'option': 'JP',
        'files': [
            'm1_restoration_gfx_sprites_jp.bin',
            'm1_restoration_gfx_ending_jp.bin',
            'm1_restoration_gfx_enemies_jp.bin',
            'm1_restoration_gfx_maptiles_jp.bin'
            ]
        },
    102: {'option': '\nLUOGHI'},
    6: {
        'option': 'US',
        'files': [
            'm1_main_text_us.txt',
            'm1_gfx_map_us.bin'
            ]
        },
    7: {
        'option': 'JP',
        'files': [
            'm1_main_text_jp.txt',
            'm1_gfx_map_jp.bin'
            ]
        },
    103: {'option': '\nPALETTE'},
    8: {
        'option': 'NES',
        'files': 'nes.ips'
        },
    9: {
        'option': 'GBA',
        'files': None
        },
    10: {
        'option': 'Nintendo Classic Mini - NES',
        'files': 'ncm.ips'
        },
    11: {
        'option': 'Virtual Console Wii e Wii U',
        'files': 'vc.ips'
        },
    104: {'option': '\nSKIP A MOTHER 1?'},
    12: {
        'option': 'Sì',
        'files': 'skipm1.ips'
        },
    13: {
        'option': 'No',
        'files': None
        }
}