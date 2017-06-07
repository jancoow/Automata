# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import Qt

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QStandardItemModel

from Model import dfa_model_list, ndfa_model_list, ndfa_list
from Model import dfa_list
from gui.create_dfa_dialog import Ui_create_dfa_dialog
from gui.create_ndfa_dialog import Ui_create_ndfa_dialog
from gui.show_dfa_dialog import Ui_ShowDfa
from gui.show_ndfa_dialog import Ui_ShowNdfa

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

class Ui_main_frame(object):
    def setupUi(self, main_frame):
        main_frame.setObjectName(_fromUtf8("main_frame"))
        main_frame.resize(1009, 540)
        main_frame.setMinimumSize(QtCore.QSize(900, 500))
        self.mainWidget = QtGui.QWidget(main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.gridLayout = QtGui.QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.mainWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.DFA_Widget = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DFA_Widget.sizePolicy().hasHeightForWidth())
        self.DFA_Widget.setSizePolicy(sizePolicy)
        self.DFA_Widget.setAutoFillBackground(False)
        self.DFA_Widget.setStyleSheet(_fromUtf8("border-right: 1px solid gray; \n"
                                                ""))
        self.DFA_Widget.setObjectName(_fromUtf8("DFA_Widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.DFA_Widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.DFA_Widget)
        self.label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.dfa_new = QtGui.QPushButton(self.DFA_Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dfa_new.sizePolicy().hasHeightForWidth())
        self.dfa_new.setSizePolicy(sizePolicy)
        self.dfa_new.setObjectName(_fromUtf8("dfa_new"))
        self.verticalLayout_2.addWidget(self.dfa_new)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.dfa_list = QtGui.QListView(self.DFA_Widget)
        self.dfa_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.dfa_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.dfa_list.setObjectName(_fromUtf8("dfa_list"))
        self.verticalLayout_2.addWidget(self.dfa_list)
        self.label_5 = QtGui.QLabel(self.DFA_Widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.widget_2 = QtGui.QWidget(self.DFA_Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.widget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.DFA_Widget)
        self.NDFA_Widget = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NDFA_Widget.sizePolicy().hasHeightForWidth())
        self.NDFA_Widget.setSizePolicy(sizePolicy)
        self.NDFA_Widget.setStyleSheet(_fromUtf8("border-right: 1px solid gray; "))
        self.NDFA_Widget.setObjectName(_fromUtf8("NDFA_Widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.NDFA_Widget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.NDFA_Widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.ndfa_new = QtGui.QPushButton(self.NDFA_Widget)
        self.ndfa_new.setObjectName(_fromUtf8("ndfa_new"))
        self.verticalLayout_4.addWidget(self.ndfa_new)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.ndfa_list = QtGui.QListView(self.NDFA_Widget)
        self.ndfa_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ndfa_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ndfa_list.setObjectName(_fromUtf8("ndfa_list"))
        self.verticalLayout_4.addWidget(self.ndfa_list)
        self.label_2.raise_()
        self.ndfa_new.raise_()
        self.ndfa_list.raise_()
        self.horizontalLayout_2.addWidget(self.NDFA_Widget)
        self.REGEX_Widget = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.REGEX_Widget.sizePolicy().hasHeightForWidth())
        self.REGEX_Widget.setSizePolicy(sizePolicy)
        self.REGEX_Widget.setObjectName(_fromUtf8("REGEX_Widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.REGEX_Widget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.REGEX_Widget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.regex_new = QtGui.QPushButton(self.REGEX_Widget)
        self.regex_new.setObjectName(_fromUtf8("regex_new"))
        self.verticalLayout_5.addWidget(self.regex_new)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem5)
        self.regex_list = QtGui.QListView(self.REGEX_Widget)
        self.regex_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.regex_list.setObjectName(_fromUtf8("regex_list"))
        self.verticalLayout_5.addWidget(self.regex_list)
        self.label_3.raise_()
        self.regex_list.raise_()
        self.regex_new.raise_()
        self.horizontalLayout_2.addWidget(self.REGEX_Widget)
        self.Grammar_Widget = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grammar_Widget.sizePolicy().hasHeightForWidth())
        self.Grammar_Widget.setSizePolicy(sizePolicy)
        self.Grammar_Widget.setObjectName(_fromUtf8("Grammar_Widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Grammar_Widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout.addWidget(self.widget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        main_frame.setCentralWidget(self.mainWidget)

        self.retranslateUi(main_frame)
        QtCore.QMetaObject.connectSlotsByName(main_frame)

    def retranslateUi(self, main_frame):
        main_frame.setWindowTitle(_translate("main_frame", "Automata Main", None))
        self.label.setText(_translate("main_frame", "DFA", None))
        self.dfa_new.setText(_translate("main_frame", "Create new", None))
        self.dfa_new.clicked.connect(Ui_create_dfa_dialog)
        self.label_5.setText(_translate("main_frame", "Select 2 DFA ...", None))
        self.ndfa_new.clicked.connect(Ui_create_ndfa_dialog)
        self.pushButton.setText(_translate("main_frame", "AND", None))
        self.pushButton.clicked.connect(self.and_dfa)
        self.pushButton_2.setText(_translate("main_frame", "OR", None))
        self.pushButton_2.clicked.connect(self.or_dfa)

        self.label_2.setText(_translate("main_frame", "NDFA", None))
        self.ndfa_new.setText(_translate("main_frame", "Create new", None))
        self.label_3.setText(_translate("main_frame", "REGEX", None))
        self.regex_new.setText(_translate("main_frame", "Create new", None))

        self.dfa_list.setModel(dfa_model_list)
        self.dfa_list.doubleClicked.connect(self.show_dfa)
        self.ndfa_list.setModel(ndfa_model_list)
        self.ndfa_list.doubleClicked.connect(self.show_ndfa)

    def show_dfa(self, x):
        Ui_ShowDfa(dfa_list[dfa_model_list.itemFromIndex(x).row()])

    def show_ndfa(self, x):
        Ui_ShowNdfa(ndfa_list[ndfa_model_list.itemFromIndex(x).row()])

    def and_dfa(self):
        indexes = self.dfa_list.selectedIndexes()
        if len(indexes) == 2:
            dfa1 = dfa_list[dfa_model_list.itemFromIndex(indexes[0]).row()]
            dfa2 = dfa_list[dfa_model_list.itemFromIndex(indexes[1]).row()]
            dfa3 = dfa1 & dfa2
            dfa_list.append(dfa3)
            item = QStandardItem(dfa3.get_tuple_string())
            dfa_model_list.appendRow(item)

    def or_dfa(self):
        indexes = self.dfa_list.selectedIndexes()
        if len(indexes) == 2:
            dfa1 = dfa_list[dfa_model_list.itemFromIndex(indexes[0]).row()]
            dfa2 = dfa_list[dfa_model_list.itemFromIndex(indexes[1]).row()]
            dfa3 = dfa1 | dfa2
            dfa_list.append(dfa3)
            item = QStandardItem(dfa3.get_tuple_string())
            dfa_model_list.appendRow(item)









