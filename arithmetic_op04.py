#Create a variable called 'number' and assign it the three-digit number.
number = 437
#Find the 'number' first digit and assign to x1.
x1 = 7
#Find the 'number' second digit and assign to x2.
x2 = 3
#Find the 'number' third digit and assign to x3.
x3 = 4
#Create a variable called 'answer' and assign it the sum of the three digits.
x1 = number%10
x2 = number//10%10 
x3 = number//100 
answer =(x1+x2+x3)
#print the sum of the three digits.
print(answer)