from .Rotor import Rotor

class RotorFactory:

    ROTORS = {
        "I": {
            "internal_wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "notch_position": "Q"
        },
        "II": {
            "internal_wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "notch_position": "E"
        },
        "III": {
            "internal_wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "notch_position": "V"
        },
        "IV": {
            "internal_wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "notch_position": "J"
        },
        "V": {
            "internal_wiring": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "notch_position": "Z"
        }
    }

    @staticmethod
    def is_rotor_type_available(rotor_type):
        return rotor_type in RotorFactory.ROTORS

    @staticmethod
    def create_rotor(rotor_type: str, initial_position, setting):
        if not RotorFactory.is_rotor_type_available(rotor_type):
            raise Exception(f"This rotor_type is not defined. (rotor_type: {rotor_type})")
        return Rotor(
                RotorFactory.ROTORS[rotor_type]['internal_wiring'],
                RotorFactory.ROTORS[rotor_type]['notch_position'],
                initial_position,
                setting
            )