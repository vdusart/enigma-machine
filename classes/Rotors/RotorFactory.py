from .Rotor import Rotor

class RotorFactory:

    ROTORS = {
        "I": {
            "internal_wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        },
        "II": {
            "internal_wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        },
        "III": {
            "internal_wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        }
    }

    def is_rotor_type_available(self, rotor_type):
        return rotor_type in self.ROTORS

    def create_rotor(self, rotor_type: str, initial_position, setting):
        if not self.is_rotor_type_available(rotor_type):
            raise Exception(f"This rotor_type is not defined. (rotor_type: {rotor_type})")
        return Rotor(self.ROTORS[rotor_type]['internal_wiring'], initial_position, setting)