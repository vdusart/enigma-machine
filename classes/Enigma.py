from .RotorBloc import RotorBloc
from .Plugboard import Plugboard

class Enigma:
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, rotor_bloc: RotorBloc, plugboard: Plugboard):
        self.rotor_bloc = rotor_bloc
        self.plugboard = plugboard

    def crypt(self, plaintext: str):
        ciphertext = ""
        for l in plaintext.upper():
            if l not in self.ALPHA:
                ciphertext += l
                continue
            ciphered_letter = self.plugboard.convert_letter(l)
            ciphered_letter = self.rotor_bloc.transform_signal(ciphered_letter)
            ciphered_letter = self.plugboard.convert_letter(ciphered_letter)
            ciphertext += ciphered_letter
        
        return ciphertext