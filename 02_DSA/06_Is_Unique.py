#Write a funtion is_unique that returns true if no charecters repeat,
#Constraint : Use a dictionary (seen={}), Goal is to achieve O(n) time
'''
The Algorithmm is as follows:
def a function
create seen={}
take input String
Iterate Through string, keep all one time occuring things in a dictionary, while simultaneously checking for repititions.
If replications not found, then it is unique, else not and end the looping there.
'''
s=input("Enter The String")
def is_unique(s):
    seen={}
    for ch in s:
        if ch in seen:
            return False
        seen[ch]=True
    return True

print(is_unique(s))