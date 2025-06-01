
#Approach 1 : Brute force method
def merge_string_alternatively_brute_force(first_str, second_str):
    merged_str=""
    first_str_len=len(first_str)
    second_str_len=len(second_str)
    min_len=min(first_str_len,second_str_len)
    for x in range(min_len):
        chr1=first_str[x]
        chr2 = second_str[x]
        merged_str+=chr1+chr2
    left_out_str1 = first_str[second_str_len:]
    left_out_str2 = second_str[first_str_len:]
    merged_str+=left_out_str1+left_out_str2
    return merged_str

#Approach 2 : Optimized using zip function
def merge_string_alternatively(first_str, second_str):
    #CASE 1 : first_str="abcd", second_str="xy"
    #Case 2 : first_str="ab", second_str="wxyz"

    #Create an empty list
    merged_list=[]
    first_str_len=len(first_str)
    second_str_len=len(second_str)

    #Multi assignment with for loop over zip function
    for ch1,ch2 in zip(first_str, second_str):
        merged_list.append(ch1+ch2)
    left_out_str1 = first_str[second_str_len:]
    left_out_str2 = second_str[first_str_len:]
    # If both String lengths are equal no left out
    # If both String lengths are not equal, only longer string will have left out
    merged_list.append(left_out_str1+left_out_str2)
    #Join the elements of list to form a String
    return "".join(merged_list)


str1=input("Enter first String : ")
str2=input("Enter second String : ")

result=merge_string_alternatively_brute_force(str1,str2)
print(f"(Brute Force) Approach 1 - Merged Strings  are : {result}")

result=merge_string_alternatively(str1,str2)
print(f"(Optimised) Approach 2 - Merged Strings  are : {result}")
