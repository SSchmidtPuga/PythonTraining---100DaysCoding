morse_code = {"A": " · –", "B": " – · · ·", "C": " – · – ·", "D": " – · ·", "E": " ·", "F": " · · – ·", "G": " – – ·  ",
              "H": " · · · ·", "I": " · ·", "J": " · – – –", "K": " – · –  ", "L": " · – · ·", "M": " – –", "N": " – ·",
              "O": " – ––  ", "P": " · – – ·", "Q": " – – · –", "R": " · – ·", "S": " · · ·", "T": " –",
              "U": " · · –  ", "V": " · · · –", "W": " · – –  ", "X": " – · · –", "Y": " – · – –", "Z": " – – · ·",
              "1": " · – – – – ", "2": " · · – – – ", "3": " · · · – – ", "4": " · · · · – ", "5": " · · · · · ",
              "6": " – · · · · ", "7": " – – · · · ", "8": " – – – · · ", "9": " – – – – · ", "0": " – – – – – ",
              ".": " · – · – · – ", ",": " – – · · – – "}

String = str(input("Please provide a string: "))
morse_caracters = []
string = ''


for letters in String:
    new_letter = morse_code[letters.upper()]
    morse_caracters.append(new_letter)
    string = ''.join(morse_caracters)

print(string)
