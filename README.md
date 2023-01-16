# Enigma

This repo contains a Python implementation of the Enigma machine I.

Rotors of type (I, II, III, IV and V) are available as well as reflectors of type (A, B, C).

## Usage

### Creating the Rotor Bloc
The rotor bloc is composed of 3 rotors and 1 reflector.

You can use the `RotorFactory` static class to instantiate rotors.

```py
rotor = RotorFactory().create_rotor(
    "I",    # Rotor type (I, II, III, IV, V)
    'C',    # Initial position (Grundstellung)
    'F'     # Rotor settings (Ringstellung)
    )
```

You can use the `ReflectorFactory` static class to instantiate reflectors.

```py
reflector = ReflectorFactory().create_reflector(
    "B"     # Reflector type (A, B, C)
    )
```

Finally, you can assemble those 4 elements into the rotor bloc like that:
```py
rotor_bloc = RotorBloc(r_left, r_middle, r_rigth, reflector)
```

### Creating the Plugboard

You can create an empty `Plugboard` like that:
```py
plugboard = Plugboard()
```
and you can plug plugs on it like that:
```py
plugboard.add_plug("P", "F") # This will swap letter P and F
```

### Assembling the Enigma Machine

Once everything is defined you just have to assemble it like that:
```py
enigma = Enigma(rotor_bloc, plugboard)
```
And now you can use the `crypt` method with a string in argument to crypt it.
```py
plaintext = "CIPHER TEST"
ciphertext = enigma.crypt(plaintext)
```

## Sources

My understanding of the Enigma machine comes from these sources:
- YouTube video from Jared Owen: [How did the Enigma Machine work?](https://www.youtube.com/watch?v=ybkkiGtJmkM)

- Technical details: https://www.ciphermachinesandcryptology.com/en/enigmatech.htm

- Wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details

- Stack Exchange comment: https://crypto.stackexchange.com/a/71233xw