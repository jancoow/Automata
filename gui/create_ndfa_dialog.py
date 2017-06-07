# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dfa_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItem

from DFA import DFA
from Model import dfa_model_list, ndfa_list, ndfa_model_list
from Model import dfa_list
from NDFA import NDFA

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


class Ui_create_ndfa_dialog(object):
    def __init__(self):
        self.dialog = QtGui.QDialog()
        self.setupUi(self.dialog)
        self.dialog.exec()

    def setupUi(self, create_ndfa_dialog):
        create_ndfa_dialog.setObjectName(_fromUtf8("create_ndfa_dialog"))
        create_ndfa_dialog.setWindowModality(QtCore.Qt.WindowModal)
        create_ndfa_dialog.resize(785, 354)
        create_ndfa_dialog.setMinimumSize(QtCore.QSize(600, 300))
        create_ndfa_dialog.setSizeGripEnabled(False)
        create_ndfa_dialog.setModal(True)
        self.formLayout = QtGui.QFormLayout(create_ndfa_dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(create_ndfa_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.dfa_alphabet = QtGui.QLineEdit(create_ndfa_dialog)
        self.dfa_alphabet.setToolTip(_fromUtf8(""))
        self.dfa_alphabet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dfa_alphabet.setObjectName(_fromUtf8("dfa_alphabet"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dfa_alphabet)
        self.label_2 = QtGui.QLabel(create_ndfa_dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dfa_start = QtGui.QLineEdit(create_ndfa_dialog)
        self.dfa_start.setText(_fromUtf8(""))
        self.dfa_start.setObjectName(_fromUtf8("dfa_start"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dfa_start)
        self.label_3 = QtGui.QLabel(create_ndfa_dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dfa_finals = QtGui.QLineEdit(create_ndfa_dialog)
        self.dfa_finals.setObjectName(_fromUtf8("dfa_finals"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dfa_finals)
        self.label_4 = QtGui.QLabel(create_ndfa_dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dfa_transitions = QtGui.QTableWidget(create_ndfa_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dfa_transitions.sizePolicy().hasHeightForWidth())
        self.dfa_transitions.setSizePolicy(sizePolicy)
        self.dfa_transitions.setMinimumSize(QtCore.QSize(0, 0))
        self.dfa_transitions.setShowGrid(True)
        self.dfa_transitions.setGridStyle(QtCore.Qt.SolidLine)
        self.dfa_transitions.setRowCount(10)
        self.dfa_transitions.setColumnCount(3)
        self.dfa_transitions.setObjectName(_fromUtf8("dfa_transitions"))
        item = QtGui.QTableWidgetItem()
        self.dfa_transitions.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.dfa_transitions.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.dfa_transitions.setHorizontalHeaderItem(2, item)
        self.dfa_transitions.horizontalHeader().setVisible(True)
        self.dfa_transitions.horizontalHeader().setStretchLastSection(True)
        self.dfa_transitions.verticalHeader().setVisible(False)
        self.dfa_transitions.verticalHeader().setHighlightSections(True)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dfa_transitions)
        self.add_dfa_button = QtGui.QPushButton(create_ndfa_dialog)
        self.add_dfa_button.setObjectName(_fromUtf8("add_dfa_button"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.add_dfa_button)

        self.retranslateUi(create_ndfa_dialog)
        QtCore.QMetaObject.connectSlotsByName(create_ndfa_dialog)

    def retranslateUi(self, create_ndfa_dialog):
        create_ndfa_dialog.setWindowTitle(_translate("create_ndfa_dialog", "Create NDFA", None))
        self.label.setText(_translate("create_ndfa_dialog", "Alphabet", None))
        self.dfa_alphabet.setPlaceholderText(_translate("create_ndfa_dialog", "a,b,c", None))
        self.label_2.setText(_translate("create_ndfa_dialog", "Start", None))
        self.dfa_start.setPlaceholderText(_translate("create_ndfa_dialog", "A,B,C", None))
        self.label_3.setText(_translate("create_ndfa_dialog", "Finals", None))
        self.dfa_finals.setPlaceholderText(_translate("create_ndfa_dialog", "A,B,C", None))
        self.label_4.setText(_translate("create_ndfa_dialog", "Transitions", None))
        item = self.dfa_transitions.horizontalHeaderItem(0)
        item.setText(_translate("create_ndfa_dialog", "State", None))
        item = self.dfa_transitions.horizontalHeaderItem(1)
        item.setText(_translate("create_ndfa_dialog", "Char", None))
        item = self.dfa_transitions.horizontalHeaderItem(2)
        item.setText(_translate("create_ndfa_dialog", "Next state(s)", None))
        self.add_dfa_button.setText(_translate("create_ndfa_dialog", "Add new NDFA", None))

        self.add_dfa_button.clicked.connect(self.create_ndfa)

    def create_ndfa(self):
        alphabet = self.dfa_alphabet.text().split(',')
        start = self.dfa_start.text().split(',')
        finals = self.dfa_finals.text().split(',')
        transitions = {}

        for row in range(0, self.dfa_transitions.rowCount()):
            state = self.dfa_transitions.item(row, 0)
            char = self.dfa_transitions.item(row, 1)
            next_state = self.dfa_transitions.item(row, 2)
            if state is not None and char is not None and next_state is not None:
                state = state.text()
                char = char.text()
                next_state = next_state.text().split(',')
                transitions[(state, char)] = next_state

        if alphabet[0] != '' and start != '' and finals[0] != '' and transitions != {}:
            ndfa = NDFA(alphabet, transitions, start, finals)
            ndfa_list.append(ndfa)
            item = QStandardItem(ndfa.get_tuple_string())

            ndfa_model_list.appendRow(item)
            self.dialog.accept()



