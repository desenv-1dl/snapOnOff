# -*- coding: utf-8 -*-

from main import Main

def name():
    return "Snap atalho"
def description():
    return "Atalho para ativar e desativar o snap rapidamente"
def version():
    return "Version 0.1"
def classFactory(iface):
    return Main(iface)
def qgisMinimumVersion():
    return "2.0"
def author():
    return "jossan costa"
def email():
    return "me@hotmail.com"
def icon():
    return "icon.png"
