# -*- coding: utf-8 -*-
import qgis
from qgis.gui import *
from qgis.core import *
from PyQt4.Qt import *
import sys, os
from PyQt4 import QtGui, uic, QtCore
import resources
from PyQt4.QtCore import pyqtSlot, QSettings, QObject
from PyQt4.QtGui import QMessageBox



sys.path.append(os.path.dirname(__file__))
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'snapButton.ui'), resource_suffix='')

class SnapButton(QtGui.QWidget, FORM_CLASS):
    def __init__(self, iface, parent=None):
        super(SnapButton, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)
        
    @pyqtSlot(bool)    
    def on_upleft_toggled(self, a):
        if self.iface.activeLayer():
            if a:
                self.setSnap(10)
                    
            else:
                self.setSnap(0)
        else:
            self.iface.messageBar().pushMessage(u"Atenção", u"Ative uma camada!",
                                                level=QgsMessageBar.INFO, duration=10)

    def setSnap(self, n):
        proj = QgsProject.instance()
        proj.writeEntry('Digitizing', 'SnappingMode', 'all_layers')
        proj.writeEntry('Digitizing','DefaultSnapType', 'to vertex and segment') 
        proj.writeEntry('Digitizing','DefaultSnapTolerance', n)
        layer = qgis.utils.iface.activeLayer()
        proj.setSnapSettingsForLayer(layer.id(), True, 0, 0, 0, True)
        #it defines the snapping options ligneid : the id of your layer, True : to enable the layer snapping, 2 : options (0: on vertex,
        # 1 on segment, 2: vertex+segment), 1: pixel (0: type of unit on map), 1000 : tolerance, true : avoidIntersection)        
        
            
    