from classes.Rotors.RotorFactory import RotorFactory
from classes.Reflectors.Reflector import Reflector
from classes.RotorBloc import RotorBloc
from classes.Plugboard import Plugboard
from classes.Enigma import Enigma

# Creation of the reflector
reflector = Reflector()

# Creation of the rotors
rotor_factory = RotorFactory()
r_left = rotor_factory.create_rotor("I", 'C', 'F')
r_middle = rotor_factory.create_rotor("II", 'B', 'E')
r_rigth = rotor_factory.create_rotor("III", 'A', 'D')

rotor_bloc = RotorBloc(r_left, r_middle, r_rigth, reflector)

# Creation of the plugboard
plugboard = Plugboard()

enigma = Enigma(rotor_bloc, plugboard)

plaintext = "CIPHER TEST"

ciphertext = enigma.crypt(plaintext)

wanted_output = "SLFLPV PVYW"
print(ciphertext == wanted_output)
