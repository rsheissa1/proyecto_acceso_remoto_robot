// CONTROL DE 5 SERVOMOTORES POR CADENA DE TEXTO RECIBIDA POR UART
// Basado en código de: zoomkat 11-22-10 serial servo (2) test 
// Modificado por José Alfonso Domínguez Chávez - AlphX - 2022-07-05

// Enviar una cadena que contenga los milisegundos del PWM de cada motor -> 12002000130011100300
// Corresponde a 1200 ms, 2000 ms, 1300 ms, 1110 ms y 300 ms para cada servo (1 al 5 respectivamente) 

 #include <Servo.h> 
 
 String readString, Strservo1, Strservo2, Strservo3, Strservo4, Strservo5; 
 // Crea los objetos para control de los servos
 Servo servo1;  
 Servo servo2; 
 Servo servo3; 
 Servo servo4; 
 Servo servo5; 

 void setup() { 
 Serial.begin(9600); 
 //Configuración de los pines para los servos
 servo1.attach(2);  
 servo2.attach(3);
 servo3.attach(4); 
 servo4.attach(5);
 servo5.attach(6); 
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
 Serial.println(readString);  //Imprime en terminal la cadena recibida

 // expect a string like 07002100 containing the two servo positions 
 Strservo1 = readString.substring(0, 4);  //Obtiene los primeros cuatro caractéres
 Strservo2 = readString.substring(4, 8);  //Obtiene los siguientes cuatro
 Strservo3 = readString.substring(8, 12);  //Obtiene los siguientes cuatro 
 Strservo4 = readString.substring(12, 16);  //Obtiene los siguientes cuatro 
 Strservo5 = readString.substring(16, 20);  //Obtiene los últimos cuatro 

//Imprime los resultados en la terminal
 Serial.println(Strservo1);  
 Serial.println(Strservo2); 
 Serial.println(Strservo3); 
 Serial.println(Strservo4); 
 Serial.println(Strservo5);

 int ms1, ms2, ms3, ms4, ms5 ;  //variables para los milisegundos 

 char carray1[6];  //magic needed to convert string to a number 
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

 // Mueve los servos
 servo1.writeMicroseconds(ms1); 
 servo2.writeMicroseconds(ms2); 
 servo3.writeMicroseconds(ms3); 
 servo4.writeMicroseconds(ms4); 
 servo5.writeMicroseconds(ms5);
 readString=""; 
 } 
 }
