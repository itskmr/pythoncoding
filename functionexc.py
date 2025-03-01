# # def sum( a , b):
# #     if a + b == 10:
# #         return True
# #     else:
# #         return False

# # def sum( a , b):
# #     return a + b == 10
       
    
# # print(sum(2,3))

# # def sum( a , b):
# #     if a + b == 10:
# #         return True
# #     else:
# #         return a+b
    
# # print(sum(2,3))

# # take a string and bs 1st character upper case mai return karna hai  

# # def function (mystring):
# #     
# #      i[0] = i[0].upper()
# #      return mystring

# # print(function('aieou'))

# # mystring = 'aieou'
# # # mystring  = mystring.upper()
# # print(mystring[0].upper())




# def function (mystring):
#     return mystring[0].upper() + mystring[1:]

# print (function("aieou"))

# def function (str1):
#     if len(str1) < 2:
#         return "ERROR"
#     else:
#         str1 = (str1[:-3:-1])
#         return str1


# print(function("abcd"))


# integers ki list mai agar 1 , 2 ,3 sequence mai mile so retun True 

# def function(list_elements):
#     for i in range(len(list_elements) - 2):
#         if list_elements[i] == 1 and list_elements[i + 1] == 2 and list_elements[i + 2] == 3:
#             return True
#     return False

# # Correct way to call the function
# print(function([1, 2, 3, 4, 5]))  # Output: True
# print(function([4, 5, 6, 1, 2, 3]))  # Output: True
# print(function([7, 8, 9]))  # Output: False


# def function (str1 , str2):
    # len_str1 = len(str1)
    # len_str2 = len(str2)

    # if len_str1 > len_str2:
    #     return len_str1 - len_str2
    # else:
    #     return 0 

#     return abs(len(str1) - len(str2))
    
# print(function('Hello' , 'Meowbaka'))


#  Ek list given hai if uski len even hai so return sum and odd hai so return the max

def function (list1):
    if len(list1) % 2 == 0 :
        return sum(list1)
    else:
        return max(list1)
    
print(function([1 , 2, 3 , 4 , 5]))