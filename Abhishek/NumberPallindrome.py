#Function to Reverse an Integer
def reverse_number(n):
    print("Inside reverse_number")
    reversed_num=0
    #Logic for reversing using modulus and division
    while n>0:
        d=n%10
        reversed_num=reversed_num * 10 + d
        n=n//10

    print(f"Reverse of the number in reverse_number function is : {reversed_num}")
    return reversed_num


#Approach -1 : Check pallindrome using reverse number function
def check_number_pallindrome(n):
    print("Inside check_number_pallindrome")
    #Call the function to reverse the integer
    reversed_num=reverse_number(n)
    if num == reversed_num:
        print(f"Number : {n} is a Pallindrome")
    else:
        print(f"Number : {n} is not a Pallindrome")


#Approach -2 : Shortcut Method Using String
#In this approach we can convert the number to string and do index based slicing to reverse it
def check_pallindrome_with_slicing(n):
  print("Inside check_pallindrome_with_slicing")
  num=str(n)
  reversed_num=num[::-1] # Using string slicing to reverse the number converted to String
  if num==reversed_num:
    print(f"Number : {n} is a Pallindrome")
  else:
    print(f"Number : {n} is not a Pallindrome")

num = int(input("Please enter a number : "))
check_number_pallindrome(num)
check_pallindrome_with_slicing(num)

