# Finding the largest number in list

number_list = []
for i in range(5):
    n = int(input(f'Enter number {i + 1}: '))
    number_list.append(n)

print(f'Your Numbers are: {number_list}')

largest_number = number_list[0]
smallest_number = number_list[0]

for n in number_list:
    if n > largest_number:
        largest_number = n
    if n < smallest_number:
        smallest_number = n

print(f'The largest number is: {largest_number}')
print(f'The largest number is: {smallest_number}')
