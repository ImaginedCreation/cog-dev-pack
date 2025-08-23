# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'umain.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_UMain(object):
    def setupUi(self, UMain):
        if not UMain.objectName():
            UMain.setObjectName(u"UMain")
        UMain.resize(700, 700)
        UMain.setMinimumSize(QSize(700, 700))
        UMain.setMaximumSize(QSize(700, 700))
        UMain.setBaseSize(QSize(700, 700))
        self.verticalLayout = QVBoxLayout(UMain)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.header_container = QWidget(UMain)
        self.header_container.setObjectName(u"header_container")
        self.header_container.setMinimumSize(QSize(0, 120))
        self.header_container.setMaximumSize(QSize(16777215, 120))
        self.header_container.setBaseSize(QSize(0, 120))
        self.verticalLayout_2 = QVBoxLayout(self.header_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.header_container)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)


        self.verticalLayout.addWidget(self.header_container, 0, Qt.AlignmentFlag.AlignVCenter)

        self.hex_converter_btn = QPushButton(UMain)
        self.hex_converter_btn.setObjectName(u"hex_converter_btn")

        self.verticalLayout.addWidget(self.hex_converter_btn, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(UMain)

        QMetaObject.connectSlotsByName(UMain)
    # setupUi

    def retranslateUi(self, UMain):
        UMain.setWindowTitle(QCoreApplication.translate("UMain", u"Form", None))
        self.title.setText(QCoreApplication.translate("UMain", u"COG Dev Pack", None))
        self.hex_converter_btn.setText(QCoreApplication.translate("UMain", u"\u8fdb\u5236\u8f6c\u6362", None))
    # retranslateUi

