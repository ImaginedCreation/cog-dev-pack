import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget

from _ui.umain import Ui_UMain
from app_attr import GRoutes
from configure import MakeConfig, MODE
from hex_converter import HexConverter
import resources_rc
from image_compression import ImageCompression

config=MakeConfig(MODE.PRO)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_UMain()
        self.ui.setupUi(self)
        self.setWindowTitle(config.title)
        self._icon=QIcon(":/icons/icons/lg.png")
        self.setWindowIcon(self._icon)

        self.hex_converter_win = HexConverter()
        self.hex_converter_win.setWindowIcon(self._icon)
        # self.hex_converter_win.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.ui.hex_converter_btn.clicked.connect(lambda:self.on_to_router(GRoutes.HexConverter))

        self.image_compression_win=ImageCompression()
        self.image_compression_win.setWindowIcon(self._icon)
        self.ui.image_compression_btn.clicked.connect(lambda:self.on_to_router(GRoutes.ImageCompression))

    def on_to_router(self,route:GRoutes):
        if route==GRoutes.HexConverter:
            self.hex_converter_win.show()
            self.hex_converter_win.move(self.x()+120,self.y()-120)
        elif route==GRoutes.ImageCompression:
            self.image_compression_win.show()
            self.image_compression_win.move(self.x()+120,self.y()-120)

if __name__=="__main__":
    app=QApplication()
    main_window=MainWindow()
    main_window.show()
    sys.exit(app.exec())
