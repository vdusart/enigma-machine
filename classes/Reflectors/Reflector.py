
class Reflector:
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, internal_wiring):
        self.internal_wiring = internal_wiring

    def reflect(self, input_letter):
        # print(f"{input_letter} -> {self.internal_wiring[self.ALPHA.index(input_letter)]}")
        return self.internal_wiring[self.ALPHA.index(input_letter)]