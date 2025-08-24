import os
import shutil

import cv2
from PySide6.QtWidgets import QWidget, QFileDialog

from _ui.uimagecompression import Ui_UImageCompression


class ImageCompression(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UImageCompression()
        self.ui.setupUi(self)
        self.ui.open_file_btn.clicked.connect(self.on_open_file)
        self.setWindowTitle("图片压缩")

    def on_open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择图片文件",
            "",
            "图片文件 (*.png *.jpg *.jpeg)"
        )
        result=self.compress_image_keep_format(file_path)
        print(f"原文件大小: {result['original_size']} 字节")
        print(f"压缩后大小: {result['compressed_size']} 字节")
        print(f"压缩率: {result['compression_ratio']:.2%}")
        print(f"备份路径: {result['backup_path']}")
        print(f"压缩文件路径: {result['output_path']}")

    @staticmethod
    def compress_image_keep_format(file_path, jpeg_quality=30, png_compression=9):
        if not os.path.isfile(file_path):
            raise FileNotFoundError("文件不存在")

        backup_path = file_path + ".bak"
        shutil.copy(file_path, backup_path)

        base, ext = os.path.splitext(file_path)
        ext = ext.lower()
        img = cv2.imread(file_path)
        if img is None:
            raise ValueError("无法读取图片文件")

        output_path = f"{base}_compressed{ext}"

        if ext in [".jpg", ".jpeg"]:
            cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])
        elif ext == ".png":
            cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            # output_path = output_path.replace('.png', '.jpg')
            # cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, 1])
        else:
            # 其它格式直接保存，不做特殊压缩
            cv2.imwrite(output_path, img)

        original_size = os.path.getsize(file_path)
        compressed_size = os.path.getsize(output_path)

        return {
            "backup_path": backup_path,
            "output_path": output_path,
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compression_ratio": compressed_size / original_size if original_size else None
        }
