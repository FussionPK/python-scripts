i = 0
nameList = ["Eris", "Denis", "Igor"]

###### FOR + IF ######
print("Printing even indexes with for loop")
for x in nameList:
    if i % 2 == 0:
        print("Current i value\t", i, "\tCurrent loop iteration\t", x)
    i += 1

i = 0
print("\n\nPrinting odd indexes with for loop")
for x in nameList:
    if i % 2 == 1:
        print("Current i value\t", i, "\tCurrent loop iteration\t", x)
    i += 1

###### WHILE + IF ######
print("\n\nPrinting even indexes with while loop")
i = 0
while i < len(nameList):  # Corrected condition
    if i % 2 == 0:
        print("Current i value\t", i, "\tCurrent loop iteration\t", nameList[i])  # Added nameList[i]
    i += 1

print("\n\nPrinting odd indexes with while loop")
i = 0
while i < len(nameList):
    if i % 2 == 1:
        print("Current i value\t", i, "\tCurrent loop iteration\t", nameList[i])  # Added nameList[i]
    i += 1
