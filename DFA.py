import itertools
import networkx as nx

from NDFA import NDFA


class DFA:
    def __init__(self, alphabet, transitions, start, finals):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def accept(self, str_input):
        """
        Accept string
        """
        state = self.start
        for char in str_input:
            state = self.accept_step(char, state)
        return state in self.finals

    def accept_step(self, char, state):
        """
        Accept start at current step
        """
        if char not in self.alphabet:
            raise ValueError("Character not in alphabet")
        if (state, char) in self.transitions:
            state = self.transitions[(state, char)]
        else:
            raise ValueError("Can't find state")
        return state

    def get_tuple_string(self):
        """
        Generate tuple string
        """
        return "{ {" + ', '.join(sorted(set([str(i[0]) for i in self.transitions]))) + "}, {" \
               + ','.join(map(str, self.alphabet)) + "}, {δ}, "\
               + str(self.start) + ", {"\
               + ','.join(map(str, self.finals))\
               + "} }"

    def reverse(self):
        """
        Reverse DFA and return NDFA
        """
        reverse_transitions = {}
        start = set()
        finals = set()
        for transition in self.transitions:
            # Check if transition already exist in dictionary, if so we need to add our new state to the current array
            if (self.transitions[transition], transition[1]) in reverse_transitions.keys():
                reverse_transitions[(self.transitions[transition], transition[1])].append(transition[0])
            else:
                reverse_transitions[(self.transitions[transition], transition[1])] = [transition[0]]
            if transition[0] not in self.start and transition[0] != '{}':
                start.add(transition[0])
            if transition[0] not in self.finals:
                finals.add(transition[0])

        return NDFA(self.alphabet, reverse_transitions, list(start), list(finals))

    def minimize_reverse(self):
        """
        Minimize DFA using the double reverse method
        """
        # Step 1: Reverse
        reversed_ndfa = self.reverse()
        # Step 2: Translate the NDFA to DFA
        reversed_dfa = reversed_ndfa.to_dfa()
        # Step 3: Reverse the DFA again
        reversed_ndfa = reversed_dfa.reverse()
        # Step 4: Translate the NDFA to DFA
        reversed_dfa = reversed_ndfa.to_dfa()

        return reversed_dfa

    def minimize_myphill(self):
        """
        Minimize DFA using the myphill (table) method
        """
        pairs = {}

        # Step 1 - create all pair of states & Step 2 - Mark state pairs
        for t1 in self.transitions:
            for t2 in self.transitions:
                # Using frozenset for removing duplicates
                combination = frozenset((t1[0], t2[0]))
                if t1[0] != t2[0]:
                    pairs[combination] = 0
                    # If one of the states in in final state we can mark them.
                    if (t1[0] in self.finals and t2[0] not in self.finals) or (
                            t1[0] not in self.finals and t2[0] in self.finals):
                        pairs[combination] = 1

        # Step 3 - Mark more state pairs until we don't find anymore states
        pairs_found = 1
        while pairs_found > 0:
            pairs_found = 0
            for pair in pairs:
                if pairs[pair] is 0:
                    for char in self.alphabet:
                        new_pair = set()
                        for s in pair:
                            new_pair.add(self.transitions[(s, char)])
                        new_pair = frozenset(new_pair)
                        if new_pair in pairs and pairs[new_pair] == 1:
                            pairs[pair] = 1
                            pairs_found += 1
                            break

        # Step 4 - Combine the pairs into the new states
        new_states = []
        for pair in pairs:
            if pairs[pair] is 0:
                is_added = False
                for new_state in new_states:
                    if len(pair.intersection(new_state)) > 0:
                        new_state.update(pair)

                        is_added = True
                        break
                if not is_added:
                    new_states.append(set(pair))

        # If there are no new states created, then we can't minimize it and return the current object
        if len(new_states) == 0:
            return self

        # Step 5 - Creating new dfa
        transitions = {}
        finals = []
        start = 0

        for new_state in new_states:
            for char in self.alphabet:
                next_state = self.transitions[(next(iter(new_state)), char)]

                state_found = False
                for s in new_states:
                    if next_state in s:
                        next_state = s
                        state_found = True
                        break

                if not state_found:
                    new_states.append({next_state})
                    next_state = {next_state}

                transitions[(','.join(sorted(new_state)), char)] = ','.join(sorted(next_state))

            # Check if state is a final state
            if len(new_state.intersection(self.finals)) > 0:
                finals.append(','.join(sorted(new_state)))

            # Check if the state is a start state
            if self.start in new_state:
                start = ','.join(sorted(new_state))

        return DFA(self.alphabet, transitions, start, finals)

    def _merge(self, other, merge_type):
        """
        Merge two DFA (only used by or / and operations)
        """
        start = 0
        finals = []
        transitions = {}

        # combined the alphabet
        alphabet = self.alphabet + [i for i in other.alphabet if i not in self.alphabet]

        for nda_1_state in self.transitions:
            for nda_2_state in other.transitions:
                if nda_2_state[1] == nda_1_state[1]:
                    new_state = nda_1_state[0] + "," + nda_2_state[0]
                    transitions[(new_state, nda_1_state[1])] = self.transitions[nda_1_state] + "," + other.transitions[nda_2_state]

                    # If both states are the start state
                    if nda_1_state[0] == self.start and nda_2_state[0] == other.start:
                        start = new_state

                    if merge_type is "and":
                        # If both states are the final state
                        if nda_1_state[0] in self.finals and nda_2_state[0] in other.finals and new_state not in finals:
                            finals.append(new_state)
                    elif merge_type is "or":
                        # If one of the states is the final state
                        if(nda_1_state[0] in self.finals or nda_2_state[0] in other.finals) and new_state not in finals:
                            finals.append(new_state)

        return DFA(alphabet, transitions, start, finals)

    def __and__(self, other):
        if type(other) is not DFA:
            return NotImplemented
        return self._merge(other, "and")

    def __or__(self, other):
        if type(other) is not DFA:
            return NotImplemented
        return self._merge(other, "or")

    def not_operation(self):
        finals = set()
        for s in self.transitions:
            if s[0] not in self.finals:
                finals.add(s[0])
        return DFA(self.alphabet, self.transitions, self.start, finals)

    def generate_words(self, length=5):
        """
        Generate a list of words which are accepted and not accepted
        """
        accepted = []
        not_accepted = []
        for i in range(1, length):
            for combination in list(itertools.product(['a', 'b'], repeat=i)):
                str_combination = ''.join(combination)
                try:
                    if self.accept(combination):
                        accepted.append(str_combination)
                    else:
                        not_accepted.append(str_combination)
                except ValueError:
                    return [], []
        return accepted, not_accepted

    def get_graph(self, name="output", current_state=None):
        """
        Generate a graphviz graph.
        Name = Output file name
        current_states = If using in step mode, the current state will be colored red
        """
        graph = nx.DiGraph()
        for key, value in self.transitions.items():
            label = key[1]

            # If this state transition already exist we should combine the label.
            if graph.get_edge_data(key[0], value):
                label += "," + graph.get_edge_data(key[0], value)["label"]

            # If this state is an end state
            if key[0] in self.finals:
                graph.add_node(key[0], shape="doublecircle")
            if value in self.finals:
                graph.add_node(value, shape="doublecircle")

            # Color current state
            if current_state == key[0]:
                graph.add_node(key[0], color="Red")

            graph.add_edge(key[0], value, label=label)

        # Add start arrow
        graph.add_node(' ', shape="point")
        graph.add_edge(' ', self.start)

        # trick for labeling
        for u, v, d in graph.edges(data=True):
            d['label'] = d.get('label', '')

        png = nx.nx_agraph.to_agraph(graph)
        png.layout(prog='dot')
        png.draw('output/' + name + '.png')

    @staticmethod
    def dfa_begins_with(begin, alphabet):
        """
        Generate dfa which begins with
        """
        transitions = {}

        for i, char in enumerate(begin):
            transitions[(i, char)] = i + 1
            for a in alphabet:  # For other chars in alphabet add transition to fuik
                if a is not char:
                    transitions[(i, a)] = '{}'

        for char in alphabet:
            transitions[('{}', char)] = '{}'
            transitions[(len(begin), char)] = len(begin)

        return DFA(alphabet, transitions, 0, [len(begin)])

    @staticmethod
    def dfa_ends_with(end, alphabet):
        """
        Generate dfa which ends with
        """

        transitions = {}

        endstate = 0

        startchar = ''
        startcharEnabled = True

        for i, char in enumerate(end):

            if startchar is '':
                startchar = char

            transitions[(i, char)] = i + 1
            for a in alphabet:
                if a is not char:
                    if startchar is not char and startcharEnabled:
                        transitions[(i, a)] = i
                        startcharEnabled = False
                    else:
                        transitions[(i, a)] = 0
            endstate = i + 1

        for char in alphabet:
            transitions[(endstate, char)] = 0

        print(transitions)

        return DFA(alphabet, transitions, 0, [endstate])

    @staticmethod
    def dfa_contains(contains, alphabet):
        """
        Generate dfa which contains
        """

        transitions = {}

        endstate = 0

        startchar = ''
        startcharEnabled = True

        for i, char in enumerate(contains):

            if startchar is '':
                startchar = char

            transitions[(i, char)] = i + 1
            for a in alphabet:
                if a is not char:
                    if startchar is not char and startcharEnabled:
                        transitions[(i, a)] = i
                        startcharEnabled = False
                    else:
                        transitions[(i, a)] = 0
            endstate = i + 1

        for char in alphabet:
            transitions[(endstate, char)] = endstate

        print(transitions)

        return DFA(alphabet, transitions, 0, [endstate])




