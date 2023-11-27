import dearpygui.dearpygui as dpg

import setting
from gui.utils.add_ru_fonts import add_ru_founts
from gui.main_menu import show_main_menu


def _init_gui():
    dpg.create_context()
    dpg.create_viewport(
        title="dm_tool",
        width=setting.MAIN_WINDOW_WIDTH,
        height=setting.MAIN_WINDOW_HEIGHT,
        resizable=setting.RESIZABLE,
    )
    dpg.setup_dearpygui()
    add_ru_founts()


def _show_viewport():
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def star_giu():
    _init_gui()

    # all component
    show_main_menu()

    _show_viewport()
