#Check if a list contains any duplicates
'''
def contains_duplicate(nums):
    # Loop through each element
    for i in range(len(nums)):
        # Compare with elements after it
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
'''
#The Better Way
def contains_duplicate(nums):
    seen={}
    for num in nums:
        if num in seen:
            print('Duplcates are:', num)
            return True
        else:
            seen[num]="Can be Anything"
    return False