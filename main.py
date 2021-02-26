import random
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


        # self.setMouseTracking(True)
        self.timer_id = QtCore.QTimer()
        self.timer_animation = QtCore.QTimer()
        self.timer_animation.timeout.connect(self.go_paint)

        self.do_paint = False
        self.btn_go_paint.clicked.connect(self.go_paint)

    def paintEvent(self, event):
        n = random.randint(5, 100)
        # r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        r, g, b = 255, 255, 0
        qp = QPainter()
        qp.begin(self)
        self.draw_elips(qp, r, g, b, n)
        qp.end()

    def draw_elips(self, qp, r, g, b, n):
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, 700), random.randint(0, 700), n, n)

    def go_paint(self):
        c = 100
        self.timer_id.singleShot(c, self.explore)
        self.timer_animation.start(100)

    def explore(self):
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
