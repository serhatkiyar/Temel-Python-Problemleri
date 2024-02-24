import sys

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris_butonu = QtWidgets.QPushButton("Giriş")
        self.yazi = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.giris_butonu)

        h_box = QtWidgets.QHBoxLayout()

        v_box.addStretch()
        h_box.addLayout(v_box)
        v_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Arayüzü")

        self.show()


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
