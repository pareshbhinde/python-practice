number = int(input(f"Enter the number to check if its prime or not:"))
    
for i in range(2, number):
    if number % i == 0:
        print (f"{number} is not prime")
    else:
        print (f"{number} is prime")
