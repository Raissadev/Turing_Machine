from tape import Tape

class TuringMachine:

    def __init__(self, tape: str = "", blank: str = " ", initial_state: str = "", final_states: str = None, transaction: dict[str, str] = None):
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
        index = (self.current_state, char)

        if index in self.transaction:
            position = self.transaction[index]
            self.tape[self.head] = position[1]

            if position[2] == "R":
                self.head += 1
            elif position[2] == "L":
                self.head -= 1
            self.current_state = position[0]

    def final(self) -> bool:
        if self.current_state in self.final_states:
            return True
        else:
            return False