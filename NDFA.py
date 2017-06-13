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
            else:  # There is no transition found, so this path dies
                pass
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

            if not any(i[0] == name for i in dfa_transitions):
                # Check final state
                if len(set(states).intersection(self.finals)) > 0:
                    final_states.add(name)

                next_states = {key: set() for key in [char for char in self.alphabet]}
                states = list(states)
                for s in states:  # Search next states
                    if (s, '$') in self.transitions:
                        states.extend(self.transitions[(s, '$')])
                    for char in self.alphabet:
                        if (s, char) in self.transitions:
                            next_states[char] |= set(self.transitions[(s, char)])

                for s in next_states:  # Create next states
                    next_state = ','.join(sorted(next_states[s]))
                    if next_state == '':
                        dfa_transitions[(name, s)] = '{}'
                    else:
                        dfa_transitions[(name, s)] = next_state
                        create_new_state(next_states[s])

        # Generate the new states
        create_new_state(self.start)

        # Check if there is an fuik created
        if any(dfa_transitions[i] == '{}' for i in dfa_transitions):
            for char in self.alphabet:
                dfa_transitions[('{}', char)] = '{}'

        return DFA(self.alphabet, dfa_transitions, start_state, final_states)

    def generate_words(self, length=5):
        """
        Generate a list of words which are accepted and not accepted
        """
        accepted = []
        not_accepted = []
        for i in range(1, length):
            for combination in list(itertools.product(self.alphabet, repeat=i)):
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
