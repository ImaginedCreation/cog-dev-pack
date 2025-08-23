from PySide6.QtWidgets import QMainWindow, QWidget

from _ui.uhexconverter import Ui_UHexConverter


class HexConverter(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui=Ui_UHexConverter()
        self.ui.setupUi(self)
