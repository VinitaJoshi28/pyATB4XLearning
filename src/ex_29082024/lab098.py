my_list=[1, 8, 1,0]
print(my_list)
my_list[2]=77
print(my_list)

my_tuple=(66,55,44)  #tuple is collection of items
print(my_tuple)
#tuple[2] =33    not possible to assign anew value
print(my_tuple)

shopping_list=["milk", "paneer", "sugar"]
shopping_list[2]="curd"
shopping_list.append("salt")
print(shopping_list)

#real world when list doesnt change use tuple

my_tuple=("sdet.club", "tta.com")
print(my_tuple)
print(type(my_tuple))
t=[my_tuple]
print(t)
print(type(t))
print(("********"))
tu=[("sdet.club", "tta.com")]
print(tu)


hero1 =("superman", "batman")
hero2=("wondergirl", "supergirl")
new_tuple=hero1,hero2
print(new_tuple)
print(new_tuple[1][1])
