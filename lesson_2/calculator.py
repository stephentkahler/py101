# Ask the user for the first number.
# Ask the user for the second number.
# Ask teh user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

#ask the user for the first number
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    print("Hmm... that doesn't look like a valid number")
    number1 = input()

#ask the user for the second number
prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    print("Hmm... that doesn't look like a valid number")
    number2 = input()

#print(f'{number1} {number2}')

prompt("""What operation would you like to peform?
1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()


while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3 or 4')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f"The result is: {output}")