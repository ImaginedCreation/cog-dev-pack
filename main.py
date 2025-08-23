import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

from _ui.umain import Ui_UMain
from app_attr import GRoutes
from configure import MakeConfig, MODE
from hex_converter import HexConverter

config=MakeConfig(MODE.PRO)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_UMain()
        self.ui.setupUi(self)
        self.setWindowTitle(config.title)

        self.hex_converter_win = HexConverter(self)
        self.hex_converter_win.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.ui.hex_converter_btn.clicked.connect(lambda:self.on_to_router(GRoutes.HexConverter))

    def on_to_router(self,route:GRoutes):
        if route==GRoutes.HexConverter:
            self.hex_converter_win.show()

if __name__=="__main__":
    app=QApplication()
    main_window=MainWindow()
    main_window.show()
    sys.exit(app.exec())
