import FiniteAutomaton

class Grammar:
    # Constructor of Grammar class
    def __init__(self, VN, VT, P):
        self.VN = VN
        self.VT = VT
        self.P = P

    # Method which generate words corresponding to rules
    def generate_string(self):
        import random
        # Start of the word
        word = "S"
        # Set of final states
        final_state = " "
        # While loop which create a random word
        while word[-1] not in final_state:
            options = []
            for vn, prod in self.P.items():
                if vn == word[-1]:
                    options += prod
            if not options:
                return None
            production = random.choice(options)
            word = word[:-1] + production
        return word

    # Method which transfer from grammar class to finite automaton class
    def to_finite_automaton(self):
        # Initiate finite set of states
        Q = set(self.VN)
        # Initiate the alphabet
        Sigma = set(self.VT)
        # Initiate the initial state
        q0 = "S"
        # Initiate the set of final states
        F = "X"
        # Initiate the transition function
        delta = {}
        for vn, prod in self.P.items():
            for symbol in prod:
                if (vn, symbol[0]) in delta :
                    delta[(vn, symbol[0])].append(symbol[1:])
                else:
                    delta[(vn, symbol[0])] = [symbol[1:]]
        print("AUtomation ", delta)


        # Call the constructor of Finite Automaton class
        return FiniteAutomaton.FiniteAutomaton(Q, Sigma, delta, q0, F)

