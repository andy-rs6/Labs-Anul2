import FiniteAutomaton
import random

class Grammar:
    # Constructor of Grammar class
    def __init__(self, VN, VT, P):
        self.VT = VT
        self.VN = VN
        self.P = P

    # Generate the strings
    def generate_string(self):
        # Start of the string
        string = "S"
        # Set of final states
        final_state = " "

        # Create a random string
        while string[-1] not in final_state:
            arr = []
            #go trough items and get the keys and values
            for key, value in self.P.items():
                if key == string[-1]:
                    #move the value in array
                    arr += value
            if not arr:
                return None
            production = random.choice(arr)
            #Reverse string, count backwards
            string = string[:-1] + production
        return string

    # Convert from grammar to finite automaton, sending all the params with self
    def from_grammar_to_finite_automaton(self):
        # Initiate finite set of states
        Q = set(self.VN)
        # Initiate the alphabet with all the characters
        Sigma = set(self.VT)
        # Initiate the initial state from the list
        q0 = "S"
        # Initiate the set of final states from the list
        F = "X"
        # Initiate the transition function
        arr = {}
        for key, value in self.P.items():
            for symbol in value:
                if (key, symbol[0]) in arr :
                    arr[(key, symbol[0])].append(symbol[1:])
                else:
                    arr[(key, symbol[0])] = [symbol[1:]]
        print("Automation :", arr)

        # Call the constructor of Finite Automaton with all the params
        return FiniteAutomaton.FiniteAutomaton(Q, Sigma, arr, q0, F)