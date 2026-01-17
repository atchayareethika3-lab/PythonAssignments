number_1=float(input("Enter a number:"))
number_2=float(input("Enter another number:"))
operation= str(input('Enter the operation to perform:add/sub/mul/div'))

add=number_1 + number_2
sub=number_1 - number_2
mul=number_1 * number_2
div=number_1 / number_2

if operation == 'add':
    print(add)
elif operation == 'sub':
    print(sub)
elif operation == 'mul':
    print(mul)
elif operation == 'div':
    print(div)
else :
    print('invalid input ')