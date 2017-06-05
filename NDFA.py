#import networkx as nx

class NDFA:
    def __init__(self, alphabet, transitions, start, finals):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def accept(self, str_input):
        states = {self.start}
        for char in str_input:
            if char not in self.alphabet:
                raise ValueError("Character not in alphabet")
            new_states = set()
            for i, state in enumerate(states):
                if (state, '$') in self.transitions:
                    new_states |= set(self.transitions[(state, '$')])
                if (state, char) in self.transitions:
                    new_states |= set(self.transitions[(state, char)])
            states = new_states

        return not states.isdisjoint(self.finals)

    def get_graph(self, name="output"):
        graph = nx.DiGraph()
        for key, value in self.transitions.items():
            for t in value:
                label = key[1]

                # If this state transition already exist we should combine the label.
                if graph.get_edge_data(key[0], t):
                    label += "," + graph.get_edge_data(key[0], t)["label"]

                # If this state is an end state
                if key[0] in self.finals:
                    graph.add_node(key[0], shape="doublecircle")

                graph.add_edge(key[0], t, label=label)

        # trick for labeling
        for u, v, d in graph.edges(data=True):
            d['label'] = d.get('label', '')

        png = nx.nx_agraph.to_agraph(graph)
        png.layout(prog='dot')
        png.draw(name + '.png')

    def __or__(self, other):
        if type(other) is not NDFA:
            return NotImplemented

        # combined the alphabet
        alphabet = self.alphabet + [i for i in other.alphabet if i not in other.alphabet]
        start = 0

        # We need to combine the transitions but we can't have duplicate states,
        # so we need to modify all the state numbers
        transitions = {}

        # Add +1 for each state so we can create a new start state
        last_state = 1
        for key, value in self.transitions.items():
            last_state = (key[0] + 1) if not (key[0] + 1) < last_state else last_state
            transitions[(key[0] + 1, key[1])] = [v + 1 for v in value]
        finals = [f + 1 for f in self.finals]

        # Add +n (max from this) so we don't create duplicate states
        for key, value in other.transitions.items():
            transitions[(key[0] + last_state + 1, key[1])] = [v + last_state + 1 for v in value]
        finals += [f + last_state + 1 for f in other.finals]

        # Add new start state with epsilon to other start states
        transitions[(0, '$')] = [self.start + 1, other.start + last_state + 1]

        ndfa = NDFA(alphabet, transitions, start, finals)
        return ndfa
