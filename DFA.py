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
            graph.add_edge(key[0], value, label=label)

        # trick for labeling
        for u, v, d in graph.edges(data=True):
            d['label'] = d.get('label', '')

        png = nx.nx_agraph.to_agraph(graph)
        png.layout(prog='dot')
        png.draw(name + '.png')

    def __and__(self, other):
        if type(other) is not DFA:
            return NotImplemented

        # combined the alphabet
        alphabet = self.alphabet + [i for i in other.alphabet if i not in self.alphabet]
        start = 0

        # We need to combine the transitions but we can't have duplicate states,
        # so we need to modify all the state numbers
        # transitions = {}

        transitions = []

        start = (self.start, other.start)
        transitions.append(start)

        transitions.append(   (self.transitions[(, 'a')], other.transitions[('1', 'a')]   )



        for nda_1_state in self.transitions:
            for nda_2_state in other.transitions:
                print(nda_1_state[0] + "," + nda_2_state[0] + "  --  " + nda_1_state[1] + " deze letter moet naar.. ")
                print(self.transitions[nda_1_state] + "-" + other.transitions[nda_2_state])
                print()
                pass


