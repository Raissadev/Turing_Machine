from tape import Tape

class TuringMachine:

    def __init__(self, tape: str = "", blank: str = " ", initial_state: str = "", final_states: str = None, transaction: dict[str, str] = None):
        self.__tape = Tape(tape)
        self.__head = 0
        self.__blank = blank
        self.__current_state = initial_state

        if transaction == None:
            self.transaction = {}
        else:
            self.transaction = transaction
        
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def getTape(self) -> str:
        return str(self.__tape)

    def step(self) -> None:
        char = self.__tape[self.__head]
        index = (self.__current_state, char)

        if index in self.transaction:
            position = self.transaction[index]
            self.__tape[self.__head] = position[1]

            if position[2] == "R":
                self.__head += 1
            elif position[2] == "L":
                self.__head -= 1
            self.__current_state = position[0]

    def final(self) -> bool:
        if self.__current_state in self.final_states:
            return True
        else:
            return False