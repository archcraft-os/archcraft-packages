"""
Page layout.

Builds the GTK interface displayed when the application starts.

Copyright (C) 2026 Archcraft
Copyright (C) 2026 Aditya Shakya <adi1090x@gmail.com>

SPDX-License-Identifier: GPL-3.0-or-later
"""

import gi

gi.require_version("Gtk", "4.0")

from collections.abc import Callable

from gi.repository import Gtk

from app.models import (
    ButtonData,
    PageData,
)
from app.resources import image_path


class Page(Gtk.Box):

    def __init__(
        self,
        data: PageData,
        on_button_clicked: Callable,
    ):

        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )
        
        self.set_margin_top(56)
        self.set_margin_bottom(56)
        self.set_margin_start(32)
        self.set_margin_end(32)
        
        self.on_button_clicked = on_button_clicked

        self.set_hexpand(True)
        self.set_vexpand(True)

        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)
        self.set_homogeneous(False)

        self.create_widgets()
        self.load_page(data)
        
    def create_widgets(self):

        self.content_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )
        
        self.content_box.set_halign(Gtk.Align.CENTER)
        self.content_box.set_size_request(760, -1)
        self.content_box.set_valign(Gtk.Align.CENTER)
        self.content_box.set_hexpand(True)
        
        self.append(self.content_box)

        #
        # Title
        #
        self.title = Gtk.Label()
        self.title.add_css_class("page-title")
        self.title.set_wrap(True)
        self.title.set_justify(Gtk.Justification.CENTER)

        #
        # Subtitle
        #
        self.subtitle = Gtk.Label()
        self.subtitle.add_css_class("page-subtitle")
        self.subtitle.set_wrap(True)
        self.subtitle.set_justify(Gtk.Justification.CENTER)
        self.subtitle.set_max_width_chars(70)

        #
        # Picture
        #
        self.image = Gtk.Picture(content_fit=Gtk.ContentFit.CONTAIN)
        
        self.image.set_size_request(500, 250)
        
        self.image.set_hexpand(True)
        self.image.set_halign(Gtk.Align.CENTER)
        self.image.set_valign(Gtk.Align.CENTER)
        self.image.add_css_class("page-image")

        #
        # Buttons
        #        
        self.button_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=18
        )
        
        self.button_box.set_halign(Gtk.Align.CENTER)
        self.button_box.set_margin_top(36)
        
        self.buttons = {}
        
        self.content_box.append(self.title)
        self.content_box.append(self.subtitle)
        self.content_box.append(self.image)
        self.content_box.append(self.button_box)
        
    def load_page(self, data: PageData) -> None:
        self.data = data

        self.title.set_label(
            data.title
        )
        
        self.subtitle.set_label(
            data.subtitle
        )
        
        self.image.set_filename(
            str(image_path(data.image))
        )

        while child := self.button_box.get_first_child():
            self.button_box.remove(child)
        
        self.buttons.clear()

        for button_data in data.buttons:
        
            button = Gtk.Button(
                label=button_data.text
            )
        
            button.add_css_class(
                button_data.style
            )

            button.connect(
                "clicked",
                self.button_clicked,
                button_data,
            )
        
            self.buttons[button_data.id] = button
        
            self.button_box.append(button)
            button.set_hexpand(True)
            self.button_box.set_homogeneous(True)

    def button_clicked(
        self,
        button: Gtk.Button,
        button_data: ButtonData,
    ) -> None:
        self.on_button_clicked(button_data)
