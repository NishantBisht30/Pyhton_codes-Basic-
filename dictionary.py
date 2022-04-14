# dictionary : is key value pairs

d1 = {"Ashish":"Burger", "abhay":"bakri","rohit":"chawal","Rohita":{"breakfast":"maggi","lunch":"chawal","dinner":"roti"}}

'''
print(d1)
print(d1["Ashish"])
print(d1["abhay"])
print(d1["Rohita"])
print(d1["Rohita"]["breakfast"])
# adding new one
d1["Ankit"]="junk food"
print(d1)
del d1["Ankit"]
print(d1)
'''

# some functions of dictionary
# copy

# d3 = d1     # ye d3 naam ki nayi dictionary hi bnarhi ha ,ye(d3) bss ek pointer ha jo ki iss dictionary ko point krra ha and d1 bhi ek pointer hajo khud ko point krraha
#
# print(d3)
# del d3["Ashish"]
# print(d1)  # d1 se bhi delete hogya therefore
# d1.copy()       #pehele d1 ki copy bana lo

print(d1["Ashish"])
print(d1.get("Ashish"))
d1.update({"ashisha": "tofee"})
print(d1)
print(d1.keys())
print(d1.items())
