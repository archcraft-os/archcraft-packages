"""
Application data models.

Contains the dataclasses used throughout the application.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ButtonData:
    id: str
    text: str
    style: str
    command: str


@dataclass(frozen=True)
class PageData:
    title: str
    subtitle: str
    image: str
    buttons: list[ButtonData]
