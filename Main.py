from PyQt4.QtGui import QStandardItem
from PyQt4 import QtGui

from DFA import DFA
from Model import dfa_list, dfa_model_list, ndfa_list, ndfa_model_list
from NDFA import NDFA
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
    # Example 2 #
    # Simple NDFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {(0, 'a'): [1], (1, 'a'): [2], (3, '$'): [0, 4], (4, 'b'): [5], (6, '$'): [3], (5, '$'): [7, 3], (7, 'a'): [8], (8, '$'): [9], (9, 'b'): [10], (10, 'b'): [11]}
    start = [0]
    finals = [0]

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa.get_graph("remcotest")


    # # REGEX TEST
    # regex = 'a(a|b)*'
    # symbols = {'(': 'BRACKET_OPEN',
    #                 ')': 'BRACKET_CLOSE',
    #                 '*': 'STAR',
    #                 '|': 'OR',
    #                 '.': 'DOT',
    #                 '+': 'PLUS'}
    # chars = []
    #
    # def parse_chars():
    #     for c in regex:
    #         if c not in symbols.keys():  # It's not a symbol so it's a char
    #             chars.append(('CHAR', c))
    #         else:
    #             chars.append((symbols[c], c))
    #
    # def parse_tokens():
    #     parse_chars()
    #     current_char_index = 0
    #
    #     def get_current_char():
    #         pass
    #
    #
    #     def parse_token(char):
    #         if char[0] is 'OR':
    #             cur_char = char
    #
    #     for index, key in enumerate(chars):
    #         parse_token(c)
    #
    #
    #
    #
    # parse_tokens()
    # exit()

    # ----------------------------- #
    # Example 1 #
    # Simple DFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('A', 'a'): 'A',
        ('A', 'b'): 'B',
        ('B', 'a'): 'B',
        ('B', 'b'): 'B',
    }

    start = 'A'
    finals = ['B']

    dfa = DFA(alphabet, transitions, start, finals)

    dfa_list.append(dfa)
    dfa_model_list.appendRow(QStandardItem(dfa.get_tuple_string()))

    # ----------------------------- #
    # Example 2 #
    # Simple NDFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('A', 'a'): ['A'],
        ('A', 'b'): ['C'],
        ('A', '$'): ['B'],
        ('C', 'b'): ['B', 'C']
    }
    start = ['A']
    finals = ['B']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))
    ndfa.get_graph("ndfa")

    # ----------------------------- #
    # Example 2 #
    # Complex NDFA with Epselon#
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('0', 'a'): ['1'],
        ('1', 'a'): ['2'],
        ('3', '$'): ['0', '4'],
        ('4', 'b'): ['5'],
        ('6', '$'): ['3'],
        ('5', '$'): ['7', '3'],
        ('7', 'a'): ['8'],
        ('8', '$'): ['9'],
        ('9', 'b'): ['10'],
        ('10', 'b'): ['11'],
        ('12', '$'): ['6'],
        ('11', '$'): ['13', '6'],
        ('13', 'a'): ['14'],
        ('15', '$'): ['12', '16'],
        ('16', 'b'): ['17'],
        ('17', 'b'): ['18'],
        ('18', 'b'): ['19'],
        ('20', '$'): ['15'],
        ('19', '$'): ['21', '15']}
    start = ['3']
    finals = ['19']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))
    ndfa.get_graph("ndfa")

    # ----------------------------- #
    # Example 3 #
    # DFA AND
    # Combining 2 DFA with an AND   #
    # ----------------------------- #
    alphabet = ['a', 'b']

    transitions_dfa_1 = {
        ('1', 'a'): '2',
        ('1', 'b'): '1',
        ('2', 'a'): '1',
        ('2', 'b'): '2',
    }
    start_dfa_1 = '1'
    finals_dfa_1 = ['1']

    transitions_dfa_2 = {
        ('1', 'a'): '1',
        ('1', 'b'): '2',
        ('2', 'a'): '1',
        ('2', 'b'): '3',
        ('3', 'a'): '1',
        ('3', 'b'): '4',
        ('4', 'a'): '4',
        ('4', 'b'): '4',
    }
    start_dfa_2 = '1'
    finals_dfa_2 = ['1', '2']

    dfa1 = DFA(alphabet, transitions_dfa_1, start_dfa_1, finals_dfa_1)
    dfa2 = DFA(alphabet, transitions_dfa_2, start_dfa_2, finals_dfa_2)

    dfa3 = dfa1 | dfa2

    dfa1.get_graph("dfa-1")
    dfa2.get_graph("dfa-2")
    dfa3.get_graph("dfa-3")

    dfa_list.append(dfa1)
    dfa_model_list.appendRow(QStandardItem(dfa1.get_tuple_string()))
    dfa_list.append(dfa2)
    dfa_model_list.appendRow(QStandardItem(dfa2.get_tuple_string()))
    dfa_list.append(dfa3)
    dfa_model_list.appendRow(QStandardItem(dfa3.get_tuple_string()))

    # ----------------------------- #
    # Example 4 #
    # DFA minimisation
    # DFA minimisation using  Myphill-Nerode Theorem  #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('A', 'a'): 'B',
        ('A', 'b'): 'C',
        ('B', 'a'): 'A',
        ('B', 'b'): 'D',
        ('C', 'a'): 'E',
        ('C', 'b'): 'F',
        ('D', 'a'): 'E',
        ('D', 'b'): 'F',
        ('E', 'a'): 'E',
        ('E', 'b'): 'F',
        ('F', 'a'): 'F',
        ('F', 'b'): 'F',

    }

    start = 'A'
    finals = ['C', 'D', 'E']

    dfa = DFA(alphabet, transitions, start, finals)
    dfa.get_graph("dfa-before")
    minimized_dfa = dfa.minimize_myphill()

    dfa_list.append(dfa)
    dfa_model_list.appendRow(QStandardItem(dfa.get_tuple_string()))

    minimized_dfa.get_graph("dfa-after")
    dfa_list.append(minimized_dfa)
    dfa_model_list.appendRow(QStandardItem(minimized_dfa.get_tuple_string()))

    # ----------------------------- #
    # Example 5 #
    # NDFA to DFA #
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
    finals = ['E']

    ndfa = NDFA(alphabet, transitions, start, finals)
    ndfa.get_graph("ndfa-to-dfa-1")
    ndfa_list.append(ndfa)
    ndfa_model_list.appendRow(QStandardItem(ndfa.get_tuple_string()))

    dfa = ndfa.to_dfa()
    dfa.get_graph("ndfa-to-dfa-2")

    # ----------------------------- #
    # Example 6 #
    # Minimisation with reverse #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('Q0', 'a'): "Q1",
        ('Q0', 'b'): "Q2",
        ('Q1', 'a'): "Q0",
        ('Q1', 'b'): "Q1",
        ('Q2', 'a'): "Q0",
        ('Q2', 'b'): "Q2",
    }
    start = 'Q0'
    finals = ['Q1', 'Q2']

    dfa = DFA(alphabet, transitions, start, finals)
    dfa.minimize_reverse()

    # ----------------------------- #
    # Example 2 #
    # Simple NDFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        ('0', 'a'): ['0', '1'],
        ('1', 'b'): ['0'],
        ('2', 'a'): ['2'],
        ('1', 'b'): ['1'],
        ('0', '$'): ['1'],
    }
    start = [0]
    finals = [0]

    ndfa = NDFA(alphabet, transitions, start, finals)

    # Launch the QT gui
    launch_gui()
