import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic.properties import QtGui


class YellowCirclesForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.circles = []

        self.painter = QPainter()

        self.init_ui()

    def init_ui(self):
        pass

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        self.draw_circles()
        self.painter.end()

    def draw_circles(self):
        for circle in self.circles:
            self.draw_circle(circle)

    def draw_circle(self, circle):
        self.painter.drawEllipse(circle.x, circle.y, circle.r, circle.r)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = YellowCirclesForm()
    wnd.show()
    sys.exit(app.exec())
