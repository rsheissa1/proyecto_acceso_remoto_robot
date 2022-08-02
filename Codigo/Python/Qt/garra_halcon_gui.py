import sys
import paho.mqtt.client as mqtt

from PySide6 import QtWidgets,QtCore

from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Configuración de MQTT
        # Prueba con broker local (localhost)
        # Prueba con broker externo ("broker.hivemq.com)
        self.client = mqtt.Client("qtclient1")
        #self.client.connect("localhost")
        self.client.connect("broker.hivemq.com")

        self.enviarButton.clicked.connect(self.buttonSend)
        self.borrarButton.clicked.connect(self.buttonClear)
        self.cerrarButton.clicked.connect(self.buttonExit)

    def buttonSend(self):
        # Se calculan los milisegundos para posicionar motor 1 en
        # el ángulo seleccionado por el usuario
        temp1 = self.mot1Spin.value()
        mot1 = format(temp1 * 7, "04d")
        moto1 = str(mot1)+"00000000000000000000"
        delay1 = self.delay1Spin.value()

        # Se calculan los milisegundos para posicionar motor 2 en
        # el ángulo seleccionado por el usuario
        temp2 = self.mot2Spin.value()
        mot2 = format(temp2 * 7, "04d")
        moto2 = str(mot1) + str(mot2) + "0000000000000000"
        delay2 = self.delay2Spin.value()

        # Se calculan los milisegundos para posicionar motor 3 en
        # el ángulo seleccionado por el usuario
        temp3 = self.mot3Spin.value()
        mot3 = format(temp3 * 7, "04d")
        moto3 = str(mot1) + str(mot2) + str(mot3) + "000000000000"
        delay3 = self.delay3Spin.value()

        # Se calculan los milisegundos para posicionar motor 4 en
        # el ángulo seleccionado por el usuario
        temp4 = self.mot4Spin.value()
        mot4 = format(temp4 * 7, "04d")
        moto4 = str(mot1) + str(mot2) + str(mot3) + str(mot4) + "00000000"
        delay4 = self.delay4Spin.value()

        # Se calculan los milisegundos para posicionar motor 5 en
        # el ángulo seleccionado por el usuario
        temp5 = self.mot5Spin.value()
        mot5 = format(temp5 * 7, "04d")
        moto5 = str(mot1) + str(mot2) + str(mot3) + str(mot4) + str(mot5) + "0000"
        delay5 = self.delay5Spin.value()

        # Se calculan los milisegundos para posicionar motor 6 en
        # el ángulo seleccionado por el usuario
        temp6 = self.mot6Spin.value()
        mot6 = format(temp6 * 7, "04d")
        moto6 = str(mot1) + str(mot2) + str(mot3) + str(mot4) + str(mot5) + str(mot6)
        delay6 = self.delay6Spin.value()

        position = moto1 + "," + str(delay1) + ","\
                 + moto2 + "," + str(delay2) + ","\
                 + moto3 + "," + str(delay3) + ","\
                 + moto4 + "," + str(delay4) + ","\
                 + moto5 + "," + str(delay5) + ","\
                 + moto6 + "," + str(delay6)

        self.client.publish("/uv/lab1/test1", position)

    def buttonClear(self):
        self.mot1Spin.setValue(0)
        self.mot2Spin.setValue(0)
        self.mot3Spin.setValue(0)
        self.mot4Spin.setValue(0)
        self.mot5Spin.setValue(0)
        self.mot6Spin.setValue(0)
        self.delay1Spin.setValue(1)
        self.delay2Spin.setValue(1)
        self.delay3Spin.setValue(1)
        self.delay4Spin.setValue(1)
        self.delay5Spin.setValue(1)
        self.delay6Spin.setValue(1)

    def buttonExit(self):
        # Código para cerrar ventana y terminar aplicación
       QtWidgets.QApplication.instance().quit() 

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
