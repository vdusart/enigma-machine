from classes.Rotors.RotorFactory import RotorFactory
from classes.Reflectors.ReflectorFactory import ReflectorFactory
from classes.RotorBloc import RotorBloc
from classes.Plugboard import Plugboard
from classes.Enigma import Enigma

# Creation of the reflector
reflector = ReflectorFactory().create_reflector("B")

# Creation of the rotors
r_left = RotorFactory().create_rotor("I", 'C', 'F')
r_middle = RotorFactory().create_rotor("II", 'B', 'E')
r_rigth = RotorFactory().create_rotor("III", 'A', 'D')

rotor_bloc = RotorBloc(r_left, r_middle, r_rigth, reflector)

# Creation of the plugboard
plugboard = Plugboard()
plugboard.add_plug("P", "F")

enigma = Enigma(rotor_bloc, plugboard)

plaintext = "CIPHER TEST"

ciphertext = enigma.crypt(plaintext)

print(ciphertext)
