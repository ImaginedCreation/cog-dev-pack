# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uimagecompression.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QWidget)

class Ui_UImageCompression(object):
    def setupUi(self, UImageCompression):
        if not UImageCompression.objectName():
            UImageCompression.setObjectName(u"UImageCompression")
        UImageCompression.resize(500, 350)
        UImageCompression.setMinimumSize(QSize(500, 350))
        UImageCompression.setMaximumSize(QSize(500, 350))
        UImageCompression.setBaseSize(QSize(500, 350))
        self.gridLayout = QGridLayout(UImageCompression)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(UImageCompression)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.ext_group = QGroupBox(self.widget)
        self.ext_group.setObjectName(u"ext_group")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_group.sizePolicy().hasHeightForWidth())
        self.ext_group.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.ext_group)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_3 = QRadioButton(self.ext_group)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.ext_group)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.ext_group)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.horizontalLayout.addWidget(self.ext_group)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)

        self.description_label = QLabel(UImageCompression)
        self.description_label.setObjectName(u"description_label")

        self.gridLayout.addWidget(self.description_label, 5, 0, 1, 1)

        self.size_change = QLabel(UImageCompression)
        self.size_change.setObjectName(u"size_change")

        self.gridLayout.addWidget(self.size_change, 9, 0, 1, 1)

        self.widgeta = QWidget(UImageCompression)
        self.widgeta.setObjectName(u"widgeta")
        self.horizontalLayout_3 = QHBoxLayout(self.widgeta)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widgeta)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.qua = QSlider(self.widgeta)
        self.qua.setObjectName(u"qua")
        self.qua.setMinimum(1)
        self.qua.setPageStep(1)
        self.qua.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.qua)

        self.qua_text = QLabel(self.widgeta)
        self.qua_text.setObjectName(u"qua_text")

        self.horizontalLayout_3.addWidget(self.qua_text)


        self.gridLayout.addWidget(self.widgeta, 4, 0, 1, 1)

        self.widget_2 = QWidget(UImageCompression)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.widget_2.setBaseSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.file_path_label = QLabel(self.widget_2)
        self.file_path_label.setObjectName(u"file_path_label")

        self.horizontalLayout_4.addWidget(self.file_path_label, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.folder_open_btn = QPushButton(UImageCompression)
        self.folder_open_btn.setObjectName(u"folder_open_btn")

        self.gridLayout.addWidget(self.folder_open_btn, 6, 0, 1, 1)

        self.open_file_btn = QPushButton(UImageCompression)
        self.open_file_btn.setObjectName(u"open_file_btn")

        self.gridLayout.addWidget(self.open_file_btn, 0, 0, 1, 1)

        self.target_file_label = QLabel(UImageCompression)
        self.target_file_label.setObjectName(u"target_file_label")

        self.gridLayout.addWidget(self.target_file_label, 8, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.open_dir_btn = QPushButton(UImageCompression)
        self.open_dir_btn.setObjectName(u"open_dir_btn")

        self.gridLayout.addWidget(self.open_dir_btn, 7, 0, 1, 1)


        self.retranslateUi(UImageCompression)

        QMetaObject.connectSlotsByName(UImageCompression)
    # setupUi

    def retranslateUi(self, UImageCompression):
        UImageCompression.setWindowTitle(QCoreApplication.translate("UImageCompression", u"Form", None))
        self.label.setText(QCoreApplication.translate("UImageCompression", u"\u76ee\u6807\u683c\u5f0f:", None))
        self.ext_group.setTitle("")
        self.radioButton_3.setText(QCoreApplication.translate("UImageCompression", u".jpeg ", None))
        self.radioButton_2.setText(QCoreApplication.translate("UImageCompression", u".jpg ", None))
        self.radioButton.setText(QCoreApplication.translate("UImageCompression", u".png ", None))
        self.description_label.setText(QCoreApplication.translate("UImageCompression", u"\u7ed3\u679c:", None))
        self.size_change.setText(QCoreApplication.translate("UImageCompression", u"\u5927\u5c0f\u53d8\u5316", None))
        self.label_2.setText(QCoreApplication.translate("UImageCompression", u"\u76ee\u6807\u8d28\u91cf:", None))
        self.qua_text.setText(QCoreApplication.translate("UImageCompression", u"0%", None))
        self.label_3.setText(QCoreApplication.translate("UImageCompression", u"\u6e90\u6587\u4ef6:", None))
        self.file_path_label.setText(QCoreApplication.translate("UImageCompression", u"NULL", None))
        self.folder_open_btn.setText(QCoreApplication.translate("UImageCompression", u"\u70b9\u51fb\u538b\u7f29", None))
        self.open_file_btn.setText(QCoreApplication.translate("UImageCompression", u"\u9009\u62e9\u6587\u4ef6", None))
        self.target_file_label.setText(QCoreApplication.translate("UImageCompression", u"\u76ee\u6807\u8def\u5f84", None))
        self.open_dir_btn.setText(QCoreApplication.translate("UImageCompression", u"\u6253\u5f00\u76ee\u6807\u6587\u4ef6\u6240\u5728\u76ee\u5f55", None))
    # retranslateUi

