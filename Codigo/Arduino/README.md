# Códigos para tarjetas arduino, se debe usar una tarjeta arduino por cada brazo robot
# Está optimizado para 6 servomotores por tarjeta
# La carpeta scripts_python contienen los códigos que se suscriben al broker para recibir las tramas de datos
# mismas que son interpretadas y enviadas a el arduino para general los movimientos correspondientes

- Curso **Iot** del **Samsung Innovation Campus**.

// Three Broketers Team

1. Dr. José Alfonso Domínguez Chávez
2. Dr. Agustín Gallardo del Ángel
3. Dr. Roberto Castañeda Sheissa

// CONTROL DE 6 SERVOMOTORES POR CADENA DE TEXTO RECIBIDA POR UART CONTROL DE INERCIA MEDIANTE VELOCIDAD DE MOVIMIENTO
//                                                                          [  ][  ][  ][  ][  ][  ]
// Enviar una cadena que contenga los milisegundos del PWM de cada motor -> 120020001300111003001800
// Corresponde a 1200 ms, 2000 ms, 1300 ms, 1110 ms y 300 ms para cada servo (1 al 6 respectivamente) 
// José Alfonso Domínguez Chávez
// Versión 2.2.1 2022-08-02
// Se agrega un canal pwm para un sexto motor
// Se corrige error en código para posiciones iniciales
// Versión 2.0.0 2022-07-28
// Se agrega el control de velocidad mediante constante para disminuir la inercia de los movimientos
// Versión 1.0.0 2022-07-14
// Versión inicial del código


