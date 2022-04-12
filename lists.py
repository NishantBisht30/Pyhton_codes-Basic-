'''grocery = ["harpic","vim bar","samosa","deodrant","bhindi"]
print(grocery)
print(grocery[1])
#print(grocery[6])       # will give error
'''
# number = [2,300,49,51,6]


# print(number[1:5:2])
'''
print(number)
number.sort()               # to sort the list , changes the original list
print(number)
number.reverse()          #to reverse the list , changes the original list
print(number)
print(len(number))
print(number[1:5])
print(number[1:5:1])
print(number[1:5:2])
print(number[::-1])  # knive way of revesrsing list
print(min(number))       # for minimum in list
print(max(number))         # for maximum in list

# append

#number.append(7)
#print(number)

#insert function
print(number)
number.insert(1,67)           #( first index ma 67 daal do ) -> will add 67 to 1st index
print(number)

#remove function

number.remove(67)
print(number)

#pop 
number.pop(2)

print(number)
number[1] = 34
print(number)        # value is changed
'''
'''
# but let we don't want to change the value
# mutable(can change) and immutable(can't change)
tp = (1,2,3)         #tuple
#tp[1] = 12       #the vlue of tuple can't be changed
print(tp)

#note : if we want to make tuple of one element
tup = (1,)       # (toh hame ek commma lagana hoga if bracket nhi chahiye to comma mt lagao)->then we have to add a comma if we don't want the bracket 
tep = (1)
print(tep)
print(tup)
'''
#
# #swapping
# a= 3
# b=4
# print(a,b)
# a,b = b,a          # simple way of swapping
# print(a,b)
