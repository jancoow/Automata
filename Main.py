from DFA import DFA
from NDFA import NDFA

if __name__ == "__main__":
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
    print(dfa.accept("aa"))
#    dfa.get_graph("dfa")

    # ----------------------------- #
    # Example 2 #
    # Simple NDFA #
    # ----------------------------- #
    alphabet = ['a', 'b']
    transitions = {
        (0, 'a'): [0, 1],
        (1, 'b'): [0],
        (2, 'a'): [2],
        (1, 'b'): [1],
        (0, '$'): [1],
    }
    start = 0
    finals = [0]

    ndfa = NDFA(alphabet, transitions, start, finals)
    print(ndfa.accept("aba"))
 #   ndfa.get_graph("ndfa")

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

#    dfa1.get_graph("dfa-1")
#    dfa2.get_graph("dfa-2")
#    dfa3.get_graph("dfa-3")

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
#    dfa.get_graph("dfa-before")
    minimized_dfa = dfa.minimize()

#    minimized_dfa.get_graph("test")



    # ----------------------------- #
    # Example 3 #
    # NDFA OR
    # Combining 2 NDFA with an OR  #
    # ----------------------------- #
    # alphabet = ['a', 'b']
    #
    # transitions_1 = {
    #     (0, 'a'): [0, 1],
    #     (0, 'b'): [0],
    #     (1, 'a'): [1],
    # }
    # start_1 = 0
    # finals_1 = [0]
    # ndfa_1 = NDFA(alphabet, transitions_1, start_1, finals_1)
    # ndfa_1.get_graph("ndfa-1")
    #
    # transitions_2 = {
    #     (0, 'a'): [0, 1],
    #     (1, 'b'): [0],
    #     (1, 'b'): [1],
    # }
    # stff iart_2 = 0
    # finals_2 = [1]
    # ndfa_2 = NDFA(alphabet, transitions_2, start_2, finals_2)
    # ndfa_2.get_graph("ndfa-2")
    #
    # ndfa_3 = ndfa_1 | ndfa_2
    # print(ndfa_3.transitions)
    # ndfa_3.get_graph("ndfa-3")





