# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dfa_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItem

from DFA import DFA
from Model import dfa_model_list
from Model import dfa_list
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


class Ui_create_dfa_dialog(object):
    def __init__(self):
        self.dialog = QtGui.QDialog()
        self.setupUi(self.dialog)
        self.dialog.exec()

    def setupUi(self, create_dfa_dialog):
        create_dfa_dialog.setObjectName(_fromUtf8("create_dfa_dialog"))
        create_dfa_dialog.setWindowModality(QtCore.Qt.WindowModal)
        create_dfa_dialog.resize(785, 535)
        create_dfa_dialog.setMinimumSize(QtCore.QSize(600, 300))
        create_dfa_dialog.setSizeGripEnabled(False)
        create_dfa_dialog.setModal(True)
        self.formLayout = QtGui.QFormLayout(create_dfa_dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(create_dfa_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.dfa_alphabet = QtGui.QLineEdit(create_dfa_dialog)
        self.dfa_alphabet.setToolTip(_fromUtf8(""))
        self.dfa_alphabet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dfa_alphabet.setObjectName(_fromUtf8("dfa_alphabet"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dfa_alphabet)
        self.label_2 = QtGui.QLabel(create_dfa_dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dfa_start = QtGui.QLineEdit(create_dfa_dialog)
        self.dfa_start.setObjectName(_fromUtf8("dfa_start"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dfa_start)
        self.label_3 = QtGui.QLabel(create_dfa_dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dfa_finals = QtGui.QLineEdit(create_dfa_dialog)
        self.dfa_finals.setObjectName(_fromUtf8("dfa_finals"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dfa_finals)
        self.label_4 = QtGui.QLabel(create_dfa_dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dfa_transitions = QtGui.QTableWidget(create_dfa_dialog)
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
        self.add_dfa_button = QtGui.QPushButton(create_dfa_dialog)
        self.add_dfa_button.setObjectName(_fromUtf8("add_dfa_button"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.add_dfa_button)
        self.line = QtGui.QFrame(create_dfa_dialog)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.line)
        self.label_5 = QtGui.QLabel(create_dfa_dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.widget = QtGui.QWidget(create_dfa_dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.widget)
        self.label_6 = QtGui.QLabel(create_dfa_dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.widget_2 = QtGui.QWidget(create_dfa_dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtGui.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.widget_2)
        self.label_7 = QtGui.QLabel(create_dfa_dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.widget_3 = QtGui.QWidget(create_dfa_dialog)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtGui.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.widget_3)

        self.retranslateUi(create_dfa_dialog)
        QtCore.QMetaObject.connectSlotsByName(create_dfa_dialog)

    def retranslateUi(self, create_dfa_dialog):
        create_dfa_dialog.setWindowTitle(_translate("create_dfa_dialog", "Dialog", None))
        self.label.setText(_translate("create_dfa_dialog", "Alphabet", None))
        self.dfa_alphabet.setPlaceholderText(_translate("create_dfa_dialog", "a,b,c", None))
        self.label_2.setText(_translate("create_dfa_dialog", "Start", None))
        self.dfa_start.setPlaceholderText(_translate("create_dfa_dialog", "A", None))
        self.label_3.setText(_translate("create_dfa_dialog", "Finals", None))
        self.dfa_finals.setPlaceholderText(_translate("create_dfa_dialog", "A,B,C", None))
        self.label_4.setText(_translate("create_dfa_dialog", "Transitions", None))
        item = self.dfa_transitions.horizontalHeaderItem(0)
        item.setText(_translate("create_dfa_dialog", "State", None))
        item = self.dfa_transitions.horizontalHeaderItem(1)
        item.setText(_translate("create_dfa_dialog", "Char", None))
        item = self.dfa_transitions.horizontalHeaderItem(2)
        item.setText(_translate("create_dfa_dialog", "Next state(s)", None))
        self.add_dfa_button.setText(_translate("create_dfa_dialog", "Add new DFA", None))
        self.label_5.setText(_translate("create_dfa_dialog", "Begins with", None))
        self.pushButton.setText(_translate("create_dfa_dialog", "Generate", None))
        self.label_6.setText(_translate("create_dfa_dialog", "Ends with", None))
        self.pushButton_2.setText(_translate("create_dfa_dialog", "Generate", None))
        self.label_7.setText(_translate("create_dfa_dialog", "Contains", None))
        self.pushButton_3.setText(_translate("create_dfa_dialog", "Generate", None))

        self.add_dfa_button.clicked.connect(self.create_dfa)
        self.pushButton.clicked.connect(self.generate_begins_with)

    def generate_begins_with(self):
        alphabet = self.dfa_alphabet.text().split(',')
        if alphabet[0] != '' and self.lineEdit.text() != '':
            dfa = DFA.dfa_begins_with(self.lineEdit.text(), alphabet)
            dfa_list.append(dfa)
            item = QStandardItem(dfa.get_tuple_string())
            dfa_model_list.appendRow(item)
            self.dialog.accept()

    def create_dfa(self):
        alphabet = self.dfa_alphabet.text().split(',')
        start = self.dfa_start.text()
        finals = self.dfa_finals.text().split(',')
        transitions = {}

        for row in range(0, self.dfa_transitions.rowCount()):
            state = self.dfa_transitions.item(row, 0)
            char = self.dfa_transitions.item(row, 1)
            next_state = self.dfa_transitions.item(row, 2)
            if state is not None and char is not None and next_state is not None:
                state = state.text()
                char = char.text()
                next_state = next_state.text()
                transitions[(state, char)] = next_state

        if alphabet[0] != '' and start != '' and finals[0] != '' and transitions != {}:
            dfa = DFA(alphabet, transitions, start, finals)
            dfa_list.append(dfa)
            item = QStandardItem(dfa.get_tuple_string())

            dfa_model_list.appendRow(item)
            self.dialog.accept()



