word = "Hello"

for letter in word:
    ascii_code = ord(letter)
    binary = "{0:08b}".format(ascii_code)
    hexadecimal = "{0:02x}".format(ascii_code)
    print("ASCII" + letter + " is " + str(ascii_code) + " binary " + binary + " hexa" + hexadecimal + ".")


# This code will convert a string to binary and hexadecimal and print the result. 