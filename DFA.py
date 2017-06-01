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

    def minimize(self):
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
