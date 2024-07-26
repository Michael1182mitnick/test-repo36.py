# Write a Python program to find the sum of the digits of a given number.

number = int(input("Enter a number: "))
sumvar = 0

# To get the the sum of the digits of a given number.
# using while loop
while(number > 0):
    rem_der = number % 10
    sumvar += rem_der           # using augmented operator
    number = number // 10

print(f"The Sum of given number","is", str(sumvar))