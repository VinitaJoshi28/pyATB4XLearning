my_shopping_list = ["bread", "butter", "jam"]


# print(my_shopping_list)

def add_food(list):
    my_shopping_list.append("cheese")
    my_shopping_list.remove("butter")
    my_shopping_list.insert(2, "waffles")
    return list


l = add_food(my_shopping_list)
print(l)


def add_item(mylist):
    new_item = str(input("enter the item"))
    my_shopping_list.insert(2, new_item)
    return mylist


l = add_item(my_shopping_list)
print(l)
