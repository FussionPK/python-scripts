try:
    with open("clothing_stock.txt", "r") as fread:
        var = fread.readlines()

        print(len(var))

    unique = set(var)

    for i in unique:
        if  "XS" |  "XXL" | "S" | "L" | "M" in i:
            print(len(i))
        
except:
    print("Execution Error")