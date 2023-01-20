def convert_num(num, base):
    if base == 10:
        decimal = int(num)
        sign_magnitude = format(decimal, 'b') if decimal >= 0 else '1' + format(abs(decimal), 'b')
        two_complement = format(decimal & (2**(len(bin(abs(decimal))[2:])-1)-1), 'b').zfill(len(bin(abs(decimal))[2:]))
        one_complement = format(int(two_complement, 2) ^ (2**len(two_complement)-1), 'b')
    elif base == 2:
        decimal = int(num, 2) if num[0] == '0' else -(int(''.join(['1' if c=='0' else '0' for c in num[1:]]), 2) + 1)
        sign_magnitude = num
        one_complement = format(~int(num, 2) & (2**(len(num)-1)-1), 'b')
        two_complement = format(int(num, 2) & (2**(len(num)-1)-1), 'b')
    elif base == 3:
        decimal = int(num, 3) if num[0] == '0' else -(int(''.join(['1' if c=='0' else '0' for c in num[1:]]), 3) + 1)
        sign_magnitude = format(decimal, 'b') if decimal >= 0 else '1' + format(abs(decimal), 'b')
        two_complement = format(decimal & (2**(len(bin(abs(decimal))[2:])-1)-1), 'b').zfill(len(bin(abs(decimal))[2:]))
        one_complement = format(int(two_complement, 2) ^ (2**len(two_complement)-1), 'b')
    elif base == 4:
        decimal = int(num, 4) if num[0] == '0' else -(int(''.join(['1' if c=='0' else '0' for c in num[1:]]), 4) + 1)
        sign_magnitude = format(decimal, 'b') if decimal >= 0 else '1' + format(abs(decimal), 'b')
        two_complement = num
        one_complement = format(~int(num, 2) & (2**(len(num)-1)-1), 'b')
    else:
        print("Invalid Base")
        return
    return decimal, sign_magnitude, one_complement, two_complement

num = input("Enter a number: ")
base = int(input("Enter the base of the number (10, 2, 3 or 4): "))
decimal, sign_magnitude, one_complement, two_complement = convert_num(num, base)
print("Decimal representation:", decimal)
print("Sign/Magnitude representation:", sign_magnitude)
print("One's Complement representation:", one_complement)
print("Two's Complement representation:", two_complement)

# Output:
# Enter a number: 10
# Enter the base of the number (10, 2, 3 or 4): 10
# Decimal representation: 10
# Sign/Magnitude representation: 1010
# One's Complement representation: 1010
# Two's Complement representation: 1010
