from PyQt4.QtGui import QStandardItem
from PyQt4 import QtGui

from DFA import DFA
from Model import dfa_list, dfa_model_list, ndfa_list, ndfa_model_list, regex_model_list
from NDFA import NDFA
from Regex import Regex
from gui import main_frame


def launch_gui():
    import sys
    app = QtGui.QApplication(sys.argv)
    frame = QtGui.QMainWindow()
    ui = main_frame.Ui_main_frame()
    ui.setupUi(frame)
    frame.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # ----------------------------- #
    # Example 1 #
    # Simple DFA #
    # Ends with 'bab'
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('q0', 'a'): 'q0',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q1',
        ('q2', 'a'): 'q0',
        ('q2', 'b'): 'q3',
        ('q3', 'a'): 'q2',
        ('q3', 'b'): 'q1',
    }

    start = 'q0'
    finals = ['q3']

    dfa = DFA(alphabet, transitions, start, finals)
    dfa_list.append(dfa)
    dfa_model_list.appendRow(QStandardItem(dfa.get_tuple_string()))

    # ----------------------------- #
    # Example 2 #
    # Simple DFA #
    # "Starts with 'ba'"
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('q0', 'a'): '{}',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): '{}',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
        ('{}', 'a'): '{}',
        ('{}', 'b'): '{}',
    }

    start = 'q0'
    finals = ['q2']

    dfa = DFA(alphabet, transitions, start, finals)
    dfa_list.append(dfa)
    dfa_model_list.appendRow(QStandardItem(dfa.get_tuple_string()))

    # ----------------------------- #
    # Example 3 #
    # Simple DFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q4',
        ('q1', 'a'): 'q4',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q4',
        ('q3', 'a'): 'q1',
        ('q3', 'b'): 'q2',
        ('q4', 'a'): 'q4',
        ('q4', 'b'): 'q4',
    }

    start = 'q0'
    finals = ['q2', 'q3']

    dfa = DFA(alphabet, transitions, start, finals)
    dfa_list.append(dfa)
    dfa_model_list.appendRow(QStandardItem(dfa.get_tuple_string()))

    # ----------------------------- #
    # Example 4 #
    # Simple NDFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('q0', 'a'): ['q0', 'q1'],
        ('q0', 'b'): ['q0', 'q3'],
        ('q1', 'b'): ['q2'],
        ('q3', 'a'): ['q4'],
        ('q2', 'b'): ['q4'],
        ('q4', 'a'): ['q4'],
        ('q4', 'b'): ['q4']
    }
    start = ['q0']
    finals = ['q4']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))

    # ----------------------------- #
    # Example 5 #
    # NDFA with multiple epsilons #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('0', 'a'): ['1'],
        ('2', '$'): ['0', '3'],
        ('3', 'b'): ['4'],
        ('4', '$'): ['5'],
        ('3', '$'): ['5'],
        ('5', 'a'): ['6']
    }
    start = ['2']
    finals = ['6',   '1']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))

    # ----------------------------- #
    # Example 6 #
    # NDFA      #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('A', 'a'): ['A', 'B', 'C', 'D', 'E'],
        ('A', 'b'): ['D', 'E'],
        ('B', 'a'): ['C'],
        ('B', 'b'): ['E'],
        ('C', 'b'): ['B'],
        ('D', 'a'): ['E'],
    }
    start = ['A']
    finals = ['C']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))

    regex = "abb.ab|b"
    regex_model_list.appendRow(QStandardItem(regex))
    regex = "(a|b)*(b+b|ab*baa)(ab+aa|bb+)*"
    regex_model_list.appendRow(QStandardItem(regex))
    regex = "(a|b)*"
    regex_model_list.appendRow(QStandardItem(regex))

    launch_gui()
