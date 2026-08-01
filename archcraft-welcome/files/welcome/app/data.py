"""
Static application data.

This module defines the page content, including titles, images and
button definitions.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

from app.models import (
    ButtonData,
    PageData,
)

APP_ID = "io.archcraft.Welcome"
APP_EXECUTABLE = "archcraft-welcome"
APP_NAME = "Welcome"
APP_ICON = "archcraft-yellow"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

BANNER_IMAGE = "banner.svg"

MAIN_PAGE = PageData(

    title="Welcome to Archcraft",

    subtitle="A minimal, lightweight and fast linux distribution, based on Arch Linux.",

    image=BANNER_IMAGE,

    buttons=[

        ButtonData(
            id="get_started",
            text="Get Started",
            style="flat-button",
            command="archcraft-welcome --help",
        ),

        ButtonData(
            id="launch_calamares",
            text="Launch Calamares",
            style="flat-button",
            command="archcraft-welcome --calamares",
        ),

        ButtonData(
            id="launch_abif",
            text="Launch ABIF",
            style="flat-button",
            command="archcraft-welcome --abif",
        ),

    ],

)
