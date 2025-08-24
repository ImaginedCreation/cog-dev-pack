# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uhexconverter.ui'
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
    QHeaderView, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_UHexConverter(object):
    def setupUi(self, UHexConverter):
        if not UHexConverter.objectName():
            UHexConverter.setObjectName(u"UHexConverter")
        UHexConverter.resize(800, 500)
        UHexConverter.setMinimumSize(QSize(800, 500))
        UHexConverter.setMaximumSize(QSize(800, 500))
        UHexConverter.setBaseSize(QSize(800, 500))
        self.gridLayout = QGridLayout(UHexConverter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(UHexConverter)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.widget.setBaseSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.content_input = QLineEdit(self.widget)
        self.content_input.setObjectName(u"content_input")

        self.horizontalLayout_2.addWidget(self.content_input)

        self.conver_btn = QPushButton(self.widget)
        self.conver_btn.setObjectName(u"conver_btn")

        self.horizontalLayout_2.addWidget(self.conver_btn)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.radio_group = QGroupBox(UHexConverter)
        self.radio_group.setObjectName(u"radio_group")
        self.radio_group.setMinimumSize(QSize(0, 40))
        self.radio_group.setMaximumSize(QSize(16777215, 40))
        self.radio_group.setBaseSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.radio_group)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_2 = QRadioButton(self.radio_group)
        self.radio_2.setObjectName(u"radio_2")

        self.horizontalLayout.addWidget(self.radio_2)

        self.radio_8 = QRadioButton(self.radio_group)
        self.radio_8.setObjectName(u"radio_8")

        self.horizontalLayout.addWidget(self.radio_8)

        self.radio_10 = QRadioButton(self.radio_group)
        self.radio_10.setObjectName(u"radio_10")

        self.horizontalLayout.addWidget(self.radio_10)

        self.radio_16 = QRadioButton(self.radio_group)
        self.radio_16.setObjectName(u"radio_16")

        self.horizontalLayout.addWidget(self.radio_16)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(4, 1)

        self.gridLayout.addWidget(self.radio_group, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.res_table = QTableWidget(UHexConverter)
        self.res_table.setObjectName(u"res_table")

        self.gridLayout.addWidget(self.res_table, 2, 0, 1, 1)


        self.retranslateUi(UHexConverter)

        QMetaObject.connectSlotsByName(UHexConverter)
    # setupUi

    def retranslateUi(self, UHexConverter):
        UHexConverter.setWindowTitle(QCoreApplication.translate("UHexConverter", u"Form", None))
        self.conver_btn.setText(QCoreApplication.translate("UHexConverter", u"\u8f6c\u6362", None))
        self.radio_group.setTitle("")
        self.radio_2.setText(QCoreApplication.translate("UHexConverter", u"2\u8fdb\u5236", None))
        self.radio_8.setText(QCoreApplication.translate("UHexConverter", u"8\u8fdb\u5236", None))
        self.radio_10.setText(QCoreApplication.translate("UHexConverter", u"10\u8fdb\u5236", None))
        self.radio_16.setText(QCoreApplication.translate("UHexConverter", u"16\u8fdb\u5236", None))
    # retranslateUi

