import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PoseListWidget(QListWidget):
    def __init__(self, parent=None):
        super(PoseListWidget, self).__init__(parent)

        self.setViewMode(QListView.IconMode)
        self.setResizeMode(QListView.Adjust)
        self.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setIconSize(QSize(90, 90))
        self.setSpacing(2)


class PoseLibraryWidget(QWidget):
    def __init__(self, parent=None):
        super(PoseLibraryWidget, self).__init__(parent)

        # Window
        self.setWindowTitle('Pose Library')
        self.resize(600, 400)

        # Tree

        # Pose List
        self.poseList = PoseListWidget()
        for i in range(1000):
            QListWidgetItem(str(i), self.poseList)

        # Layout
        QHBoxLayout(self)

        self.layout().addWidget(self.poseList)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PoseLibraryWidget()
    window.show()
    quitCode = app.exec_()
    sys.exit(quitCode)
