from classes.Rotors.RotorFactory import RotorFactory
from classes.Reflectors.Reflector import Reflector
from classes.RotorBloc import RotorBloc
from classes.Plugboard import Plugboard

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

reflector = Reflector()

rotor_factory = RotorFactory()
r_left = rotor_factory.create_rotor("I", 'A', 'B')
r_middle = rotor_factory.create_rotor("II", 'A', 'B')
r_rigth = rotor_factory.create_rotor("III", 'A', 'B')

rotor_bloc = RotorBloc(r_left, r_middle, r_rigth, reflector)
input_letter = 'A'

print(input_letter, "->", rotor_bloc.transform_signal(input_letter))
print(input_letter, "->", rotor_bloc.transform_signal(input_letter))
print(input_letter, "->", rotor_bloc.transform_signal(input_letter))
print(input_letter, "->", rotor_bloc.transform_signal(input_letter))
print(input_letter, "->", rotor_bloc.transform_signal(input_letter))

# plugboard = Plugboard()
# plugboard.add_plug("A", "D")
# plugboard.add_plug("B", "E")
# plugboard.add_plug("C", "F")
# for l in ALPHA:
#     print(l, "->", plugboard.convert_letter(l), end=" | ")

# print()