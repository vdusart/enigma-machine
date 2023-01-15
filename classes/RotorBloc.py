from classes.Rotors.Rotor import Rotor
from classes.Reflectors.Reflector import Reflector

class RotorBloc:
    def __init__(self, rotor_left: Rotor, rotor_middle: Rotor, rotor_right: Rotor, reflector: Reflector):
        self.rotor_left = rotor_left
        self.rotor_middle = rotor_middle
        self.rotor_right = rotor_right
        self.reflector = reflector

    def rotate_all_rotors(self):
        # TO DO: Proper rotors rotations
        # self.rotor_left.rotate()
        # self.rotor_middle.rotate()
        self.rotor_right.rotate()
    
    def transform_signal(self, input_letter):
        self.rotate_all_rotors()
        output = self.rotor_right.get_letter(input_letter, False)
        output = self.rotor_middle.get_letter(output, False)
        output = self.rotor_left.get_letter(output, False)

        output = self.reflector.reflect(output)

        output = self.rotor_left.get_letter(output, True)
        output = self.rotor_middle.get_letter(output, True)
        output = self.rotor_right.get_letter(output, True)
        return output
