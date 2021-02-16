
dict = {}

with open("morse-code.txt") as file:
    data = file.readlines()
    for symbol in data:
        dict[symbol[0]] = symbol[2:].strip()




string_to_be_converted = input("Enter the string: ")
string_to_be_converted = string_to_be_converted.upper()


coded_string = ""

for letter in range(0, len(string_to_be_converted)):
    for (key, value) in dict.items():
        if key == string_to_be_converted[letter]:
            coded_string += f"{value} "
        elif string_to_be_converted[letter] == " ":
            coded_string += " "*7

print(coded_string)