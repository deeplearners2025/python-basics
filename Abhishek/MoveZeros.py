def move_zeros_at_end(nums):
    l=len(nums)
    i=0
    for j in range(l):
        if(nums[j] !=0):
            #Swapping a zero and a Non zero element
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
    return nums

mylist=[0, 1, 5, 7, 0, 14, 0, 18]
print(f"Input list is : {mylist}")
result=move_zeros_at_end(mylist)
print(f"Output list is : {result}")