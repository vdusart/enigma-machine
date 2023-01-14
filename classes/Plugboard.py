
class Plugboard:
    def __init__(self):
        self.plugs = {}
    
    def add_plug(self, letter_1, letter_2):
        if letter_1 in self.plugs or letter_2 in self.plugs:
            raise Exception(f"This letter is already in the plugboard ({letter_1 if letter_1 in self.plugs else letter_2})")
        self.plugs[letter_1] = letter_2
        self.plugs[letter_2] = letter_1
    
    def convert_letter(self, letter):
        return letter if letter not in self.plugs else self.plugs[letter]