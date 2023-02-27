import Grammar
from ChomskyHierarchy import ChomskyHierarchy
#Varianta 8

# Set of terminal symbols
VT = {'a', 'b', 'c', 'd', 'e'}

# Set of non-terminal symbols
VN = {'S', 'D', 'E', 'J'}

# Set of productions, rules or transitions
P = {"S": ["aD"],"D": ["dE", "bJ", "aE"],"J": ["cS"],"E": ["eX", "aE"],"X": " " }

# Initiate the grammar calling the constructor with all 3 params
grammar = Grammar.Grammar(VN, VT, P)

# Initiate the finite automaton
finite_automaton = grammar.from_grammar_to_finite_automaton()

# Generate 5 string
word_1 = grammar.generate_string()
word_2 = grammar.generate_string()
word_3 = grammar.generate_string()
word_4 = grammar.generate_string()
word_5 = grammar.generate_string()

# Print the strings including the  validation
# print("word_1 = {x} ".format(x = word_1) + " | " + str(finite_automaton.check_string(word_1)))
# print("word_2 = {x} ".format(x = word_2) + " | " + str(finite_automaton.check_string(word_2)))
# print("word_3 = {x} ".format(x = word_3) + " | " + str(finite_automaton.check_string(word_3)))
# print("word_4 = {x} ".format(x = word_4) + " | " + str(finite_automaton.check_string(word_4)))
# print("word_5 = {x} ".format(x = word_5) + " | " + str(finite_automaton.check_string(word_5)))
#

automation = ChomskyHierarchy()
automation.states = ['q0', 'q1', 'q2', 'q3', 'q4']
automation.alphabet = ['a', 'b']
automation.transitions = {('q0', 'a'): {'q1'},
            ('q1', 'b'): {'q2'},
            ('q2', 'b'): {'q0'},
            ('q3', 'a'): {'q4'},
            ('q4', 'a'): {'q0'},
            ('q2', 'a'): {'q3'},
            ('q1', 'b'): {'q1'}}
automation.start_state = 'q0'
automation.accept_states = ['q3']
print('')
print('')
print('')
print('-------------------------------------------------------------------LAB2-------------------------------------------------------------------------')
# Check if automaton is deterministic
is_deterministic = automation.is_deterministic()
print(f"Is automaton deterministic? {is_deterministic}")

# Convert NDFA to DFA
dfa = automation.to_dfa()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")

# Convert automaton to regular grammar
grammar = automation.to_grammar()
print(f"Regular grammar productions: {grammar}")

