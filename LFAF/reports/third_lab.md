# Topic: Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Andrei Ceban FAF-211

## Theory
&ensp;&ensp;&ensp; Lexer and scanner are terms that are often used interchangeably in the field of computer science, but they refer to slightly different concepts. In general, a lexer (short for lexical analyzer) is a program that takes a stream of characters as input and breaks it up into a series of tokens, which are the basic building blocks of a programming language.

&ensp;&ensp;&ensp; The scanner is a component of the lexer that reads the input stream of characters and identifies the individual tokens. In some cases, the scanner and lexer may be separate programs or components of a larger program, but they are typically closely related and work together to parse the input.

&ensp;&ensp;&ensp; The process of tokenizing involves breaking up the input stream into distinct pieces that represent the various elements of a programming language, such as keywords, operators, identifiers, and literals. These tokens are then passed on to the next stage of the parsing process, where they are analyzed and interpreted.

&ensp;&ensp;&ensp; The lexer and scanner are critical components of any compiler or interpreter for a programming language. They play a key role in parsing the input code and generating an abstract syntax tree (AST) that can be used by the compiler or interpreter to generate executable code.

&ensp;&ensp;&ensp; The lexer and scannerare fundamental components of the parsing process in a programming language. The lexer takes an input stream of characters and breaks it up into a series of tokens, while the scanner is responsible for identifying the individual tokens in the input stream. Together, they provide the foundation for the compilation or interpretation of a programming language.

## Objectives:

- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.

## Implementation description
### check_deterministic
&ensp;&ensp;&ensp; This code checks whether the finite automaton represented by the object is deterministic or not. It does so by creating a transition map that maps the current state and input symbol to a set of next states. If any state in the automaton has multiple transitions for the same input symbol, then the automaton is non-deterministic and the method returns false. Otherwise, the automaton is deterministic and the method returns true. The method takes no arguments and returns a boolean value.

```
def check_deterministic(self):
    for state in self.states:
        for symbol in self.alphabet:
            next_states = self.transitions.get((state, symbol), set())
            if len(next_states) != 1:
                return False
    return True
```
### NDFA_to_a_DFA
&ensp;&ensp;&ensp; This code converts a non-deterministic finite automaton NFA to a deterministic finite automaton DFA. It does so by creating a power set of all possible states of the NFA, creating a new DFA transition table, and then using the transition table to create the DFA.
The method creates a power set of all possible states of the NFA by calling the "getPowerSet" method, which returns a set of sets representing all possible combinations of states. The method then creates a new DFA transition table by iterating over all state sets in the power set and creating a set of next states for each symbol in the alphabet by examining the possible transitions from each state in the current state set for each input symbol. Finally, the method creates a new DFA by initializing the new DFA with the transition table, final states, and initial state.

```
def NDFA_to_a_DFA(self):
    if self.check_deterministic():
        return self

    dfa_states = set()
    dfa_F = set()
    dfa_transitions = dict()
    state_queue = [frozenset([self.q0])]
    while state_queue:
        current_states = state_queue.pop(0)
        dfa_states.add(current_states)
        if any(state in self.F for state in current_states):
            dfa_F.add(current_states)
        for symbol in self.alphabet:
            next_states = set()
            for state in current_states:
                next_states |= set(self.transitions.get((state, symbol), set()))
            if next_states:
                next_states = frozenset(next_states)
                dfa_transitions[(current_states, symbol)] = next_states
                if next_states not in dfa_states:
                    state_queue.append(next_states)

    dfa = ChomskyHierarchy(self, self.alphabet, self.F, self.q0, self.transitions)
    dfa.states = dfa_states
    dfa.F = dfa_F
    dfa.transitions = dfa_transitions

return dfa
```

### isRegularGrammar
- The isRegularGrammar() method checks if the right-hand side of every production consists of either a single lowercase letter or two symbols where the first symbol is uppercase and the second is lowercase. If all productions satisfy this condition, then the grammar is regular.


```
def check_Context_sensitive(self, P):

    for symbol, string in P.items():
        for rhs in string:
            if len(rhs) < len(symbol):
                return False
            for i, symbol in enumerate(rhs):
                if symbol in P and i != len(rhs) - 1:
                    if len(rhs) <= len(symbol):
                        return False
    return True


```
### isContextFreeGrammar
- The isContextFreeGrammar() method checks if the left-hand side of every production is a single uppercase letter and the right-hand side consists of either uppercase or lowercase letters. If all productions satisfy this condition, then the grammar is context-free.


```
def check_Context_free(self, P):

    for symbol, string in P.items():
        if len(symbol) != 1 or not symbol.isupper():
            return False
        for rhs in string:
            for symbol in rhs:
                if symbol not in P and not symbol.islower():
                    return False
    return True
```

### isContextSensitiveGrammar
- The isContextSensitiveGrammar() method checks if the length of the left-hand side of every production is less than or equal to the length of the right-hand side. If all productions satisfy this condition, then the grammar is context-sensitive.

```
def check_Regular(self, P):

    for symbol, string in P.items():
        if not symbol.isupper():
            return False
        for rhs in string:
            if len(rhs) == 1 and rhs.islower():
                continue
            elif len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper():
                continue
            else:
                return False
    return True
```



## Results
![Alt text](screenshots/lab2.png)
## Conclusions
&ensp;&ensp;&ensp; After doing this laboratory work,i understand that determinism in finite automata is an important
concept in computer science that refers to the ability of a machine to uniquely determine its next state
based on the current input and state. Deterministic finite automata (DFA) are particularly useful for pattern
recognition and language processing tasks, as they can efficiently recognize regular languages.

The process of converting a non-deterministic finite automaton (NDFA) to a DFA involves transforming the NDFA into a deterministic version of itself, where each input symbol leads to exactly one next state. This conversion is important for simplifying the machine and making it easier to analyze and
understand.

Also, using the Chomsky hierarchy which is a classification of formal languages into four categories
based on their complexity and the types of grammars that can generate them. These categories include regular languages, context-free languages, context-sensitive languages, and recursively enumerable languages.
Each category has its own set of rules and limitations, and understanding these categories can help in the
design and analysis of computational systems.

