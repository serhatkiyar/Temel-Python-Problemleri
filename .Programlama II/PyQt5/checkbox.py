import sys

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.checkbox = QtWidgets.QCheckBox()
        self.yazi = QtWidgets.QLabel("5 + 5 = 10")
        self.sonuc = QtWidgets.QLabel("")
        self.kontrol_butonu = QtWidgets.QPushButton("Kontrol Et")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.checkbox)
        h_box.addWidget(self.yazi)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.sonuc)
        v_box.addLayout(h_box)
        v_box.addWidget(self.kontrol_butonu)
        v_box.addStretch()

        self.kontrol_butonu.clicked.connect(self.click)

        self.setWindowTitle("CheckBox")
        self.setLayout(v_box)
        self.show()

    def click(self):
        if self.checkbox.isChecked():
            self.sonuc.setText("Doğru!")
        else:
            self.sonuc.setText("Yanlış!")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())