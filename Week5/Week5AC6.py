try:
    Grades = {'Alice':85,"Bob":92,'Charlie':78}

    print("Before Update: ", Grades, "\n")

    Grades["Diana"] = 88

    Grades['Bob'] = 95

    print("Updated Dictionary: ",Grades, "\n")

    numbers = Grades.values()


    print("Below are the grades above 80: ")

    for i in numbers:
       if i > 80:
        print(f"Grade {i}\n")
    
    grade_count = len(Grades.values())

    print("The number of grades presented are: ", grade_count, "\n")
    
    total = sum(Grades.values())

    print("The Total of all grades combined is: ", total, "\n") 

    avg = total/grade_count

    print("By doing the sum of all grades divided by the number of grades the average is: ", avg, "\n")

    
except:
 print("Execution Error")