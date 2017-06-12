import itertools
import networkx as nx


class NDFA:
    def __init__(self, alphabet, transitions, start, finals):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def accept(self, str_input):
        """
        Accept string
        """
        states = list(self.start)
        for char in str_input:
            states = self.accept_step(char, states)
        return set(states).intersection(self.finals)  # Check if one of the states are in final state

    def accept_step(self, char, states):
        """
        Accept start at current step
        """
        if char not in self.alphabet:
            raise ValueError("Character not in alphabet")
        new_states = set()
        for i, state in enumerate(states):
            if (state, '$') in self.transitions:  # Epsilon found, so we add a new state and check it later in the loop.
                states.extend(self.transitions[(state, '$')])
            if (state, char) in self.transitions:  # Normal transition
                new_states |= set(self.transitions[(state, char)])
            else:  # There is no transition found, so we are staying in our current state
                new_states |= set(state)
        return list(new_states)

    def get_tuple_string(self):
        """
        Generate tuple string
        """
        return "{ {" + ', '.join(sorted(set([str(i[0]) for i in self.transitions]))) + "}, {" \
               + ','.join(map(str, self.alphabet)) + "}, {δ}, {"\
               + ','.join(map(str, self.start)) + "}, {"\
               + ','.join(map(str, self.finals))\
               + "} }"

    def to_dfa(self):
        """
        Translate this ndfa to dfa
        """
        from DFA import DFA

        dfa_transitions = {}
        final_states = set()
        start_state = ','.join(sorted(self.start))

        def create_new_state(states):
            name = ','.join(sorted(states))
            for s in states:
                for char in self.alphabet:
                    # Merge all the outputs from individual states in a set
                    if (s, char) in self.transitions:
                        if (name, char) in dfa_transitions:
                            if type(dfa_transitions[(name, char)]) != set:
                                dfa_transitions[(name, char)] = set(dfa_transitions[(name, char)].split(','))
                            dfa_transitions[(name, char)] |= set(self.transitions[(s, char)])
                        else:
                            dfa_transitions[(name, char)] = set(self.transitions[(s, char)])

            # Change set array to a string name
            for char in self.alphabet:
                if (name, char) in dfa_transitions:
                    new_state_name = ','.join(sorted(dfa_transitions[(name, char)]))

                    # If the state name doesn't exist yet we need to create it
                    if not any(i[0] == new_state_name for i in dfa_transitions):
                        create_new_state(dfa_transitions[(name, char)])
                    # Check if this state could be a final state
                    if len(dfa_transitions[(name, char)].intersection(self.finals)) > 0:
                        final_states.add(new_state_name)

                    dfa_transitions[(name, char)] = new_state_name

        # Generate the new states
        for transition in self.transitions:
            next_state = self.transitions[transition]
            if len(next_state) > 1:  # New state detected
                create_new_state(next_state)
            # Check if this state could be a final state
            if len(set(next_state).intersection(self.finals)) > 0:
                final_states.add(','.join(sorted(next_state)))

            dfa_transitions[transition] = ','.join(sorted(next_state))

        # Add 'fuiken' and check for removable states
        deleted = 1
        while deleted > 0:
            deleted = 0
            for transition in dfa_transitions.copy().items():
                for c in self.alphabet:
                    # A char from the alphabet is missing, so we need to add a 'fuik'
                    if (transition[0][0], c) not in dfa_transitions.keys():
                        dfa_transitions[transition[0][0], c] = '{}'
                        # if the fuik doesn't exist yet
                        for ch in self.alphabet:
                            dfa_transitions[('{}', ch)] = '{}'
                    # Check if this state can be reached at all
                    if (transition[0][0], c) in dfa_transitions.keys() \
                            and transition[0][0] is not self.start \
                            and not any(transition[0][0] == dfa_transitions[i]
                                        and i[0] != transition[0][0] for i in dfa_transitions):
                        del dfa_transitions[(transition[0][0], c)]
                        deleted += 1

        return DFA(self.alphabet, dfa_transitions, start_state, final_states)

    def generate_words(self, length=5):
        """
        Generate a list of words which are accepted and not accepted
        """
        accepted = []
        not_accepted = []
        for i in range(1, length):
            for combination in list(itertools.product(['a', 'b'], repeat=i)):
                str_combination = ''.join(combination)
                if self.accept(combination):
                    accepted.append(str_combination)
                else:
                    not_accepted.append(str_combination)
        return accepted, not_accepted

    def get_graph(self, name="output", current_states=None):
        """
        Generate a graphviz graph.
        Name = Output file name
        current_states = If using in step mode, the current state will be colored red
        """
        graph = nx.DiGraph()
        for key, value in self.transitions.items():
            for t in value:
                label = key[1]

                # If this state transition already exist we should combine the label.
                if graph.get_edge_data(key[0], t):
                    label += "," + graph.get_edge_data(key[0], t)["label"]

                # Color current state
                state_color = 'Black'
                transition_color = 'Black'
                if current_states is not None:
                    if key[0] in current_states:
                        state_color = 'Red'
                        graph.add_node(key[0], color="Red")
                    if t in current_states:
                        transition_color = 'Red'
                        graph.add_node(t, color="Red")

                # If this state is an end state
                if key[0] in self.finals:
                    graph.add_node(key[0], shape="doublecircle", color=state_color)
                if t in self.finals:
                    graph.add_node(t, shape="doublecircle", color=transition_color)

                # If this state is a start state
                if key[0] in self.start:
                    graph.add_node(' ', shape="point")
                    graph.add_edge(' ', key[0])

                graph.add_edge(key[0], t, label=label)

        # trick for labeling
        for u, v, d in graph.edges(data=True):
            d['label'] = d.get('label', '')

        png = nx.nx_agraph.to_agraph(graph)
        png.layout(prog='dot')
        png.draw('output/' + name + '.png')
