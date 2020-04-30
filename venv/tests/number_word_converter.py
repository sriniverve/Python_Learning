'''
This is a program to take number input & print number in words
'''

number = input("Enter the phone number: ")
digits_mappings = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
num_in_words = ""
for digit in number:
    num_in_words += digits_mappings.get(digit, "!")+" "

print(num_in_words)
