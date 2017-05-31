import networkx as nx


class DFA:
    def __init__(self, alphabet, transitions, start, finals):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def accept(self, str_input):
        state = self.start
        for char in str_input:
            if char not in self.alphabet:
                raise ValueError("Character not in alphabet")
            state = self.transitions[(state, char)]
        return state in self.finals

    def get_graph(self, name="output"):
        graph = nx.DiGraph()
        for key, value in self.transitions.items():
            label = key[1]

            # If this state transition already exist we should combine the label.
            if graph.get_edge_data(key[0], value):
                label += "," + graph.get_edge_data(key[0], value)["label"]

            # If this state is an end state
            if key[0] in self.finals:
                graph.add_node(key[0], shape="doublecircle")

            graph.add_edge(key[0], value, label=label)

        # Add start arrow
        graph.add_node(' ', shape="point")
        graph.add_edge(' ', self.start)

        # trick for labeling
        for u, v, d in graph.edges(data=True):
            d['label'] = d.get('label', '')

        png = nx.nx_agraph.to_agraph(graph)
        png.layout(prog='dot')
        png.draw(name + '.png')

    def __and__(self, other):
        if type(other) is not DFA:
            return NotImplemented

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

                    # If both states are the final state
                    if nda_1_state[0] in self.finals and nda_2_state[0] in other.finals and new_state not in finals:
                        finals.append(new_state)

        return DFA(alphabet, transitions, start, finals)

    def __or__(self, other):
        if type(other) is not DFA:
            return NotImplemented

        start = 0
        finals = []
        transitions = {}

        # combined the alphabet
        alphabet = self.alphabet + [i for i in other.alphabet if i not in self.alphabet]

        for nda_1_state in self.transitions:
            for nda_2_state in other.transitions:
                if nda_2_state[1] == nda_1_state[1]: # Only continue if Nda1 state alphabet is equal as ours
                    new_state = nda_1_state[0] + "," + nda_2_state[0]
                    transitions[(new_state, nda_1_state[1])] = self.transitions[nda_1_state] + "," + other.transitions[nda_2_state]

                    # If both states are the start state
                    if nda_1_state[0] == self.start and nda_2_state[0] == other.start:
                        start = new_state

                    # If one of the states is the final state
                    if (nda_1_state[0] in self.finals or nda_2_state[0] in other.finals) and new_state not in finals:
                        finals.append(new_state)

        return DFA(alphabet, transitions, start, finals)
