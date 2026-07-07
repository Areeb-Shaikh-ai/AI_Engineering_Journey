#Traverse, Insert, Delete, Search 
arr=[10,30,15,20,25]

#Traverse
for item in arr:
    print(item)

#Time complexity is linear, O(n) as the algorithm visits every element exactly once.

#Insert:
x=int(input ('Enter Element to be Inserted '))
z=int(input('Enter Position to be Inserted'))
arr.insert(z,x)
#arr.append(x)
print(arr)

#Time Complexity is constant for arr.append, O(1) as this sentence is executed once, it's logic is to insert the element at the end of the array.
#Time Complexity is linear, O(n) for arr.insert, as this sentence is executed n times, it's logic is to find the position then insert the element.

#Delete:
y=int(input ('Enter Element to be Deleted '))
arr.remove(y)
print(arr)

#Time Complexity is linear, O(n) as this sentence is executed n times, it's logic is to find the element then delete it.
'''Find element
    ↓
Delete it
    ↓
Shift remaining elements'''

#Search:
z=int(input('Enter Element To be Searhed'))
for item in arr:
    if item == z:
        print('Element Found')
else:
    print('Element Not Found')

#Time complexity is linear, O(n) as this sentence executed n times, it's logic is to find the element in the array.
'''Worst case:
Element is at the last position
or not present.
Therefore every element must be checked.'''

#maximum and minimum element in array
largest = arr[0]
smallest = arr[0]
for item in arr:
    if item > largest:
        largest = item
    elif item < smallest:
        smallest = item
print('Largest Element:',largest)
print('Smallest Element:',smallest)


# Continue array fundamentals (insertion/deletion/shifting)
def insert_at_index(arr, index, value):
    # return new array with value inserted at index
    # do NOT use arr.insert()
    if index<0:
        index = len(arr)-1

    if index>len(arr):
        raise IndexError("Index Out of Bounds")
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    new_arr.append(value)
    for i in range(index, len(arr)):
        new_arr.append(arr[i])
    return new_arr
'''Can also be handled easily by list slicing
def insert_at_index(arr, index, value):
    return arr[:index] + [value] + arr[index:]
'''


def delete_at_index(arr, index):
    # return new array with element at index removed
    # do NOT use arr.pop() or del arr[index]
    if index<0:
        index = len(arr)-1

    if index>=len(arr):
        raise IndexError("Index Out of Bounds")
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    for i in range(index+1, len(arr)):
        new_arr.append(arr[i])
    return new_arr
'''  Can also be done like below
def insert_at_index(arr, index):
    return arr[:index] + arr[index+1:]
'''

def remove_all(arr, value):
    # return new array with all occurrences of value removed
    # do NOT use .remove() or list comprehension
    new_arr=[]
    for x in arr:
        if x != value:
            new_arr.append(x)
    return new_arr
#The Time Complexity for this case is linear O(n).