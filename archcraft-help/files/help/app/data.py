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

APP_ID = "io.archcraft.Help"
APP_EXECUTABLE = "archcraft-help"
APP_NAME = "Archcraft Help"
APP_ICON = "archcraft-purple"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

BANNER_IMAGE = "banner.png"

MAIN_PAGE = PageData(

    title="Hello!",

    subtitle="Visit Archcraft Wiki for everything you need to know to operate Archcraft like a Hero.",

    image=BANNER_IMAGE,

    buttons=[

        ButtonData(
            id="open_wiki",
            text="Archcraft Wiki",
            style="flat-button",
            command="archcraft-help --wiki",
        ),

        ButtonData(
            id="open_tutorials",
            text="Archcraft Tutorials",
            style="flat-button",
            command="archcraft-help --blog",
        ),

        ButtonData(
            id="open_gallery",
            text="Archcraft Gallery",
            style="flat-button",
            command="archcraft-help --gallery",
        ),

    ],

)
