echo off
Rem To be run with the QGIS Application available from OSGeo here https://www.qgis.org/en/site/forusers/download.html
SET OSGEO4W_ROOT=C:\OSGeo4W64
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
SET QGIS_PREFIX_PATH=%QGIS%
SET VSCODE="C:\Users\Loyd IV\AppData\Local\Programs\Microsoft VS Code\code.exe"

CALL %OSGEO4W_ROOT%\bin\o4w_env.bat
CALL %OSGEO4W_ROOT%\bin\py3_env.bat
CALL %OSGEO4W_ROOT%\bin\qt5_env.bat
CALL %OSGEO4W_ROOT%\apps\grass\grass78\etc\env.bat

SET PATH=%PATH%;%QGIS%\bin
SET PATH=%PATH%;%OSGEO4W_ROOT%\apps\QT5\bin
SET PATH=%PATH%;%OSGEO4W_ROOT%\apps\Python37\Scripts
SET PATH=%PATH%;%OSGEO4W_ROOT%\apps\Python37\lib
SET PATH=%PATH%;C:\Program Files\GDAL
SET PATH=%PATH%;C:\Program Files\GDAL\gdalplugins
echo "PATH=%PATH%"
SET PYTHONPATH=%QGIS%\python;%PYTHONPATH%
SET PYTHONPATH=%PYTHONPATH%;C:\1-CodeRepos\0-IO-Tools\Play\VisualizeMaps\src;%OSGEO4W_ROOT%\apps\Python37\lib\site-packages
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
echo "PYTHONPATH=%PYTHONPATH%"
echo "PYTHONHOME=%PYTHONHOME%"
REM start "PyCharm aware of QGIS" /B %PYCHARM% %*
%VSCODE% "C:\1-CodeRepos\0-IO-Tools\Play\VisualizeMaps"