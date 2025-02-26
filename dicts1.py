# # dict1 = {'k1':10 , 'k2':20 , 'k3':30 , 'k4':40 }
# # print(dict1.keys())
# # print(dict1.values())
# # print(dict1.items())
# # print(dict1['k3'])

# dict1 = {'k1': [10 , 20 , 30 ]}
# print(dict1)

# print(dict1['k1'][2])

d3 = {'k1' :  [{'nest_key' : ['this is deep' , ['hello']]}]}

d3['k1'][0]['nest_key'][1] = ' Good Bye'
print(d3)