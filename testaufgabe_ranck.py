# entfernt die anderen Zeichen, lässt nur die Binärzahl übrig
def clip(string):
    return string[1:-3]

def convert_to_decimal(binary_string):
    length = len(binary_string)
    p = length - 1
    i = 0
    decimal_number = 0
    while i < length:
        if binary_string[i] == "1":
            decimal_number = decimal_number + 2**p
        p -= 1
        i += 1
    return decimal_number

def is_palindrome(binary_string):
    i = 0
    half_the_length = int(len(binary_string)/2)
    while i < half_the_length:
        if binary_string[i] != binary_string[-i-1]:
            return False
        i += 1
    return True

with open("numbers.txt", "r") as file:
    sum = 0
    for line in file:
        binary_string = clip(line)
        if is_palindrome(binary_string):
            sum = sum + convert_to_decimal(binary_string)
    print("Der Gesamtwert ist: " + str(sum))
