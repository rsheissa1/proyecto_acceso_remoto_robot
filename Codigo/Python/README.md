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

## Comunicación MQTT con Arduino

El directorio **Interprete_mensajes_control** contiene código Phyton que permite suscribirse a un broker y recibir 
tramas enviadas a los brazos robot.

Se ejecuta un script por cada robot, cambiando el nombre de cada cliente con el fin de evitar duplicados.

Código traído a ustedes por Three Broketers Team

Dr. José Alfonso Domínguez Chávez
Dr. Agustín Gallardo del Ángel
Dr. Roberto Castañeda Sheissa

[Basado](https://www.digi.com/resources/documentation/Digidocs/90001541/reference/r_example_subscribe_mqtt.htm) en el trabajo de © 2022 Digi International Inc.

RemoteArm_v_3_0 04/08/2022
- Cambia la forma de empleo de las funciones de "paho" para un cierre correcto de las llamadas a procesos
- Se logra hacer conecciòn entre clientes y subscriptores dentro de un red local mediante sus IP respectivas

RemoteArm_v_2_1 21/07/2022
- Se corrige error al enviar trama no se mandaba el retorno de carro

RemoteArm_v_2_0 14/07/2022
- Se agrega código para manejo de varias instrucciones y temporizado entre tramas

RemoteArm_v_1_0 12/07/2022
- Se reenvía el mensaje recibido por el subscriptor hacia el puerto serie.
- Traducción de los comentarios de la fuente del código.
