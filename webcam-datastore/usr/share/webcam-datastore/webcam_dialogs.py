#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk
import os
import stat
import sys

USERNAME = ''
PASSWORD = ''

# ================


class UserDialog(gtk.Window):

    def close(self,widget,event,data = None):
        self.hide()
        gtk.main_quit()
        return gtk.FALSE

    def prep(self,widget,option):
        print widget, option
	global USERNAME
	global PASSWORD

        USERNAME = self.userentry.get_text()
        PASSWORD = self.passentry.get_text()
        self.hide()
        gtk.main_quit()
#        return gtk.FALSE
 
    def __init__(self):
        super(UserDialog, self).__init__()

        self.set_title("Acceso a WebCam Datastore")
        self.set_size_request(350, 160)
        self.set_position(gtk.WIN_POS_CENTER)
        
        win = gtk.Fixed()

        self.userlabel = gtk.Label("Usuario:")
        self.userentry = gtk.Entry()
        
        self.passlabel = gtk.Label("Password:")
        self.passentry = gtk.Entry()
        self.passentry.set_visibility(False)
        
        self.runbutton = gtk.Button("Conectar")
        self.exitbutton = gtk.Button("Salir")

        self.exitbutton.connect("clicked", self.close, "Exit")
        self.runbutton.connect("clicked", self.prep, "Run")

        #win.put(self.urllabel, 50, 30)
        #win.put(self.urlentry, 150, 25)
        
        win.put(self.userlabel, 50, 30)
        win.put(self.userentry, 150, 25)
        
        win.put(self.passlabel, 50, 70)
        win.put(self.passentry, 150, 65)
        
        win.put(self.runbutton, 250, 110)
        win.put(self.exitbutton, 50, 110)
                        
        self.add(win)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()


def get_credentials():
	UserDialog()
	gtk.main()
	return (USERNAME, PASSWORD)

def error_dialog(txt):
	md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, txt)
	md.run()
	md.destroy()

def info_dialog(txt):
	md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, txt)
	md.run()
	md.destroy()
# ===============
