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

        # map will be replaced by saved settings
        self.default_map = { 'Music':[".mp3","wav"], 
                        'Pictures':[".jpg",".png",".bmp",".gif"] }

        # default folders - replaced by saved settings
        self.default_folders = ["Music", "Pictures", "Videos"]


        # list of all available extensions - this will be big
        # and probably fetched from somewhere
        self.all_extensions = [".mp3",".wav",".jpg",".png",".gif",".bmp",".odt",".sql"]

        # add elements to the dropdown list
        self.folders = self.builder.get_object("folder_list")
        for folder in self.default_folders:
            self.folders.append(None,folder)

        # add default nothing to the extensions
        # maybe disable the tree 
        self.thelist = self.builder.get_object("extensions")
        self.add_folder_dialog = self.builder.get_object("folder_add_name_dialog")
        self.thelist.insert(0,("No Folder",))
        self.thelist.insert(1,("selected",))


        self.available_extensions = self.builder.get_object("available_extensions")
        for extension in self.all_extensions:
            self.available_extensions.append((extension,))

        # Bind each preference widget to gsettings
        # settings = Gio.Settings("net.launchpad.ubuntusorter")
        # widget = self.builder.get_object('example_entry')
        # settings.bind("example", widget, "text", Gio.SettingsBindFlags.DEFAULT)

        # Code for other initialization actions should be added here.
    
    def on_folder_remove_clicked(self, widget):
        index = self.folders.get_active()
        if index>=0:
            self.default_map.pop(self.default_folders[index],None)  # remove from map
            self.folders.remove(index)                              # remove from the dropdown display
            self.default_folders.pop(index)                         # remove from the list of folders
            print "Folder ",index," Removed" 
        else:
            print "Nothing Selected to remove - display some sort of warning box"

    def on_folder_add_clicked(self, widget):
        # missing text input for the name of the folder - needs redesign or maybe
        #                                      use some dialog box to input name
        self.add_folder_dialog.show()
        print "folder added"

    def on_save_button_clicked(self, widget):
        input_text = self.builder.get_object("folder_name_entry").get_text()
        # check the validity of inputed text
        # display error if any
        # else are you sure question
        # if yes save the new folder
        # else revert to input again

    def on_close_button_clicked(self, widget):
        print "canceled!"
        # clear buffer by adding a default text in
        self.builder.get_object("newFolderBuffer").set_text("Folder Name",11)
        self.add_folder_dialog.hide()


    # handler for changing the folder dropdown menu
    def selected_folder(self, folder_extensions_store):

        folder_extensions_store.clear() # empty the store
        text = self.folders.get_active_text()
        if text is not None:
            extensions = self.default_map[self.folders.get_active_text()] # get the list of the extensions
                                                                      # in the selected folder
            for extension in extensions: 
                self.thelist.append((extension,))   # add each extension to the store
