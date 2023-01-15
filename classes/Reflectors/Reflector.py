
class Reflector:
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self):
        self.internal_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    def reflect(self, input_letter):
        # print(f"{input_letter} -> {self.internal_wiring[self.ALPHA.index(input_letter)]}")
        return self.internal_wiring[self.ALPHA.index(input_letter)]