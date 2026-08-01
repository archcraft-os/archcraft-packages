#!/usr/bin/env python3

"""
Archcraft app launcher

A GTK4-based application for Archcraft OS.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

from gi.repository import GLib

from app.app import ArchcraftApplication
from app.data import APP_EXECUTABLE

GLib.set_prgname(APP_EXECUTABLE)

app = ArchcraftApplication()

app.run()
