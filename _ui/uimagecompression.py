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
        UImageCompression.resize(400, 300)
        UImageCompression.setMinimumSize(QSize(400, 300))
        UImageCompression.setMaximumSize(QSize(400, 300))
        UImageCompression.setBaseSize(QSize(400, 300))
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

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.open_file_btn = QPushButton(UImageCompression)
        self.open_file_btn.setObjectName(u"open_file_btn")

        self.gridLayout.addWidget(self.open_file_btn, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.folder_open_btn = QPushButton(UImageCompression)
        self.folder_open_btn.setObjectName(u"folder_open_btn")

        self.gridLayout.addWidget(self.folder_open_btn, 4, 0, 1, 1)

        self.description_label = QLabel(UImageCompression)
        self.description_label.setObjectName(u"description_label")

        self.gridLayout.addWidget(self.description_label, 3, 0, 1, 1)

        self.widget_2 = QWidget(UImageCompression)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSlider = QSlider(self.widget_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)


        self.retranslateUi(UImageCompression)

        QMetaObject.connectSlotsByName(UImageCompression)
    # setupUi

    def retranslateUi(self, UImageCompression):
        UImageCompression.setWindowTitle(QCoreApplication.translate("UImageCompression", u"Form", None))
        self.label.setText(QCoreApplication.translate("UImageCompression", u"\u76ee\u6807\u683c\u5f0f:", None))
        self.groupBox.setTitle("")
        self.radioButton_3.setText(QCoreApplication.translate("UImageCompression", u"jpeg ", None))
        self.radioButton_2.setText(QCoreApplication.translate("UImageCompression", u"jpg ", None))
        self.radioButton.setText(QCoreApplication.translate("UImageCompression", u"png ", None))
        self.open_file_btn.setText(QCoreApplication.translate("UImageCompression", u"\u9009\u62e9\u6587\u4ef6", None))
        self.folder_open_btn.setText(QCoreApplication.translate("UImageCompression", u"\u70b9\u51fb\u538b\u7f29,\u538b\u7f29\u6210\u679c\u540e\u6253\u5f00\u76ee\u5f55", None))
        self.description_label.setText(QCoreApplication.translate("UImageCompression", u"\u7ed3\u679c:", None))
        self.label_2.setText(QCoreApplication.translate("UImageCompression", u"\u76ee\u6807\u8d28\u91cf:", None))
        self.label_3.setText(QCoreApplication.translate("UImageCompression", u"10%", None))
    # retranslateUi

