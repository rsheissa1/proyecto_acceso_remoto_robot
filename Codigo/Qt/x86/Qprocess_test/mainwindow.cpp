#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtNetwork/QHostAddress>
#include <QtNetwork/QNetworkInterface>
#include <QDebug>
#include <QStringList>
#include <QByteArray>
#include <QDateTime>
#include <QtMqtt/QMqttClient>
#include <QMessageBox>

/* Este programa localiza la IP del servidor de streaming
 * y lo envía al cliente junto con los canales del streaming.
 * Habilita 2 webcams y envía el streaming por RTSP usando
 * la plataforma VLC.
 * Ejecuta el script de Python para recibir las posiciones
 * en ms de los motors de dos brazos robots.
 */

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QString ip;
    QString programa;
    programa.append("cvlc");

    const QHostAddress &localhost = QHostAddress(QHostAddress::LocalHost);
    for (const QHostAddress &address: QNetworkInterface::allAddresses()) {
        if (address.protocol() == QAbstractSocket::IPv4Protocol && address != localhost){
            qDebug() << address.toString();
            ip.append(address.toString());
            ui->linea_IP->setText("IP: "+address.toString());
        }
    }

    cvlc_cam1 = new QProcess(this);
    cvlc_cam2 = new QProcess(this);

    QStringList cam1;
    cam1<<"-vvv"<<"v4l2:///dev/video0"<<"--sout=#transcode{vcodec=h264,vb=1500,width=1280,height=720,acodec=mp3,ab=192,channels=2,samplerate=44100,scodec=none}:rtp{sdp=rtsp://:8554/live}"<<":no-sout-all"<<":sout-keep";

    QStringList cam2;
    cam2<<"-vvv"<<"v4l2:///dev/video2"<<"--sout=#transcode{vcodec=h264,vb=1500,width=1280,height=720,acodec=mp3,ab=192,channels=2,samplerate=44100,scodec=none}:rtp{sdp=rtsp://:8555/live}"<<":no-sout-all"<<":sout-keep";

    connect(cvlc_cam1,SIGNAL(readyReadStandardOutput()),this,SLOT(datosRecibido1()));
    connect(cvlc_cam1,SIGNAL(readyReadStandardError()),this,SLOT(Error_proc1()));
    connect(cvlc_cam1,SIGNAL(started()),this,SLOT(iniciado1()));

    cvlc_cam1->start(programa,cam1);

    connect(cvlc_cam2,SIGNAL(readyReadStandardOutput()),this,SLOT(datosRecibido2()));
    connect(cvlc_cam2,SIGNAL(readyReadStandardError()),this,SLOT(Error_proc2()));
    connect(cvlc_cam2,SIGNAL(started()),this,SLOT(iniciado2()));

    cvlc_cam2->start(programa,cam2);

    /*QString program = "cvlc";
    QStringList arguments;
    arguments << "rtsp://192.168.5.158:1234/live";

    //QProcess *myProcess = new QProcess(parent);
    cvlc1->start(program, arguments);*/

    cliente = new QMqttClient(this);
    cliente->setHostname("148.226.18.64");//localhost");
    cliente->setPort(1883);

    connect(cliente,&QMqttClient::stateChanged,this,&MainWindow::estadoCambiado);
    connect(cliente,&QMqttClient::connected,this,&MainWindow::brokerConectado);
    //estadoCambiado();
    cliente->connectToHost();

    QString programaPy;
    QStringList argsPy;
    programaPy.append("python3");
    argsPy<<"RemoteArm_v_2_1.py";
    motoresPy = new QProcess(this);
    connect(motoresPy,SIGNAL(readyReadStandardOutput()),this,SLOT(datosRecibido3()));
    connect(motoresPy,SIGNAL(readyReadStandardError()),this,SLOT(Error_proc3()));
    connect(motoresPy,SIGNAL(started()),this,SLOT(iniciado3()));
    motoresPy->start(programaPy,argsPy);
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString MainWindow::texto(int a)
{
    switch (a) {
    case 0:
       return "Desconectado";
        break;
    case 1:
       return "Conectando...";
        break;
    case 2:
       return "Conectado";
        break;
    default:
        break;
    }
}

void MainWindow::datosRecibido1()
{
    //ui->C1_init->append(cvlc_cam1->readAllStandardOutput());
}

void MainWindow::iniciado1()
{
    qDebug()<<"programa1: "<<cvlc_cam1->program()<<"    proceso:"<<cvlc_cam1->processId();
}

void MainWindow::Error_proc1()
{
    ui->C1_show->append(cvlc_cam1->readAllStandardError());
}

void MainWindow::datosRecibido2()
{
    //ui->C2_init->append(cvlc_cam2->readAllStandardOutput());
}

void MainWindow::iniciado2()
{
    qDebug()<<"programa2: "<<cvlc_cam1->program()<<"    proceso:"<<cvlc_cam2->processId();
}

void MainWindow::Error_proc2()
{
    ui->C2_show->append(cvlc_cam2->readAllStandardError());
}

void MainWindow::datosRecibido3()
{
    ui->py_show->append(motoresPy->readAllStandardOutput());
}

void MainWindow::iniciado3()
{
    qDebug()<<"programa2: "<<motoresPy->program()<<"    proceso:"<<motoresPy->processId();
}

void MainWindow::Error_proc3()
{
    ui->py_show->append(motoresPy->readAllStandardError());
}

void MainWindow::estadoCambiado()
{
    const QString content = QDateTime::currentDateTime().toString("dd.MM.yy hh:mm:ss.zzz")
                    + QLatin1String(": Estado de conexion: ")
                    + texto(cliente->state());//QString::number(cliente->state())
                    //+ QLatin1Char('\n');
    ui->mqtt_show->append(content);
}

void MainWindow::brokerConectado()
{
    const QString content = QDateTime::currentDateTime().toString("dd.MM.yy hh:mm:ss.zzz")
            + QLatin1String(": Broker conectado");
    ui->mqtt_show->append(content);

    QString topic;
    QString mensaje;

    topic="/uv/lab1/test1";//servidor1";
    mensaje=ui->linea_IP->text().remove(0,4)+",8554/live"+",8555/live";   //"hola mundo";

    if (cliente->publish(topic,mensaje.toUtf8()) == -1)
        QMessageBox::critical(this, QLatin1String("Error"), QLatin1String("No es posible enviar el mensaje./nIntente nuevamente"));
    else{
        const QString content2 = QDateTime::currentDateTime().toString("dd.MM.yy hh:mm:ss.zzz")
                + QLatin1String(": Mensaje enviado");
        ui->mqtt_show->append(content2);
    }
    const QString content3 = QDateTime::currentDateTime().toString("dd.MM.yy hh:mm:ss.zzz")
            + QLatin1String(": Mensaje: ")
            +mensaje;
    ui->mqtt_show->append(content3);
}

