my_string = "Python Ogreniyorum"
new_string = my_string[5]
print(new_string)
my_new_string = "ProgramlamayaMerhabaDedik"
print(my_new_string[5:8:])
my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
print(my_last_string[::-1])
print(type(4 + 12.2 + 48))
print(5 + 7 * 12)
# 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]
new_list = [1]
new_list0 = [3,"a"]
new_list1 = new_list + new_list0
new_list2 = []
new_list2.append(1)
new_list2.append(3)
new_list2.append("a")
print(new_list1)
print(new_list2)
my_list = [3.14, 4, [2,3,"b"], True]
print(my_list[2][2])
my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
print(my_dictionary["kk2"][1]["k21"])
my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]
print(set(my_list_to_be_set))
x = 30 * 5 + 3
y = 108 - 2 * 4
print(x > y)