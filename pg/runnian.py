#!/usr/bin/python3

input("sddss")
list_result= []
for item in range(1970,2051):
    if item % 4==0 and item % 100 != 0 or item % 400 == 0:
        list_result.append(item)
print(list_result)