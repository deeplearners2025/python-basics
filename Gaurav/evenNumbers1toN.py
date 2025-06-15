n = int(input("Enter the number to print the Range to:"))

print(f"Printing Even numbers from 1 to {n}")
for i in range(1,n+1):
    # Method 1 using if
    if i%2 == 0:
        print(i)
    # Method 2 using lambda function
    evenNumber=(lambda i:i%2==0)
    if evenNumber(i):
        print(i)
