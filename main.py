import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRect


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles_params = []
        self.pushButton.clicked.connect(self.add_circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor("yellow"))
        for (x, y), radius in self.circles_params:
            qp.drawEllipse(QRect(x, y, radius, radius))
        qp.end()

    def add_circle(self):
        diameter = random.randint(5, 50)
        cords = random.randint(0, self.width() - diameter), random.randint(0, self.height() - diameter)
        self.circles_params.append((cords, diameter))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
