# Códigos en phyton para suscribirse al brokery recibir las tramas que son enviadas a los brazos robot
# Ejecutar un script por cada robot cambiando el nombre de cada cliente de manera que no existan duplicados

- Curso **Iot** del **Samsung Innovation Campus**.

// Three Broketers Team

1. Dr. José Alfonso Domínguez Chávez
2. Dr. Agustín Gallardo del Ángel
3. Dr. Roberto Castañeda Sheissa

# Basado en el trabajo de © 2022 Digi International Inc.
# https://www.digi.com/resources/documentation/Digidocs/90001541/reference/r_example_subscribe_mqtt.htm

# RemoteArm_v_3_0 04/08/2022
# - Cambia la forma de empleo de las funciones de "paho" para un cierre correcto de las llamadas a procesos
# - Se logra hacer conecciòn entre clientes y subscriptores dentro de un red local mediante sus IP respectivas
# RemoteArm_v_2_1 21/07/2022
# - Se corrige error al enviar trama no se mandaba el retorno de carro
# RemoteArm_v_2_0 14/07/2022
# - Se agrega código para manejo de varias instrucciones y temporizado entre tramas
# RemoteArm_v_1_0 12/07/2022
# - Se reenvía el mensaje recibido por el subscriptor hacia el puerto serie.
# - Traducción de los comentarios de la fuente del código.

# 

