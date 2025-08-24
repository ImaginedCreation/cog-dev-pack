from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget, QHeaderView, QRadioButton, QTableWidgetItem

from _ui.uhexconverter import Ui_UHexConverter


class _HexList(Enum):
    Hex2 = "2进制"
    Hex8 = "8进制"
    Hex10 = "10进制"
    Hex16 = "16进制"


class _Result:
    def __init__(self):
        self.b2 = None
        self.b8 = None
        self.b10 = None
        self.b16 = None


class HexConverter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UHexConverter()
        self.ui.setupUi(self)
        self.setWindowTitle("进制转换")
        self.init_table()
        self.render_table(_Result(),_HexList.Hex10)

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
        current_type=_HexList.Hex2
        if hex_t == _HexList.Hex2.value:
           result=self.b2_converter(content)
           current_type=_HexList.Hex2
        elif hex_t==_HexList.Hex8.value:
            result=self.b8_converter(content)
            current_type=_HexList.Hex8
        elif hex_t == _HexList.Hex10.value:
            result = self.b10_converter(content)
            current_type = _HexList.Hex10
        elif hex_t == _HexList.Hex16.value:
            result = self.b16_converter(content)
            current_type = _HexList.Hex16
        self.render_table(result,current_type)


    def render_table(self,result:_Result,current_type:_HexList):
        self.ui.res_table.setItem(0,0,QTableWidgetItem(_HexList.Hex2.value))
        self.ui.res_table.setItem(0,1,QTableWidgetItem(result.b2))
        self.ui.res_table.setItem(0,2,QTableWidgetItem(f"{current_type.value}转2进制"))

        self.ui.res_table.setItem(1, 0, QTableWidgetItem(_HexList.Hex8.value))
        self.ui.res_table.setItem(1, 1, QTableWidgetItem(result.b8))
        self.ui.res_table.setItem(1, 2, QTableWidgetItem(f"{current_type.value}转8进制"))

        self.ui.res_table.setItem(2, 0, QTableWidgetItem(_HexList.Hex10.value))
        self.ui.res_table.setItem(2, 1, QTableWidgetItem(result.b10))
        self.ui.res_table.setItem(2, 2, QTableWidgetItem(f"{current_type.value}转10进制"))

        self.ui.res_table.setItem(3, 0, QTableWidgetItem(_HexList.Hex16.value))
        self.ui.res_table.setItem(3, 1, QTableWidgetItem(result.b16))
        self.ui.res_table.setItem(3, 2, QTableWidgetItem(f"{current_type.value}转16进制"))

    @staticmethod
    def b16_converter(b16_str):
        result=_Result()
        result.b2=bin(int(b16_str,16))[2:]
        result.b8=oct(int(b16_str,16))[2:]
        result.b10=str(int(b16_str,16))
        result.b16=b16_str
        return result

    @staticmethod
    def b10_converter(b10_str):
        result=_Result()
        result.b2=bin(int(b10_str,10))[2:]
        result.b8=oct(int(b10_str,10))[2:]
        result.b10=b10_str
        result.b16=hex(int(b10_str,10))[2:]
        return result

    @staticmethod
    def b8_converter(b8_str):
        result=_Result()
        result.b2=bin(int(b8_str,8))[2:]
        result.b8=b8_str
        result.b10=str(int(b8_str,8))
        result.b16=hex(int(b8_str,8))[2:]
        return result

    @staticmethod
    def b2_converter(b2_str):
        result=_Result()
        result.b2=b2_str
        result.b8=oct(int(b2_str,2))[2:]
        result.b10=str(int(b2_str,2))
        result.b16=hex(int(b2_str,2))[2:]
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
