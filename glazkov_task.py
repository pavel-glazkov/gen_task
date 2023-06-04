#Write a Python program that iterates the integers from 1 to 50
#For multiples of three print "Fizz" instead of the number and 
#for multiples of five print "Buzz". 
#For numbers that are multiples of three and five, print "FizzBuzz"

current = ''
for num in range(1,51):
    if num % 3 == 0:
        current = 'Fizz'
    if num % 5 == 0:
        current = current + 'Buzz'
    if not current:
        current = num
    print(current)
    current = ''
