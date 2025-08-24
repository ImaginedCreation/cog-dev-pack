from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget, QHeaderView, QRadioButton, QTableWidgetItem

from _ui.uhexconverter import Ui_UHexConverter


class _HexList(Enum):
    BIN = "2进制"
    OCT = "8进制"
    DEC = "10进制"
    HEX = "16进制"


class _Result:
    def __init__(self):
        self.bin = None
        self.oct = None
        self.dec = None
        self.hex = None


class HexConverter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UHexConverter()
        self.ui.setupUi(self)
        self.setWindowTitle("进制转换")
        self.init_table()
        self.render_table(_Result(),_HexList.DEC)

        self.ui.conver_btn.clicked.connect(self.on_converter)

    def on_converter(self):
        current_checked = None
        current_input_text = self.ui.content_input.text()
        for item in self.ui.radio_group.findChildren(QRadioButton):
            if item.isChecked():
                current_checked = item.text()
        if current_checked and current_input_text:
            self.update_result(current_checked, current_input_text)

    def update_result(self, hex_t: _HexList, content):
        result=_Result()
        current_type = _HexList.BIN
        try:
            if hex_t == _HexList.BIN.value:
                result = self.bin_converter(content)
                current_type = _HexList.BIN
            elif hex_t == _HexList.OCT.value:
                result = self.oct_converter(content)
                current_type = _HexList.OCT
            elif hex_t == _HexList.DEC.value:
                result = self.dec_converter(content)
                current_type = _HexList.DEC
            elif hex_t == _HexList.HEX.value:
                result = self.hex_converter(content)
                current_type = _HexList.HEX
            self.render_table(result, current_type)
        except Exception as e:
            self.render_table(result, current_type)

    def render_table(self,result:_Result,current_type:_HexList):
        self.ui.res_table.setItem(0,0,QTableWidgetItem(_HexList.BIN.value))
        self.ui.res_table.setItem(0,1,QTableWidgetItem(result.bin))
        self.ui.res_table.setItem(0,2,QTableWidgetItem(f"{current_type.value}转2进制"))

        self.ui.res_table.setItem(1, 0, QTableWidgetItem(_HexList.OCT.value))
        self.ui.res_table.setItem(1, 1, QTableWidgetItem(result.oct))
        self.ui.res_table.setItem(1, 2, QTableWidgetItem(f"{current_type.value}转8进制"))

        self.ui.res_table.setItem(2, 0, QTableWidgetItem(_HexList.DEC.value))
        self.ui.res_table.setItem(2, 1, QTableWidgetItem(result.dec))
        self.ui.res_table.setItem(2, 2, QTableWidgetItem(f"{current_type.value}转10进制"))

        self.ui.res_table.setItem(3, 0, QTableWidgetItem(_HexList.HEX.value))
        self.ui.res_table.setItem(3, 1, QTableWidgetItem(result.hex))
        self.ui.res_table.setItem(3, 2, QTableWidgetItem(f"{current_type.value}转16进制"))

    @staticmethod
    def hex_converter(hex_str):
        result=_Result()
        result.bin=bin(int(hex_str,16))[2:]
        result.oct=oct(int(hex_str,16))[2:]
        result.dec=str(int(hex_str,16))
        result.hex=hex_str
        return result

    @staticmethod
    def dec_converter(dec_str):
        result=_Result()
        result.bin=bin(int(dec_str,10))[2:]
        result.oct=oct(int(dec_str,10))[2:]
        result.dec=dec_str
        result.hex=hex(int(dec_str,10))[2:]
        return result

    @staticmethod
    def oct_converter(oct_str):
        result=_Result()
        result.bin=bin(int(oct_str,8))[2:]
        result.oct=oct_str
        result.dec=str(int(oct_str,8))
        result.hex=hex(int(oct_str,8))[2:]
        return result

    @staticmethod
    def bin_converter(bin_str):
        result=_Result()
        result.bin=bin_str
        result.oct=oct(int(bin_str,2))[2:]
        result.dec=str(int(bin_str,2))
        result.hex=hex(int(bin_str,2))[2:]
        return result

    def init_table(self):
        self.ui.res_table.verticalHeader().setVisible(False)
        self.ui.res_table.setColumnCount(3)
        self.ui.res_table.setRowCount(4)
        self.ui.res_table.setHorizontalHeaderLabels(["进制", "结果", "描述"])
        header = self.ui.res_table.horizontalHeader()
        header.setStyleSheet("border-bottom: 2px solid #888;")
        header.setSectionResizeMode(0, QHeaderView.Fixed)  # 第1列固定宽度
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # 第2列自动填充
        header.setSectionResizeMode(2, QHeaderView.Fixed)  # 第3列固定宽度
        self.ui.res_table.setColumnWidth(0, 100)  # 第1列宽度
        self.ui.res_table.setColumnWidth(2, 100)  # 第3列宽度
