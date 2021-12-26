number_dictionary = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero',
}

phone_number = input('Enter Your Phone Number: ')

output = ''

for digit in phone_number:
    output += number_dictionary.get(digit, '***') + ' '

print(output)
