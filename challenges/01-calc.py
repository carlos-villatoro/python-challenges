# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What calculation would you like to do? (add, sub, mult, div) ')
print('okay, lets ' + operator)
num1 = input('What is number 1? ')
num1 = int(num1)
num2 = input(f'okay we have: {num1}, whats number 2? ')
num2 = int(num2)

if (operator == 'add'):
    print ('your result is', num1 + num2)
elif (operator == 'sub'):
    print ('your result is', num1 - num2)
elif (operator == 'mult'):
    print ('your result is', num1 * num2)
elif (operator == 'div'):
    print ('your result is', num1 / num2)
else:
    print('that is not a valid operator')