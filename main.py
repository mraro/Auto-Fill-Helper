import sys
from PyQt5.QtWidgets import *



class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        btn = QPushButton("Add Source")
        combo = QComboBox()
        combo.addItems([
            "Title",
            "ID",
            "Description",
            "Float",
            "Int",
        ])

        combo.currentText()
        vb = QGridLayout(self)

        vb.addWidget(combo)
        vb.addWidget(btn)

if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec_())
