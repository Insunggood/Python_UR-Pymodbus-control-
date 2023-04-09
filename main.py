from PyQt5 import QtCore, QtGui, QtWidgets

import time

import threading

from pymodbus.client import ModbusTcpClient


class Ui_Dialog(object):
    def __init__(self):
        self.client = ModbusTcpClient(host='192.168.0.17', port=502, auto_open=True, unit_id=1, auto_close=False)
        t = threading.Thread(target=self.check_io, args=(self.client,))
        t.daemon = True
        t.start()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 397)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(460, 20, 91, 251))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 220, 71, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 310, 71, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(370, 220, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 310, 71, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(273, 240, 21, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(393, 240, 21, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(273, 290, 21, 20))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(393, 290, 21, 20))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 110, 141, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_1.clicked.connect(self.pushBtn1_click)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.pushBtn2_click)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.pushBtn3_click)

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.pushBtn4_click)

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Position 1"))
        self.label_2.setText(_translate("Dialog", "Position 4"))
        self.label_3.setText(_translate("Dialog", "Position 2"))
        self.label_4.setText(_translate("Dialog", "Position 3"))
        self.pushButton_1.setText(_translate("Dialog", "Position 1"))
        self.pushButton_2.setText(_translate("Dialog", "Position 2"))
        self.pushButton_3.setText(_translate("Dialog", "Position 3"))
        self.pushButton_4.setText(_translate("Dialog", "Position 4"))



    def pushBtn1_click(self):  # Pos 1 이벤트 처리

        self.client.write_register(129, 1)
        self.label_5.setStyleSheet('border-image:url(./images/blue.jpg);border:0px;')
        self.label_6.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_7.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_8.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


    def pushBtn2_click(self):   # Pos 2 이벤트 처리

        self.client.write_register(129, 2)
        self.label_6.setStyleSheet('border-image:url(./images/blue.jpg);border:0px;')
        self.label_7.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_8.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_5.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')



    def pushBtn3_click(self):   # Pos 3 이벤트 처리

        self.client.write_register(129, 3)
        self.label_8.setStyleSheet('border-image:url(./images/blue.jpg);border:0px;')
        self.label_5.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_6.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_7.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')


    def pushBtn4_click(self):   # Pos 4 이벤트 처리

        self.client.write_register(129, 4)
        self.label_7.setStyleSheet('border-image:url(./images/blue.jpg);border:0px;')
        self.label_8.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_5.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')
        self.label_6.setStyleSheet('border-image:url(./images/red.jpg);border:0px;')

    def check_io(self, client):
        prev_result = None
        while True:
            curr_result = client.read_holding_registers(130).registers[0]
            print(curr_result)

            if prev_result != curr_result:
                if curr_result == 1:
                    self.label_5.setStyleSheet('border-image:url(./images/green.jpg);border:0px;')

                if curr_result == 2:
                    self.label_6.setStyleSheet('border-image:url(./images/green.jpg);border:0px;')

                if curr_result == 3:
                    self.label_8.setStyleSheet('border-image:url(./images/green.jpg);border:0px;')

                if curr_result == 4:
                    self.label_7.setStyleSheet('border-image:url(./images/green.jpg);border:0px;')

            prev_result = curr_result
            time.sleep(0.1)


    def __del__(self):  # UI 종료 이벤트

        self.client.close()

        print("App Exiting....")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

