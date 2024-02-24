import sys

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.bas = 0
        self.buton = QtWidgets.QPushButton("Tıkla")
        self.yazi = QtWidgets.QLabel('0')

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()


    def click(self):
        self.bas += 1
        self.yazi.setText(f"{self.bas}")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
