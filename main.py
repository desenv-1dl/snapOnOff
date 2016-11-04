# result3 = QgsVectorLayer("LineString", "ligne", "memory") 
# #it's to create your layer
# 
# ligneid=result3.id()
# # it allows you to have the idvalue for your layer
# 
# QgsProject.instance().setSnapSettingsForLayer(ligneid,True,2,1,1000,True)
# # it defines the snapping options ligneid : the id of your layer, True : to enable the layer snapping, 2 : options (0: on vertex,
# # 1 on segment, 2: vertex+segment), 1: pixel (0: type of unit on map), 1000 : tolerance, true : avoidIntersection)

from qgis.core import QgsMapLayerRegistry, QgsMapLayer, QgsField, QGis
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import QVariant, QSize
from snapButton import SnapButton

class Main:
    def __init__(self, iface):
        self.iface = iface        
        self.snapB = SnapButton(self.iface)
    
    def initGui(self):
        self.iface.addToolBarWidget(self.snapB.upleft)
        
        
    def unload(self):    
        pass
    
   
    