# from datetime import date

# name = "Ryan Noah"
# todaysDate = date.today()

# with open("user_info.txt", mode="w") as Filer:
#     Filer.write(f"Name: {name}\nDate: {todaysDate}")


# with open("Data.txt", mode="w") as Fwrite:
#     Fwrite.write("These are alot of important passwords\n\n1214151\n14515141ff1\njahadhfadgha\nasfd1er1431")

# with open("Data.txt", mode="r") as rword:
#     variable = rword.read()

# print(variable)


# try:
#     with open('students.txt', 'r') as f:
#         s = f.read()
#     print(s)

# except:
#     print("students.txt doesnt exist")

#     #create the file if it doesnt exit

#     with open('students.txt', 'w') as w:
#         w.write("Hello i am student one\n")
#         w.write("Hello i am student two\n")

#     #re open the file

#     with open('students.txt', 'r') as f:
#         s = f.read()
#     print(s)

# #display the file contents

# print()


# x = []

# for i in range (1,11):
#     x.append(i)

# x.append(15)
# del x[0]
# x.pop()
# x.reverse()
# print(x)

cities = ('Nairobi', 'Dubai', 'Ajman', 'New York', 'Ohio')

print(cities[2])

new_cities = ('juba', 'Shanghai')

print(cities + new_cities)

all_cities = list(cities + new_cities)

print(all_cities)


