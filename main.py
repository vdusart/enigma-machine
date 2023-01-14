from classes.Plugboard import Plugboard

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plugboard = Plugboard()
plugboard.add_plug("A", "D")
plugboard.add_plug("B", "E")
plugboard.add_plug("C", "F")
for l in ALPHA:
    print(l, "->", plugboard.convert_letter(l), end=" | ")

print()