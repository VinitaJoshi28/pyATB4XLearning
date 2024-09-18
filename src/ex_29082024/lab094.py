# list is collection of items

my_list = [1, 9, 7, 0]  # same type of data
print(my_list)

list_2 = ["hi", 7, 3.14]
list_2[2] = "bye"
print(list_2)
print("print list size", len(list_2))

print(list_2[2])
print("value of index->", list_2[2])

print("*********")
my_list = [1, 9, 7, 0]
for element in my_list:
    print(element)

my_list.append(9)
my_list.append(2)
my_list.extend([11,12,13])
my_list.insert(2,3)
print(my_list)

my_list[2]=8  #this replaces the value at 2 index
print(my_list)    #1,9,8,7,0,8,9,2,11,12,13
my_list.remove(1)
print(my_list)

print("******************")
copied_list=my_list.copy()
my_list.clear()
print("list",my_list)
print("copied list",copied_list)
copied_list.sort()
print(copied_list)
copied_list.reverse()
print(copied_list)
#
# for i in range(0, 5):
#     print(i)  # it will give you a list from 1-9
