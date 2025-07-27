'''
Sets are unique collection of elments does not have any index and are used for fatser lookups
Set operations like intersection and union
Very very Useful
'''
'''
fruits = {"apple", "banana", "orange", "mango"}
fruits.add("Litchi")
fruits.remove("banana")

if "mango" in fruits:
    print("yes!!")

    more_fruits = {"Kiwi", "Rasphberry", "blueberries"}
    all_fruits = fruits.union(more_fruits)
    print(all_fruits)

    students_1 = {"akash", "riya", "sneha", "vivek"}
    students_2 = {"akash", "manoj", "vivek", "Tiwari"}

    common_students = students_1.intersection(students_2)
    print("Common Students Name", common_students)
'''







'''
------------Question ---------------
'''
name_1= {"akash", "riya", "sneha", "vivek","noobu"}
name_2 = {"akash", "manoj", "vivek", "Tiwari"}
all_names = name_1.intersection(name_2)
if "skye" in all_names:
    print("Yesss!!!")
    print("required names are", all_names)
