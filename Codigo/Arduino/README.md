## Códigos para tarjetas Arduino

Para controlar el movimiento de un brazo robot, se requiere una tarjeta Arduino.

Está optimizado para 6 servomotores por tarjeta.

Three Broketers Team

Dr. José Alfonso Domínguez Chávez

Dr. Agustín Gallardo del Ángel

Dr. Roberto Castañeda Sheissa

### Control de motores por cadena de texto

Es posible controlar 6 servomotores por medio de una cadena de texto recibida por UART control de inercia mediante velocidad de movimiento.

La estructura de la cadena de texto sería como sigue -> 120020001300111003001800

Esta cadena se interpreta como la cantidad, en milisegundos, del PWM para cada motor, es decir -> |1200|2000|1300|1110|0300|1800|

Los símbolos || indican el inicio y fin de los dígitos de control correspondientes a cada motor. 

Por lo tanto, el ejemplo anterior corresponde a 1200 ms, 2000 ms, 1300 ms, 1110 ms y 300 ms para cada servo (1 al 6 respectivamente).

Desarrollado y probado por José Alfonso Domínguez Chávez -> Inventor, patentor y controlador (de motores)

**Versión 2.2.1 2022-08-02**

- Se agrega un canal PWM para un sexto motor.

- Se corrige error en código para posiciones iniciales.

**Versión 2.0.0 2022-07-28**

- Se agrega el control de velocidad mediante constante para disminuir la inercia de los movimientos

**Versión 1.0.0 2022-07-14**

- Versión inicial del código


