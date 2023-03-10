class Rotor:
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    IS_VERBOSE = False

    def __init__(self, internal_wiring, notch_position, initial_position, setting):
        self.internal_wiring = internal_wiring
        self.notch_position = notch_position
        self.position = initial_position
        self.setting = setting

    def rotor_permutation(self, index, is_reverse):
        return self.internal_wiring[index] if not is_reverse else self.ALPHA[self.internal_wiring.index(self.ALPHA[index])]

    def calculate_offset_input(self):
        position_offset = self.ALPHA.index(self.position)
        setting_offset = -self.ALPHA.index(self.setting)

        return position_offset + setting_offset

    def calculate_offset_output(self):
        position_offset = -self.ALPHA.index(self.position)

        setting_offset = self.ALPHA.index(self.setting)

        return position_offset + setting_offset

    def get_letter(self, input_letter, is_reverse):
        self.IS_VERBOSE and print("Current position:", self.position)
        offset_input = self.calculate_offset_input()
        letter_index = (self.ALPHA.index(input_letter) + offset_input) % len(self.ALPHA)

        offset_output = self.calculate_offset_output()
        output = self.ALPHA[(self.ALPHA.index(self.rotor_permutation(letter_index, is_reverse)) + offset_output)%len(self.ALPHA)]
        self.IS_VERBOSE and print(f"{input_letter} -> {self.ALPHA[letter_index]} -> {self.rotor_permutation(letter_index, is_reverse)} -> {output}")
        return output
    
    def rotate(self):
        next_rotor_should_rotate = self.position == self.notch_position
        self.position = self.ALPHA[(self.ALPHA.index(self.position) + 1)%len(self.ALPHA)]
        return next_rotor_should_rotate