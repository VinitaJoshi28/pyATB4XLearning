#lambda expression --it is a anonymous function that returns some form of data

def triple_me(num):
 return num**3

output= triple_me(10)
print(output)


output=lambda num: num**3
print(output(10))


output=lambda a,b:a+b
print(output(10,20))

output=lambda num: num**2
print(output(4))




