"""
Application entry point.

Creates the main application window,
loads the main page and dispatches
button actions.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

import shlex
import subprocess

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from app.data import (
    APP_ID,
    APP_NAME,
    MAIN_PAGE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from app.layouts.page import Page
from app.resources import load_css


class ArchcraftApplication(Gtk.Application):

    def __init__(self):

        super().__init__(
            application_id=APP_ID
        )

    def launch_command(self, button_data):
        try:
            subprocess.Popen(
                shlex.split(button_data.command),
                start_new_session=True,
            )
        except FileNotFoundError:
            print(f"Command not found: {button_data.command}")
        except OSError as err:
            print(f"Failed to execute '{button_data.command}': {err}")


    def do_activate(self):
    
        window = Gtk.ApplicationWindow(application=self)
        
        window.set_title(APP_NAME)
        window.set_default_size(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )
        
        load_css(window.get_display())

        self.page = Page(
            MAIN_PAGE,
            self.launch_command,
        )
        
        window.set_child(self.page)
                
        window.present()
