try:
    with open("Lab 05-20251022\Les_Brown.txt", "r") as fread:
        for i in fread:
            lines = fread.readline()

            if "dream" in i :
                with open("dream_sentences.txt", "a") as fadd:
                    fadd.write(i)
except:
    print("Execution Error")