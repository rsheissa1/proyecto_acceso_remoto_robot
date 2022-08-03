#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QProcess>
#include <QMqttClient>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QProcess *cvlc_cam1;
    QProcess *cvlc_cam2;
    QProcess *motoresPy;
    QString texto(int a);

public slots:
    void datosRecibido1();
    void iniciado1();
    void Error_proc1();
    void datosRecibido2();
    void iniciado2();
    void Error_proc2();
    void datosRecibido3();
    void iniciado3();
    void Error_proc3();

private:
    Ui::MainWindow *ui;
    QMqttClient *cliente;

private slots:
    void estadoCambiado();
    void brokerConectado();
};
#endif // MAINWINDOW_H
