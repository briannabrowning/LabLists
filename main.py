# create 3 lists
list_names = ["Brianna", "Alex", "Maeve"]
list_towns = ["Rye", "Portsmouth", "Hampton"]
list_foods = ["Pizza", "Hamburgers", "Sandwiches"]
# prompt user if they want to search for a name
def search_name():
        search_name = input("Would you like to search for a name? y/n ")
        if search_name == "y":
            valid_name = input("Please enter a name: ")
            found_names = []                                   # create an empty list
            for idx, a_name in enumerate(list_names):          # use enumerate to get index and name bc a_name just repsresents the name itself
                if valid_name.lower() in a_name.lower():       # if name is found
                    found_names.append(idx)                    # add its index to found_names

            if found_names:
                print("Names found:")                           # confirm a name was found
                for idx in found_names:                         # searches the associated index
                    print(list_names[idx])                      # print it

                    # ask about hometown and food
                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                    if "hometown" in next_q:
                        print(f"{list_names[idx]} is from {list_towns[idx]}")
                    elif "food" in next_q:
                        print(f"{list_names[idx]}'s favorite food is {list_foods[idx]}")
                    else:
                        print("Invalid choice. Enter 'hometown' or 'favorite food': ").lower()
                    while True:  # loop the re-search
                        another_student = input("Would you like to learn about another student? y/n ")
                        if another_student == "y":
                            search_name = input("Would you like to search for a name? y/n ")
                            if search_name == "y":
                                valid_name = input("Please enter a name: ")
                                found_names = []
                                for idx, a_name in enumerate(
                                        list_names):
                                    if valid_name.lower() in a_name.lower():
                                        found_names.append(idx)

                                if found_names:
                                    print("Names found:")
                                    for idx in found_names:
                                        print(list_names[idx])

                                        # ask about hometown and food
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                                        if "hometown" in next_q:
                                            print(f"{list_names[idx]} is from {list_towns[idx]}")
                                        elif "food" in next_q:
                                            print(f"{list_names[idx]}'s favorite food is {list_foods[idx]}")
                                        else:
                                            print("Invalid choice. Enter 'hometown' or 'favorite food': ").lower()
                            if search_name == "n":
                                need_list = input("Would you like to see a list of names? y/n ")
                                if need_list == "y":
                                    print(", ".join(list_names))  # print list without brackets
                                    name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                    while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                        name = input(f"Please enter a valid number (1-{len(list_names)}): ")
                                    name = int(name) - 1
                                    print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")
                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                    if "hometown" in next_q:
                                        print(f"{list_names[name]} is from {list_towns[name]}")
                                    elif "food" in next_q:
                                        print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                    else:
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                                if need_list == "n":
                                    name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                    while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                        name = input(f"Please enter a valid number (1-{len(list_names)}): ")

                                    name = int(name) - 1  # redefining name to a number and subtract 1 bc the list starts at 0
                                    print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")

                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                    if "hometown" in next_q:
                                        print(f"{list_names[name]} is from {list_towns[name]}")
                                    elif "food" in next_q:
                                        print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                    else:
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                        if another_student == "n":
                            break

        if search_name == "n":
            need_list = input("Would you like to see a list of names? y/n ")
            if need_list == "y":
                print(", ".join(list_names))  # print list without brackets
                name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                    name = input(f"Please enter a valid number (1-{len(list_names)}): ")
                name = int(name) - 1
                print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")
                next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                if "hometown" in next_q:
                    print(f"{list_names[name]} is from {list_towns[name]}")
                elif "food" in next_q:
                    print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                else:
                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                while True:  # loop the re-search
                    another_student = input("Would you like to learn about another student? y/n ")
                    if another_student == "y":
                        search_name = input("Would you like to search for a name? y/n ")
                        if search_name == "y":
                            valid_name = input("Please enter a name: ")
                            found_names = []
                            for idx, a_name in enumerate(
                                    list_names):
                                if valid_name.lower() in a_name.lower():
                                    found_names.append(idx)

                            if found_names:
                                print("Names found:")
                                for idx in found_names:
                                    print(list_names[idx])

                                    # ask about hometown and food
                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                                    if "hometown" in next_q:
                                        print(f"{list_names[idx]} is from {list_towns[idx]}")
                                    elif "food" in next_q:
                                        print(f"{list_names[idx]}'s favorite food is {list_foods[idx]}")
                                    else:
                                        print("Invalid choice. Enter 'hometown' or 'favorite food': ").lower()
                        if search_name == "n":
                            need_list = input("Would you like to see a list of names? y/n ")
                            if need_list == "y":
                                print(", ".join(list_names))  # print list without brackets
                                name = input(
                                    f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                    name = input(f"Please enter a valid number (1-{len(list_names)}): ")
                                name = int(name) - 1
                                print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")
                                next_q = input(
                                    "Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                if "hometown" in next_q:
                                    print(f"{list_names[name]} is from {list_towns[name]}")
                                elif "food" in next_q:
                                    print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                else:
                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                            if need_list == "n":
                                name = input(
                                    f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                    name = input(f"Please enter a valid number (1-{len(list_names)}): ")

                                name = int(
                                    name) - 1  # redefining name to a number and subtract 1 bc the list starts at 0
                                print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")

                                next_q = input(
                                    "Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                if "hometown" in next_q:
                                    print(f"{list_names[name]} is from {list_towns[name]}")
                                elif "food" in next_q:
                                    print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                else:
                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                        if another_student == "n":
                            break

            if need_list == "n":
                name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                while not name.isdigit() or not (0 <= int(name) - 1 < len(
                        list_names)):  # validating that a letter or out of range number wasn't entered
                    name = input(f"Please enter a valid number (1-{len(list_names)}): ")

                name = int(name) - 1  # redefining name to a number and subtract 1 bc the list starts at 0
                print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")

                next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                if "hometown" in next_q:
                    print(f"{list_names[name]} is from {list_towns[name]}")
                elif "food" in next_q:
                    print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                else:
                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()

                    while True:  # loop the re-search
                        another_student = input("Would you like to learn about another student? y/n ")
                        if another_student == "y":
                            search_name = input("Would you like to search for a name? y/n ")
                            if search_name == "y":
                                valid_name = input("Please enter a name: ")
                                found_names = []
                                for idx, a_name in enumerate(
                                        list_names):
                                    if valid_name.lower() in a_name.lower():
                                        found_names.append(idx)

                                if found_names:
                                    print("Names found:")
                                    for idx in found_names:
                                        print(list_names[idx])

                                        # ask about hometown and food
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                                        if "hometown" in next_q:
                                            print(f"{list_names[idx]} is from {list_towns[idx]}")
                                        elif "food" in next_q:
                                            print(f"{list_names[idx]}'s favorite food is {list_foods[idx]}")
                                        else:
                                            print("Invalid choice. Enter 'hometown' or 'favorite food': ").lower()
                            if search_name == "n":
                                need_list = input("Would you like to see a list of names? y/n ")
                                if need_list == "y":
                                    print(", ".join(list_names))  # print list without brackets
                                    name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                    while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                        name = input(f"Please enter a valid number (1-{len(list_names)}): ")
                                    name = int(name) - 1
                                    print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")
                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                    if "hometown" in next_q:
                                        print(f"{list_names[name]} is from {list_towns[name]}")
                                    elif "food" in next_q:
                                        print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                    else:
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                                if need_list == "n":
                                    name = input(f"Which student would you like to learn more about? (1-{len(list_names)}): ")
                                    while not name.isdigit() or not (0 <= int(name) - 1 < len(list_names)):
                                        name = input(f"Please enter a valid number (1-{len(list_names)}): ")

                                    name = int(name) - 1  # redefining name to a number and subtract 1 bc the list starts at 0
                                    print(f"Student {name + 1} is {list_names[name]}. What would you like to know? ")

                                    next_q = input("Enter 'hometown' or 'favorite food': ").lower()  # lower for case sensitivity
                                    if "hometown" in next_q:
                                        print(f"{list_names[name]} is from {list_towns[name]}")
                                    elif "food" in next_q:
                                        print(f"{list_names[name]}'s favorite food is {list_foods[name]}")
                                    else:
                                        next_q = input("Enter 'hometown' or 'favorite food': ").lower()
                        if another_student == "n":
                            break
search_name()
