# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dfa_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItem

from DFA import DFA
from Model import dfa_model_list, ndfa_list, ndfa_model_list, regex_model_list
from Model import dfa_list
from NDFA import NDFA
from Regex import Regex

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


class Ui_create_regex_dialog(object):
    def __init__(self):
        self.dialog = QtGui.QDialog()
        self.setupUi(self.dialog)
        self.dialog.exec()

    def setupUi(self, create_regex_dialog):
        create_regex_dialog.setObjectName(_fromUtf8("create_regex_dialog"))
        create_regex_dialog.setWindowModality(QtCore.Qt.WindowModal)
        create_regex_dialog.resize(600, 100)
        create_regex_dialog.setMinimumSize(QtCore.QSize(600, 100))
        create_regex_dialog.setSizeGripEnabled(False)
        create_regex_dialog.setModal(True)
        self.formLayout = QtGui.QFormLayout(create_regex_dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(create_regex_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.dfa_alphabet = QtGui.QLineEdit(create_regex_dialog)
        self.dfa_alphabet.setToolTip(_fromUtf8(""))
        self.dfa_alphabet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dfa_alphabet.setObjectName(_fromUtf8("dfa_alphabet"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dfa_alphabet)
        self.add_regex_button = QtGui.QPushButton(create_regex_dialog)
        self.add_regex_button.setObjectName(_fromUtf8("add_regex_button"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.add_regex_button)
        self.widget = QtGui.QWidget(create_regex_dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.widget)

        self.retranslateUi(create_regex_dialog)
        QtCore.QMetaObject.connectSlotsByName(create_regex_dialog)

    def retranslateUi(self, create_regex_dialog):
        create_regex_dialog.setWindowTitle(_translate("create_regex_dialog", "Create REGEX", None))
        self.label.setText(_translate("create_regex_dialog", "Regex string", None))
        self.dfa_alphabet.setPlaceholderText(_translate("create_regex_dialog", "(a|b)*", None))
        self.add_regex_button.setText(_translate("create_regex_dialog", "Add new REGEX", None))

        self.add_regex_button.clicked.connect(self.create_regex)

    def create_regex(self):
        regex_string = self.dfa_alphabet.text()
        if regex_string != '':
            regex = Regex(regex_string)
            item = QStandardItem(regex_string)
            regex_model_list.appendRow(item)
            self.dialog.accept()



