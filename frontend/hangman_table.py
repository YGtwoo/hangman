# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hangman_wid.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class TablePoints(object):
    def setup_ui(self, table_points):
        table_points.setObjectName("table_points")
        table_points.resize(241, 353)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(9)
        table_points.setFont(font)
        table_points.setStyleSheet("")
        self.tableWidget = QtWidgets.QTableWidget(table_points)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 241, 355))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslate_ui(table_points)
        QtCore.QMetaObject.connectSlotsByName(table_points)

    def table_name(self):
        with open('name_points.txt', encoding='ANSI') as file:
            lst_name_points = [l.split() for l in file.readlines()]
            for lst in lst_name_points:
                col = 0
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for item in lst:
                    cellinfo = QTableWidgetItem(item)
                    self.tableWidget.setItem(rowPosition, col, cellinfo)
                    col += 1
        self.tableWidget.sortItems(0)

    def retranslate_ui(self, table_points):
        _translate = QtCore.QCoreApplication.translate
        table_points.setWindowTitle(_translate("table_points", "Form"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("table_points", "Имя игрока"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("table_points", "Очки"))
