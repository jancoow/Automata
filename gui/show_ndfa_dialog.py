# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_dfa_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtTest

from PyQt4 import QtCore, QtGui
import time

from PyQt4.QtGui import QStandardItem

from Model import dfa_list, dfa_model_list, ndfa_list, ndfa_model_list

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_ShowNdfa(object):
    def __init__(self, NDFA):
        self.NDFA = NDFA
        self.NDFA.get_graph("tmp")

        self.dialog = QtGui.QDialog()
        self.setupUi(self.dialog)
        self.dialog.exec()

    def setupUi(self, ShowNdfa):
        ShowNdfa.setObjectName(_fromUtf8("ShowNdfa"))
        ShowNdfa.resize(756, 473)
        self.gridLayout = QtGui.QGridLayout(ShowNdfa)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(ShowNdfa)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 3, 0, 1, 1)
        self.widget = QtGui.QWidget(ShowNdfa)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ShowNdfa)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(ShowNdfa)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_4 = QtGui.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 1)

        self.retranslateUi(ShowNdfa)
        QtCore.QMetaObject.connectSlotsByName(ShowNdfa)

    def retranslateUi(self, ShowNdfa):
        ShowNdfa.setWindowTitle(_translate("ShowNdfa", "Show NDFA", None))
        self.label.setText(_translate("ShowNdfa", "Check string", None))
        self.pushButton.setText(_translate("ShowNdfa", "Check", None))
        self.pushButton_2.setText(_translate("ShowNdfa", "Step by step", None))
        self.label_2.setText(_translate("ShowNdfa", "~", None))
        self.pushButton_4.setText(_translate("ShowNdfa", "To DFA", None))

        self.pushButton.clicked.connect(self.accept_input)
        self.pushButton_2.clicked.connect(self.accept_input_step)
        self.pushButton_4.clicked.connect(self.to_dfa)

        self.update_graph()

    def accept_input(self):
        ex_time = 0
        try:
            start_time = time.time()
            output = self.NDFA.accept(self.lineEdit.text())
            ex_time = time.time() - start_time
            if output:
                output = "String accepted"
            else:
                output = "String not accepted"
        except Exception as e:
            output = e.args[0]

        self.label_2.setText("Result: " + output + '\nExecution time: ' + str(round(ex_time * 1000, 4)) + " ms")

    def accept_input_step(self):
        states = self.NDFA.start
        i = 1
        for char in self.lineEdit.text():
            states = self.NDFA.accept_step(char, states)
            self.NDFA.get_graph("tmp", states)
            self.update_graph()
            i += 1
            self.label_2.setText("Step " + str(i) + ": " + char)
            QtTest.QTest.qWait(1000)

        output = set(states).intersection(self.NDFA.finals)

        if output:
            output = "String accepted"
        else:
            output = "String not accepted"
        self.label_2.setText("Result: " + output)

    def to_dfa(self):
        new_dfa = self.NDFA.to_dfa()
        dfa_list.append(new_dfa)
        item = QStandardItem(new_dfa.get_tuple_string())

        dfa_model_list.appendRow(item)

    def update_graph(self):
        scene = QtGui.QGraphicsScene()
        pic = QtGui.QPixmap("output/tmp.png")
        scene.addItem(QtGui.QGraphicsPixmapItem(pic))
        self.graphicsView.setScene(scene)
        self.graphicsView.update()

