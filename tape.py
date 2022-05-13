class Tape(object):

    blank = " "

    def __init__(self, tape = ""):
        self.tape = dict((enumerate(tape)))

    def __str__(self) -> str:
        string_ = ""
        min_index = min(self.tape.keys())
        max_index = max(self.tape.keys())

        for i in range(min_index, max_index):
            string_ += self.tape[max_index]
        
        return string_

    def __getitem__(self, index: int):
        if index in self.tape:
            return self.tape[index]
        else:
            return Tape.blank

    def __setitem__(self, pos: int, char: str):
        self.tape[pos] = char