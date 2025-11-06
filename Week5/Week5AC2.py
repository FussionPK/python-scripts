try:

    with open("shopping.txt", "w") as fwrite:
        fwrite.write("Apples\n")
        fwrite.write("Bananas\n")
        fwrite.write("Cheese\n")
        fwrite.write("Soap\n")
        fwrite.write("Toothbrush")

    with open("shopping.txt", "r") as fread:
        var = fread.readlines()

        for i in var:
            print(f"you need to buy {i}")

    total = len(var)
    print("\nTotal number of items in shopping cart is: ",total)
        
except:
    print("Execution Error")