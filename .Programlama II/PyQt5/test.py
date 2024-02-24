import sys
from PyQt5 import QtWidgets

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    buton1 = QtWidgets.QPushButton("Buton1")
    buton2 = QtWidgets.QPushButton("Buton2")

    v_box = QtWidgets.QVBoxLayout()


    v_box.addWidget(buton1)
    v_box.addWidget(buton2)

    h_box = QtWidgets.QHBoxLayout()
    h_box.addLayout(v_box)

    pencere = QtWidgets.QWidget()
    pencere.setLayout(h_box)
    pencere.setLayout(v_box)
    pencere.setWindowTitle("PyQt5 öğreniyorum")
    pencere.setGeometry(400, 400, 900, 900)
    pencere.show()

    sys.exit(app.exec_())


pencere()