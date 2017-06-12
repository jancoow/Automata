from NDFA import NDFA


class Regex:
    def __init__(self, regex):
        self.regex = regex
        self.symbols = {'(': 'Haakje open',
                        ')': 'Haakje sluiten',
                        '*': 'STAR',
                        '|': 'OR',
                        '.': 'DOT',
                        '+': 'PLUS'}
        self.tokens = []

        self.parse_tokens()

    def parse_tokens(self):
        for c in self.regex:
            if c not in self.symbols.keys(): # It's not a symbol so it's a char
                self.tokens.append(('CHAR', c))
            else:
                self.tokens.append((self.symbols[c], c))
        print(self.tokens)

    def OR(self):

        pass

    def DOT(self):
        pass

    def STAR(self):
        pass

    def PLUS(self):
        pass

    def check_language(self, language):
        pass

    def to_ndfa(self):
        alphabet = set()
        for token in self.tokens:
            if token[0] is 'CHAR':
                alphabet.add(token[1])
        alphabet = sorted(alphabet)

        start = 0

        finals = [0]

        transitions = {}

        ndfa = NDFA(alphabet, transitions, start, finals)

        for token in self.tokens:
            if token[0] is "OR":
                self.OR()
                temptransitions = {
                    (ndfa.finals[0] + 1, '$') : [ndfa.start, ndfa.finals[0] + 2]
                }
                ndfa.transitions.update(temptransitions)
                ndfa = NDFA(alphabet, ndfa.transitions, ndfa.finals[0] + 1, [ndfa.finals[0] + 2])

            elif token[0] is "STAR":
                self.STAR()
                temptransitions = {
                    (ndfa.finals[0] + 1, '$'): [ndfa.start],
                    (ndfa.finals[0], '$'): [ndfa.finals[0] + 2, ndfa.start],
                    (ndfa.start, '$'): [ndfa.finals[0] + 2]
                }

                for temp_transition in temptransitions:
                    if temp_transition in ndfa.transitions.keys():
                        ndfa.transitions[temp_transition].extend(temptransitions[temp_transition])
                    else:
                        ndfa.transitions[temp_transition] = temptransitions[temp_transition]

                ndfa = NDFA(alphabet, ndfa.transitions, ndfa.finals[0] + 1, [ndfa.finals[0] + 2])

            elif token[0] is "DOT":
                temptransitions = {(ndfa.finals[0], '$') : [ndfa.finals[0] + 1]}
                for temp_transition in temptransitions:
                    if temp_transition in ndfa.transitions.keys():
                        ndfa.transitions[temp_transition].extend(temptransitions[temp_transition])
                    else:
                        ndfa.transitions[temp_transition] = temptransitions[temp_transition]

                ndfa = NDFA(alphabet, ndfa.transitions, ndfa.start, [ndfa.finals[0] + 1])
                self.DOT()
            elif token[0] is "PLUS":
                self.PLUS()
                temptransitions = {
                    (ndfa.finals[0] + 1, '$') : [ndfa.start],
                    (ndfa.finals[0], '$') : [ndfa.finals[0] + 2, ndfa.start]
                }
                for temp_transition in temptransitions:
                    if temp_transition in ndfa.transitions.keys():
                        ndfa.transitions[temp_transition].extend(temptransitions[temp_transition])
                    else:
                        ndfa.transitions[temp_transition] = temptransitions[temp_transition]

                ndfa = NDFA(alphabet, ndfa.transitions, ndfa.finals[0] + 1, [ndfa.finals[0] + 2])
            elif token[0] is "CHAR":
                temptransitions = {(ndfa.finals[0], token[1]) : [ndfa.finals[0] + 1]}

                for temp_transition in temptransitions:
                    if temp_transition in ndfa.transitions.keys():
                        ndfa.transitions[temp_transition].extend(temptransitions[temp_transition])
                    else:
                        ndfa.transitions[temp_transition] = temptransitions[temp_transition]

                ndfa = NDFA(alphabet, ndfa.transitions, ndfa.start, [ndfa.finals[0] + 1])
        #transitions = {
            # (0, 'a'): [0, 1],
            # (1, 'b'): [0],
            # (2, 'a'): [2],
            # (1, 'b'): [1],
            # (0, '$'): [1],
        #}
        #int to str conversion
        new_transitions = {}
        for t in ndfa.transitions:
            new_transitions[(str(t[0]), t[1])] = [str(i) for i in ndfa.transitions[t]]
        ndfa.finals = [str(i) for i in ndfa.finals]
        ndfa = NDFA(ndfa.alphabet, new_transitions, [str(ndfa.start)], ndfa.finals)
        return ndfa



