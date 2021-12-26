name = input('Enter your name: ')
age = input('Enter your age: ')

if len(name) < 3:
    print('Name is too short. Please input in correct format.')
elif len(name) > 50:
    print('Name is too Long. Please input in correct format.')

else:
    if int(age) > 18:
        print(f'{name} can join PUB...')
    else:
        print(f'{name} needs to wait {18-int(age)} years to join PUB...')
