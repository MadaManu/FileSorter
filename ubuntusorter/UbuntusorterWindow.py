# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('ubuntusorter')

from ubuntusorter_lib import Window
from ubuntusorter.AboutUbuntusorterDialog import AboutUbuntusorterDialog
from ubuntusorter.PreferencesUbuntusorterDialog import PreferencesUbuntusorterDialog

# See ubuntusorter_lib.Window.py for more details about how this class works
class UbuntusorterWindow(Window):
    __gtype_name__ = "UbuntusorterWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UbuntusorterWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutUbuntusorterDialog
        self.PreferencesDialog = PreferencesUbuntusorterDialog

        self.preferenceButton = self.builder.get_object("preferencesbutton")
	
	def on_preferencesbutton_clicked(self, widget):
		# Run the preferences dialog.    
    	dia = PreferencesUbuntusorterDialog()
    	dia.show()


        # Code for other initialization actions should be added here.

