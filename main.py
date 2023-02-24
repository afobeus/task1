import sys
import random

from ui import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRect


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles_params = []
        self.pushButton.clicked.connect(self.add_circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for (x, y), radius, color in self.circles_params:
            qp.setBrush(QColor(*color))
            qp.drawEllipse(QRect(x, y, radius, radius))
        qp.end()

    def add_circle(self):
        diameter = random.randint(5, 50)
        cords = random.randint(0, self.width() - diameter), random.randint(0, self.height() - diameter)
        color = [random.randint(0, 255) for _ in range(3)]
        self.circles_params.append((cords, diameter, color))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
