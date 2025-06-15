n = int(input("Enter the number to print the Range to:"))

print(f"Printing Even numbers from 1 to {n}")
for i in range(1,n):
    if i%2 == 0:
        print(i)
