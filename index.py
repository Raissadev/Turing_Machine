from machine import TuringMachine

class Main:

    def __init__(self):
        self.initial_state = "init"
        self.accepting_states = ["final"]
        self.transaction = {
            ("init","0"):("init", "1", "R"),
            ("init","1"):("init", "0", "R"),
            ("init"," "):("final"," ", "N"),
        }
        self.final_states = {"final"}

    def run(self) -> None:
        numbers = input("Binary numbers for the machine: ")

        for number in numbers:
            if number != "0" and number != "1":
                print(f"Enter only binary base numbers!")
                return

        turing = TuringMachine(numbers, initial_state = "init", final_states = self.final_states, transaction = self.transaction)

        print(f"Input on Tape: {turing.getTape()}")

        while not turing.final():
            turing.step()

        print(f"Result of the turing machine calculation: {turing.getTape()}")


go = Main()
go.run()