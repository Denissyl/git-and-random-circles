import sys
from random import randint

from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

from Circle import Circle


class YellowCirclesForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.circles = []

        self.painter = QPainter()

        self.init_ui()

    def init_ui(self):
        self.pb_draw_circles.clicked.connect(self.generate_circles)

    def generate_circles(self):
        self.circles.clear()
        for _ in range(10):
            self.circles.append(Circle(randint(0, self.width()),
                                       randint(0, self.height()),
                                       randint(10, 100)))
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.draw_circles()
        self.painter.end()

    def draw_circles(self):
        self.painter.setPen(QColor(255, 200, 0))
        for circle in self.circles:
            self.draw_circle(circle)

    def draw_circle(self, circle):
        self.painter.drawEllipse(circle.x - circle.r, circle.y - circle.r, circle.r * 2, circle.r * 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = YellowCirclesForm()
    wnd.show()
    sys.exit(app.exec())
