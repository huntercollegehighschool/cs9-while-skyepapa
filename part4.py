'''
***PART 4***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program calculate the product of all of the entered numbers and prints the product.

Example of what should appear when this part runs:

Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 3
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 0
Product: 60

'''
fact1 = int(input("Enter a number or 0 to stop: "))
fact2 = int(input("Enter a number or 0 to stop: "))
product = fact1 * fact2

fact1 = int(input("Enter a number or 0 to stop: "))

while fact1 != 0:
  product = product * fact1
  fact1 = int(input("Enter a number or 0 to stop: "))

print("Product: " + str(product))
