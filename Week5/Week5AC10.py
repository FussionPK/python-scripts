try:
    with open("Lab 05-20251022\Les_Brown.txt", "r") as fread:
        for i in fread:
            lines = fread.readline()

            if "dream" and "!" in i:
                with open("possibility.txt", "a") as fadd:
                    upper = fadd.write(i.upper())
                    

except:             
    print("Execution Error")

    #what do you understand from this code above ^^^^