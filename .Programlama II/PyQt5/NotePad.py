import sys
import os
from PyQt5 import QtWidgets


class NotePad(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazialani = QtWidgets.QTextEdit()

        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Dosya Aç")
        self.kaydet = QtWidgets.QPushButton("Dosyayı Kaydet")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazialani)
        v_box.addLayout(h_box)

        self.temizle.clicked.connect(self.metnitemizle)
        self.ac.clicked.connect(self.dosyaac)
        self.kaydet.clicked.connect(self.dosyakaydet)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.show()

    def metnitemizle(self):
        self.yazialani.clear()

    def dosyaac(self):
        dizin = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("Home"))
        with open(dizin[0], "r") as file:
            self.yazialani.setText(file.read())

    def dosyakaydet(self):
        dizin = QtWidgets.QFileDialog.getSaveFileName(self, "Dosyayı Kaydet", os.getenv("Home"))
        with open(dizin[0], "w") as file:
            file.write(self.yazialani.toPlainText())


app = QtWidgets.QApplication(sys.argv)
notepad = NotePad()
sys.exit(app.exec_())
