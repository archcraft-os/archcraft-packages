"""
Resource helpers.

Provides helper functions for locating images, stylesheets and other
application resources.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

import os
from pathlib import Path

from gi.repository import Gdk, Gtk

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"
IMAGES = ASSETS / "images"

CSS = ASSETS / "css"
_STYLE_CSS = CSS / "style.css"
_FALLBACK_CSS = CSS / "fallback.css"

_THEME_DIRS = (
    Path.home() / ".themes",
    Path.home() / ".local/share/themes",
    Path("/usr/share/themes"),
)

def image_path(filename: str) -> Path:
    return IMAGES / filename

def current_theme() -> str:
    """Return the current GTK theme name."""

    theme = os.environ.get("GTK_THEME")

    if theme:
        return theme.split(":", 1)[0]

    settings = Gtk.Settings.get_default()

    if settings is None:
        return ""

    return settings.get_property("gtk-theme-name")

def theme_has_gtk4(theme: str) -> bool:
    """Return True if the selected theme provides GTK4 assets."""

    if not theme:
        return False

    for directory in _THEME_DIRS:
        if (directory / theme / "gtk-4.0").is_dir():
            return True

    return False

def using_gtk4_theme() -> bool:
    """Return True if the current theme supports GTK4."""

    return theme_has_gtk4(current_theme())

def load_css(display: Gdk.Display) -> None:
    """Load application stylesheets."""

    style = Gtk.CssProvider()
    style.load_from_path(str(_STYLE_CSS))

    Gtk.StyleContext.add_provider_for_display(
        display,
        style,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
    )
    
    if using_gtk4_theme():
        return
    
    fallback = Gtk.CssProvider()
    fallback.load_from_path(str(_FALLBACK_CSS))
    
    Gtk.StyleContext.add_provider_for_display(
        display,
        fallback,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
    )
