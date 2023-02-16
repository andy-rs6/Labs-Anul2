import Grammar
#Varianta 8

# Set of terminal symbols
VT = {'a', 'b', 'c', 'd', 'e'}

# Set of non-terminal symbols
VN = {'S', 'D', 'E', 'J'}



# Set of productions, rules or transitions
P = {"S": ["aD"],"D": ["dE", "bJ", "aE"],"J": ["cS"],"E": ["eX", "aE"],"X": " " }

# Initiate the grammar
grammar = Grammar.Grammar(VN, VT, P)

# Initiate hte finite automaton
finite_automaton = grammar.to_finite_automaton()


# Create five words
word_1 = grammar.generate_string()
word_2 = grammar.generate_string()
word_3 = grammar.generate_string()
word_4 = grammar.generate_string()
word_5 = grammar.generate_string()

# Print the word with validation
print("word_1 = {x} ".format(x = word_1) + " | " + str(finite_automaton.string_belongs_to_language(word_1)))
print("word_2 = {x} ".format(x = word_2) + " | " + str(finite_automaton.string_belongs_to_language(word_2)))
print("word_3 = {x} ".format(x = word_3) + " | " + str(finite_automaton.string_belongs_to_language(word_3)))
print("word_4 = {x} ".format(x = word_4) + " | " + str(finite_automaton.string_belongs_to_language(word_4)))
print("word_5 = {x} ".format(x = word_5) + " | " + str(finite_automaton.string_belongs_to_language(word_5)))