from tape import Tape

class TuringMachine:

    def __init__(self, tape = "", blank = " ", initial_state = "", final_states = None, transaction = None):
        self.tape = Tape(tape)
        self.head = 0
        self.blank = blank
        self.current_state = initial_state

        if transaction == None:
            self.transaction = {}
        else:
            self.transaction = transaction
        
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def getTape(self) -> str:
        return str(self.tape)

    def step(self) -> None:
        char = self.tape[self.head]
        x = (self.current_state, char)

        if x in self.transaction:
            y = self.transaction[x]
            self.tape[self.head] = y[1]
            if y[2] == "R":
                self.head += 1
            elif y[2] == "L":
                self.head -= 1
            self.current_state = y[0]

    def final(self) -> bool:
        if self.current_state in self.final_states:
            return True
        else:
            return False