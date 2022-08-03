// Three Broketers Team
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

 #include <Servo.h> 
 String readString, Strservo1, Strservo2, Strservo3, Strservo4, Strservo5, Strservo6; 
 int k_inercial = 1;
 int step_servo1, step_servo2, step_servo3, step_servo4, step_servo5, step_servo6, movimientos;
 // Posiciones iniciales para los servos
 int ms1=1200;
 int ms2=1200;
 int ms3=1200;
 int ms4=1200;
 int ms5=1200;
 int ms6=1200;

 // Crea los objetos para control de los servos
 Servo servo1;  
 Servo servo2; 
 Servo servo3; 
 Servo servo4; 
 Servo servo5; 
 Servo servo6; 

 void setup() { 
 Serial.begin(9600); 
 //Configuración de los pines para los servos
 servo1.attach(2);  
 servo2.attach(3);
 servo3.attach(4); 
 servo4.attach(5);
 servo5.attach(6); 
 servo6.attach(7); 

// Mueve a inicio los servomotores

 servo1.writeMicroseconds(ms1);
 servo2.writeMicroseconds(ms2);
 servo3.writeMicroseconds(ms3);
 servo4.writeMicroseconds(ms4); 
 servo5.writeMicroseconds(ms5);
 servo6.writeMicroseconds(ms6);

 step_servo1 = ms1; 
 step_servo2 = ms2; 
 step_servo3 = ms3; 
 step_servo4 = ms4; 
 step_servo5 = ms5; 
 step_servo6 = ms6; 

 } 

 void loop() { 

 while (Serial.available()) { 
 delay(10); 
 if (Serial.available() >0) { //Si el puerto serie está abierto ...
 char c = Serial.read();  //Obtiene un caractér del buffer
 readString += c;  //Concatena la cadena hasta que encuentra retorno de carro
 } 
 } 

 if (readString.length() >0) { //Si la variable contiene datos ...
 Serial.print ("Recibido ... ");
 Serial.print (readString);  //Imprime en terminal la cadena recibida

 Strservo1 = readString.substring(0, 4);  //Obtiene los primeros cuatro caractéres
 Strservo2 = readString.substring(4, 8);  //Obtiene los siguientes cuatro
 Strservo3 = readString.substring(8, 12);  //Obtiene los siguientes cuatro 
 Strservo4 = readString.substring(12, 16);  //Obtiene los siguientes cuatro 
 Strservo5 = readString.substring(16, 20);  //Obtiene los penúltimos cuatro 
 Strservo6 = readString.substring(20, 24);  //Obtiene los últimos cuatro 

 char carray1[6];  //Conversión de cadena a número
 Strservo1.toCharArray(carray1, sizeof(carray1)); 
 ms1 = atoi(carray1); 

 char carray2[6]; 
 Strservo2.toCharArray(carray2, sizeof(carray2)); 
 ms2 = atoi(carray2); 

 char carray3[6]; 
 Strservo3.toCharArray(carray3, sizeof(carray3)); 
 ms3 = atoi(carray3); 

 char carray4[6]; 
 Strservo4.toCharArray(carray4, sizeof(carray4)); 
 ms4 = atoi(carray4); 

 char carray5[6]; 
 Strservo5.toCharArray(carray5, sizeof(carray5)); 
 ms5 = atoi(carray5); 

 char carray6[6]; 
 Strservo6.toCharArray(carray6, sizeof(carray6)); 
 ms6 = atoi(carray6); 

movimientos = (step_servo1-ms1)+(step_servo2-ms2)+(step_servo3-ms3)+(step_servo4-ms4)+(step_servo5-ms5)+(step_servo6-ms6);
 while (movimientos != 0){
 movimientos = (step_servo1-ms1)+(step_servo2-ms2)+(step_servo3-ms3)+(step_servo4-ms4)+(step_servo5-ms5)+(step_servo6-ms6);

    if (step_servo1 - ms1 > 0) {step_servo1--;}
    if (step_servo1 - ms1 < 0) {step_servo1++;}

    if (step_servo2 - ms2 > 0) {step_servo2--;}
    if (step_servo2 - ms2 < 0) {step_servo2++;}

    if (step_servo3 - ms3 > 0) {step_servo3--;}
    if (step_servo3 - ms3 < 0) {step_servo3++;}

    if (step_servo4 - ms4 > 0) {step_servo4--;}
    if (step_servo4 - ms4 < 0) {step_servo4++;}

    if (step_servo5 - ms5 > 0) {step_servo5--;}
    if (step_servo5 - ms5 < 0) {step_servo5++;}

    if (step_servo6 - ms6 > 0) {step_servo6--;}
    if (step_servo6 - ms6 < 0) {step_servo6++;}

   // Mueve los servos
   
   servo1.writeMicroseconds(step_servo1); 
   servo2.writeMicroseconds(step_servo2); 
   servo3.writeMicroseconds(step_servo3); 
   servo4.writeMicroseconds(step_servo4); 
   servo5.writeMicroseconds(step_servo5);
   servo6.writeMicroseconds(step_servo6);
   delay (k_inercial);
 } //fin de while
  Serial.print (" - finalizado el movimiento");
  Serial.print ('\n');
  step_servo1 = ms1; 
  step_servo2 = ms2; 
  step_servo3 = ms3; 
  step_servo4 = ms4; 
  step_servo5 = ms5; 
  step_servo6 = ms6; 
   
 readString=""; 
 } 
 }
