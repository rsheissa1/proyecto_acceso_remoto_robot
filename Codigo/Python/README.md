## Qt para Python

En este directorio se encuentra código generado por PySide6.

Se ha creado una intefase gráfica en Qt, por medio del siguiente comando en una terminal

_pyide6-designer_

El archivo resultante se nombró **MainWindow.ui**.

En una terminal se utilizó la aplicación

_pyside6-uic_

para convertir el diseño Qt (formato XML) a Python, el nuevo archivo se identifica como **MainWindow.py**.

Las operaciones que puede desarrollar la aplicación se encuentran en el archivo **garra_halcon_gui.py**.

Además de librerías Qt, se hace uso de la librearía Paho, la cual es una API para MOSQUITTO.
