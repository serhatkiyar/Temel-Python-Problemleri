import sys

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.bas = 0
        self.yazialani = QtWidgets.QLabel("Bana henüz tıklanmadı!")
        self.buton = QtWidgets.QPushButton("Tıkla")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.buton)
        h_box.addWidget(self.yazialani)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)

        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):
        self.bas += 1
        self.yazialani.setText(f"Bana {self.bas} defa tıklandı")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
