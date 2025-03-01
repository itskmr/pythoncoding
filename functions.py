# def function():
#     print('hello')

# function()

# def function(name=' ronit'):
#     print('hello' + name)

# # function(' anshika')
# function()

# def function(num1 , num2):
#     return num1+num2

# result = function(2,3)
# print(result*10)


# def function (string1):
#     return 'secret' in string1
       
    
# print(function('meow meow'))


# def function(string1):
#     for i in string1:
#         if(i== 'a' or 'i' or 'e' or 'o' or 'u'):
#             i = 'x'
#     return string1

# print(function('aieou'))       
# Completely wrong yha pe hi index pata karne ke liye enumlate use karte hai 

def function(string1):
    output = list(string1)
    print(output)

    for index,letter in enumerate(string1):
        print(letter , end=" ")
        for vowels in 'aieou':
       
          if letter == vowels:
             output[index] = 'x'
    output = "".join(output)
   
    return output


print(function('aieou'))

print(max(1,5,9))

print(min(0.1 , -9999))