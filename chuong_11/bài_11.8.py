nums=[1,2,3,4,7,5,6,8,9]
def has_lucky_numbers(nums):
    for i in nums:
        if i%7==0:
            print(True)
            break 
    else:
        print(False)
    return
has_lucky_numbers(nums)

            