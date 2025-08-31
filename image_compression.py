import os
import re
import shutil
import subprocess
from PIL import Image
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QRadioButton

from _ui.uimagecompression import Ui_UImageCompression


class ImageCompression(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UImageCompression()
        self.ui.setupUi(self)
        self._count=1
        self._open_file_path=None
        self._target_dir=None
        self.ui.open_file_btn.clicked.connect(self.on_open_file)
        self.setWindowTitle("图片压缩")
        self.ui.qua.valueChanged.connect(self.on_qua_changed)
        self.ui.radioButton.clicked.connect(self.on_radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.on_radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.on_radio_clicked)
        self.ui.folder_open_btn.clicked.connect(self.on_start_compress)
        self.ui.open_dir_btn.clicked.connect(self.on_open_target_dir)

    def on_open_target_dir(self):
        print(self._target_dir)
        subprocess.run(["explorer", "/select,", self._target_dir])

    def on_start_compress(self):
        result=self.compress_image_keep_format(self._open_file_path)
        self.ui.target_file_label.setText(result['output_path'])
        self.ui.size_change.setText(
            f"压缩前: {result['original_size'] / (1024 * 1024):.2f} MB, 压缩后: {result['compressed_size'] / (1024 * 1024):.2f} MB"
        )
        self._target_dir=os.path.normpath(result['output_path'])
        print(f"原文件大小: {result['original_size']} 字节")
        print(f"压缩后大小: {result['compressed_size']} 字节")
        print(f"质量: {result['out_qua']}")
        print(f"压缩文件路径: {result['output_path']}")

    def on_radio_clicked(self):
        if self.ui.radioButton.isChecked():
            self.ui.qua.setMinimum(0)
            self.ui.qua.setMaximum(9)
        else:
            self.ui.qua.setMinimum(1)
            self.ui.qua.setMaximum(99)
        self.on_qua_changed()

    def on_qua_changed(self):
        if self.ui.radioButton.isChecked():
            self.ui.qua_text.setText(str(self.ui.qua.value()) + "级(值越大,压缩后越小)")
        else:
            self.ui.qua_text.setText(str(self.ui.qua.value()) + "%(值越小,压缩后越小)")


    def get_select_ext(self):
        for item in self.ui.ext_group.findChildren(QRadioButton):
            if item.isChecked():
                return item.text()
        return None

    def on_open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择图片文件",
            "",
            "图片文件 (*.png *.jpg *.jpeg)"
        )
        self.ui.file_path_label.setText(file_path)
        self._open_file_path=file_path

    def compress_image_keep_format(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError("文件不存在")

        base, ext = os.path.splitext(file_path)
        ext = ext.lower()
        file_dir = os.path.dirname(file_path)

        dir_name = os.path.join(file_dir, "_compress")
        os.makedirs(dir_name, exist_ok=True)
        new_file_path: str = os.path.join(dir_name, re.sub(r'[\u4e00-\u9fff\s]', '', os.path.basename(base)) + ext)
        print("dir_name:", dir_name)
        print("new_file_path:", new_file_path)
        shutil.copy(file_path, new_file_path)

        # 使用 Pillow 打开图片
        try:
            img = Image.open(new_file_path)
        except Exception as e:
            QMessageBox.warning(None, "tip", f"无法读取图片文件: {e}")
            return None

        out_ext = self.get_select_ext().strip()  # 去除扩展名的多余空格
        if not out_ext:
            QMessageBox.warning(None, "tip", "请选择输出的文件格式")
            return None

        # 获取滑块值
        slider_value = self.ui.qua.value()
        print(f"滑块值: {slider_value}")

        # 设置输出路径
        output_path, _ext = os.path.splitext(new_file_path)
        output_path += out_ext

        # 设置压缩参数
        if out_ext in [".jpg", ".jpeg"]:
            img = img.convert("RGB")  # 确保 JPEG 格式为 RGB 模式
            img.save(output_path, format="JPEG", quality=slider_value, optimize=True)
        elif out_ext == ".png":
            img.save(output_path, format="PNG", compress_level=slider_value)
        else:
            img.save(output_path)

        original_size = os.path.getsize(file_path)
        compressed_size = os.path.getsize(output_path)

        print(f"原文件大小: {original_size} 字节")
        print(f"压缩后大小: {compressed_size} 字节")

        return {
            "out_qua": slider_value,
            "output_path": output_path,
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compression_ratio": compressed_size / original_size if original_size else None
        }