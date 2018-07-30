my_name = 'Jose'
your_name = input('Enter your name: ')
print('hello, ' + your_name)

age = input('Enter your age: ')
print('You have lived for ' + age * 12 + 'months.')

age = input('Enter your age: ')
age_num = int(age) * 12
print('You lived ' + str(age_num) + ' months')

age = int(input('Enter your age: '))
print('You have lived for ' + str(age * 12) + ' months.')

age = int(input('Enter your age: '))
months = age * 12
print('You have lived for ' + str(months) + ' months')

age = int(input('Enter your age: '))
seconds = age * 365 * 24 * 60 * 60
print('You have lived for ' + str(seconds) + ' seconds')