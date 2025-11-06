# import random

# #functions

# addition = lambda x, y: x + y
# subtraction = lambda x, y: x - y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y
# exponent = lambda base, exponent: base ** exponent
# reminder = lambda x, y: x % y
 
# #loop the calculations from user input

# Loop = True
# score = 0
# while(Loop):

#     print('''\nWhat operation would you like to try?
#         1:Addition
#         2:Subtraction
#         3:Multiplication
#         4:Division
#         5:Exponent
#         6:Reminder''')
    
#     #take user input for type of calculation

#     userInput = str(input("Please select a number from 1 -6: "))

#     #get your random numbers

#     num1 = random.randint(0,9)
#     num2 = random.randint(0,9)


#     match userInput:
#         case '1':
#             print(f"what is addition of {num1} and {num2} ")
#             result = float(input())
#             if result == addition(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")
#             else:
#                 print("Wrong")

#             pause = str(input("do you want to continue? y or n: "))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")

#         case '2':
#             print(f"what is subtraction of {num1} and {num2} ")
#             result = float(input())
#             if result == subtraction(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")
#             else:
#                 print("Wrong")

#             pause = str(input("do you want to continue? y or n: "))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")
            
#         case '3':
#             print(f"what is the multiplication of {num1} and {num2} ")
#             result = float(input())
#             if result == multiplication(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")
#             else:
#                 print("Wrong")

#             pause = str(input("do you want to continue? y or n: "))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")
            
#         case '4':
#             print(f"what is the division of {num1} and {num2} ")
#             result = float(input())
#             if result == division(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")
#             elif division(num1,num2) == num1 / 0 or 0 / num2:
#                 print("invalid division operator")
#             else:
#                 print("Wrong")
#                 print(result)

#             pause = str(input("do you want to continue? y or n: "))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")
            
#         case '5':
#             print(f"what is the exponent calculation of {num1} and {num2} ")
#             result = float(input())
#             if result == exponent(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")
#             else:
#                 print("Wrong")
#                 print(result)

#             pause = str(input("do you want to continue? y or n: "))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")
            
#         case '6':
#             print(f"what is the reminder of the calculation of {num1} and {num2} ")
#             result = float(input())
#             if result == reminder(num1,num2):
#                 print("Correct")
#                 score += 1
#                 print(f"your current score is {score} ")

#             elif result == 0:
#                 print("Error") 
#             else:
#                 print("Wrong")
#                 print(result)

#             pause = str(input("do you want to continue y or n"))

#             if pause == "y":
#                 print("\ngoing on...")
#             elif pause == "n":
#                 break
#             else:
#                 print("invalid option")
            
        
            

# import threading
# import time

# # Function to be executed in a thread
# def thread_function(name):
#     print(f"Thread {name}: starting")
#     time.sleep(2)  # Simulate a task taking time
#     print(f"Thread {name}: finishing")

# # Creating threads
# threads = []
# for i in range(5):
#     thread = threading.Thread(target=thread_function, args=(i,))
#     threads.append(thread)
#     thread.start()  # Start the thread

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print("All threads complete.")


import subprocess
import os
import threading

# Define the path to your VBS scripts
vbs_folder = r"C:\Users\Fussion\Desktop\MyPython\Threads"  # Change this to your actual path

# List of VBS scripts to run
vbs_scripts = [
    "hello.vbs",
    "info.vbs",
    "processes.vbs"
]

# Function to run a VBS script
def run_vbs(script_name):
    script_path = os.path.join(vbs_folder, script_name)
    subprocess.run(['wscript.exe', script_path])

if __name__ == "__main__":
    threads = []

    # Create a thread for each VBS script
    for script in vbs_scripts:
        thread = threading.Thread(target=run_vbs, args=(script,))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All scripts have completed.")

