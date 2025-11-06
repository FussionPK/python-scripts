try:
    with open("Lab 05-20251022\Les_Brown.txt", "r") as fread:

        lines = fread.readlines()

        print(lines)

        lines_length = len(lines)

        print(lines_length)

except:
    print("Execution Error")