from .Reflector import Reflector

class ReflectorFactory:

    REFLECTORS = {
        "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    }

    @staticmethod
    def is_reflector_type_available(reflector_type):
        return reflector_type in ReflectorFactory.REFLECTORS

    @staticmethod
    def create_reflector(reflector_type: str):
        if not ReflectorFactory.is_reflector_type_available(reflector_type):
            raise Exception(f"This reflector_type is not defined. (reflector_type: {reflector_type})")
        return Reflector(ReflectorFactory.REFLECTORS[reflector_type])