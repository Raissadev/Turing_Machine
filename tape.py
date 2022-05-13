class Tape(object):

    blank = " "

    def __init__(self, tape = ""):
        self.__tape = dict((enumerate(tape)))

    def __str__(self) -> str:
        string_ = ""
        min_index = min(self.__tape.keys())
        max_index = max(self.__tape.keys())

        for i in range(min_index, max_index):
            string_ += self.__tape[i]
        
        return string_

    def __getitem__(self, index: int):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank

    def __setitem__(self, pos: int, char: str):
        self.__tape[pos] = char