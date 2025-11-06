contacts = { "Mom": "555-1234", "Dad": "555-5678", "Friend": "555-9012" }

print(contacts)

contacts["Brother"] = "555-4444"

print(contacts)

contact_list = list(contacts)

print("\n===Here are all the contacts====")

for name, number in contacts.items():

    print(f"{name}: {number}")
    
userInput = str(input("Whose contact are you looking for: "))

for i in contacts:
    match userInput:
        case "Mom":
            print(f"{contact_list[0]}:", contacts["Mom"])
            break
        case "Dad":
            print(f"{contact_list[1]}:", contacts["Dad"])
            break
        case "Friend":
            print(f"{contact_list[2]}:", contacts["Friend"])
            break
        case "Brother":
            print(f"{contact_list[3]}:", contacts["Brother"])
            break


