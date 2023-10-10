from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from  random import randint
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
win.resize(300,300)
win.setWindowTitle("Generator")
mainline = QVBoxLayout()

lbl = QLabel("Generate numer of winner")
lblWin = QLabel("?")
btn = QPushButton("Generate winner")

mainline.addWidget(lbl, alignment = Qt.AlignCenter)
mainline.addWidget(lblWin, alignment= Qt.AlignCenter)
mainline.addWidget(btn, alignment= Qt.AlignCenter)

def winnerShow ():
    num = randint(1,1000)
    lbl.setText("winner")
    lblWin.setText(str(num))
btn.clicked.connect(winnerShow)
win.setLayout(mainline)
win.show()
app.exec()