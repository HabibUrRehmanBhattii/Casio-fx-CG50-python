#Conversion function
def convert_bits(value, from_unit):
    #Dictionary to hold the conversion factors
    conversion_factors = {
        "bit": {
            "kbit": 1/1000,
            "kibibit": 1/1024,
            "kByte": 1/8000,
            "Kibibyte": 1/8192,
            "Mebibyte": 1/8589934592,
            "Mebibit": 1/1048576,
            "Mbit": 1/1000000
        }
    }
    #Checking if the input unit is valid or not
    if from_unit not in conversion_factors.keys():
        print("Invalid unit input")
        return 
    #Iterating through the units
    for to_unit in conversion_factors[from_unit]:
        #Calculating the conversion
        quotient = value * conversion_factors[from_unit][to_unit]
        print(str(value) + " " + from_unit + " = " + str(quotient) + " " + to_unit)

#Taking input from user
value = int(input("Enter the value: "))
from_unit = input("Enter the unit (bit, kibibit, kByte, Kibibyte, Mebibyte, Mebibit, Mbit): ")

#Example usage
convert_bits(value, from_unit)
