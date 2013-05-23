# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

# This is your preferences dialog.
#
# Define your preferences in
# data/glib-2.0/schemas/net.launchpad.ubuntusorter.gschema.xml
# See http://developer.gnome.org/gio/stable/GSettings.html for more info.

from gi.repository import Gio # pylint: disable=E0611

from locale import gettext as _

import logging
logger = logging.getLogger('ubuntusorter')

from ubuntusorter_lib.PreferencesDialog import PreferencesDialog

class PreferencesUbuntusorterDialog(PreferencesDialog):
    __gtype_name__ = "PreferencesUbuntusorterDialog"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the preferences dialog"""
        super(PreferencesUbuntusorterDialog, self).finish_initializing(builder)

        folders = self.builder.get_object("folder_list")
        folders.append(None,"Music")
        folders.append(None,"Videos")
        folders.append(None,"Pictures")

        thelist = self.builder.get_object("liststore1")
        thelist.insert(0,("hello0",))
        thelist.insert(1,("hello1",))
        thelist.insert(2,("hello2",))
        thelist.insert(3,("hello3",))
        thelist.insert(4,("hello4",))
        thelist.insert(5,("hello5",))
        thelist.insert(6,("hello6",))
        thelist.insert(7,("hello7",))
        thelist.insert(8,("hello8",))
        thelist.insert(9,("hello9",))
        thelist.insert(10,("hello10",))
        thelist.insert(11,("hello11",))
        thelist.insert(12,("hello12",))


        available = self.builder.get_object("liststore2")
        available.insert(0,(".avi",))
        available.insert(1,(".txt",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))
        available.insert(2,(".mp3",))

        # Bind each preference widget to gsettings
        # settings = Gio.Settings("net.launchpad.ubuntusorter")
        # widget = self.builder.get_object('example_entry')
        # settings.bind("example", widget, "text", Gio.SettingsBindFlags.DEFAULT)

        # Code for other initialization actions should be added here.
