my_list = [10, 20, 30, 40]
another_list = [50,60,70]
my_list.insert(1,15)
print(my_list)

my_list.extend(another_list)
print(my_list)

del my_list[-1]
print(my_list)
my_list.sort()

print(my_list.index(30))