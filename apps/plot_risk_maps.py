from qgis.core import *
from mapViewerWindow import mapViewerWindow
import os
from mapViewerWindow import mapTypes
# from qgis.PyQt.QtWidgets import *
# from qgis.PyQt.QtCore import *
# from qgis._gui import *


QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
qgs = QgsApplication([], True)
qgs.initQgis()
mp = mapViewerWindow()
mp.loadDefaultLyrs()
print(os.getcwd())

mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_landcover_n33900w119100_viz.tif",
    Tag="landcover risk",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_population_n33900w119100_viz.tif",
    Tag="population risk",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_slope_n33900w119100_viz.tif",
    Tag="slope risk",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_n33900w119100_viz.tif",
    Tag="total risk",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_slope_n33900w119100_viz.tif",
    Tag="total risk",
    mapType=mapTypes.Slope)
# mp.addRasterLayer(
#     fn=r"maps/rasterMaps/utm_population_5_n34000w119000_viz.tif",
#     Tag="utm population 2021",
#     mapType=mapTypes.utm_5_population)
mp.show()
qgs.exec_()