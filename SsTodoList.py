from prettytable import PrettyTable

print("\n*** My TO-DO List. ***")

instructions = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to check your TO-DO."
print(instructions)

my_todo_list = []

x = PrettyTable()

def my_list():
    x.field_names = ["Item Names"]
    for i in my_todo_list:
        x.add_row([i])
    print(x.get_string(title="TO DO List"))
    x.clear_rows()

def add_todo():
    new_todo = input("\nEnter your new TO DO: ").lower()
    print(f"\nYour current TO DO is {new_todo}.")
    my_todo_list.append(new_todo)

def delete_todo():
    while True:
        item_name = input("\nEnter the item you want to delete: ").lower()
        try:
            if item_name in my_todo_list:
                choice = input(f"Are you sure to delete {item_name} from your TODO list? (Y/N): ").lower()
                if choice == "y":
                    my_todo_list.remove(item_name)
                    print("Your updated TO-DO List:")
                    my_list()
                    break
                else:
                    print("Item not deleted.")
            else:
                print("Item not found.")
        except Exception:
            print("Something went wrong.")

def update_todo():
    while True:
        item_name = input("\nEnter the item you want to update: ").lower()
        try:
            if item_name in my_todo_list:
                choice = input(f"Are you sure to update {item_name} from your TODO list? (Y/N): ").lower()
                if choice == "y":
                    update_item = input(f"Enter a name you want to update {item_name} with: ").lower()
                    index = my_todo_list.index(item_name)
                    my_todo_list[index] = update_item
                    print("Your updated TO-DO List:")
                    my_list()
                    break
                else:
                    print("Item not updated.")
            else:
                print("Item not found.")
        except Exception:
            print("Something went wrong.")

def exit_program():
    ask_user = input("\nAre you sure you want to exit? (Y/N): ").lower()
    if ask_user == "y":
        return True
    return False

def process_input(user_input):
    switch = {
        "a": add_todo,
        "d": delete_todo,
        "u": update_todo,
        "e": exit_program,
        "l": my_list,
        "": lambda: print("Please enter something."),
    }
    return switch.get(user_input, lambda: print("Enter a valid value."))()

running = True
while running:
    user_input = input("\nWhat do you want to do? (A,D,U,E,L): ").lower()
    running = not process_input(user_input)