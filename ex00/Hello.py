ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"} # similar to an object in javascript, a dictionary is a collection of key-value pairs.

#your code here

ft_list[1] = " World!"
# re-assigned to point to a new tuple since tuples are immutable.
ft_tuple = (ft_tuple[0], " Morocco!")
# set are mutable but do not support indexing, so we cannot assign a value to a specific index. Instead, we can remove an element and add a new one.
ft_set.remove("tutu!")
ft_set.add(" Benguerir!")
# dictionaries are mutable, so we can assign a new value to an existing key.
ft_dict["Hello"] = " 1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# print ({"Hello", "tutu!"} == {"tutu!", "Hello"}) # True, sets are unordered collections of unique elements, so the order of the elements does not matter.