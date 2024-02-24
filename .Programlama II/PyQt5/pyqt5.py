import sys
from PyQt5 import QtWidgets, QtGui

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")

    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("resim.jpg"))
    etiket2.move(0, 0)

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("TEXT")
    etiket1.move(960, 540)



    pencere.setGeometry(0, 0, 1920, 1080)
    pencere.show()

    sys.exit(app.exec_())


pencere()
