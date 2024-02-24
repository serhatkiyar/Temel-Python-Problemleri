import sys
import os
from PyQt5 import QtWidgets, QtSql


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazialani = QtWidgets.QLineEdit()
        self.textt = QtWidgets.QTextEdit()
        self.buton1 = QtWidgets.QPushButton("Dosya Aç")
        self.buton2 = QtWidgets.QPushButton("Temizle")
        self.buton3 = QtWidgets.QPushButton("Programı Kapat")
        self.buton4 = QtWidgets.QPushButton("Kaydet")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.textt)
        v_box.addWidget(self.buton2)
        v_box.addStretch()

        v_box2 = QtWidgets.QVBoxLayout()

        v_box2.addWidget(self.buton1)
        v_box2.addWidget(self.buton4)
        v_box2.addWidget(self.buton3)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addLayout(v_box)
        h_box.addLayout(v_box2)
        h_box.addStretch()

        self.setLayout(h_box)

        # self.buton1.clicked.connect()
        self.buton2.clicked.connect(self.temizle)
        self.buton3.clicked.connect(self.kapat)

        self.setWindowTitle("TurevAlici")
        self.show()

    def temizle(self):
        self.yazialani.clear()
        self.textt.clear()
    def kapat(self):
        sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
