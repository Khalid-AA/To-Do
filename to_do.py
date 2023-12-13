import os
from datetime import datetime

to_do = {}
to_do_b4_changes = {}

def add_task(name, due_date):
    if name in to_do:
        option = input(f"The task '{name}' already exist. \
            \nDO YOU WANT TO REPLACE THE DUE DATE FOR THE TASK '{name}' (Y/N): ").strip().title()
        if option == "Y" or option == "Yes":
            to_do[name] = due_date
            print(f"Task updated:{name} Due date: {due_date}")
            save_task(to_do)
        elif option == "N" or option == "No":
            print(f"Task unchanged:{name} Due date: {to_do[name]}")
        else:
            print("Invalid option...")
    else:
        to_do[name] = due_date
        print(f"New task added:{name}  Due date {due_date}")
        
        
def view_task():
    load_to_do_file()
    if not to_do:
        print("You have no tasks.")
    else:
        for key in to_do:
            print(f"TASK: {key}  DUE DATE: {to_do[key]}")


def remove_task(name):
    if name in to_do:
        to_do.pop(name, None)
        print(f"Task:{name} removed.")
    else:
        print(f"Task:{name} not found")
    save_task(to_do)
        
        
def load_to_do_file():
    with open("to_do.txt", "r") as tdr:
        while True:
            line = tdr.readline()
            if line == "":
                break
            else:
                name, due_date = line.split()
                to_do[name] = due_date
        
        
def save_task(dict_name):
    with open("to_do.txt", "w") as tdw:                
        for task in dict_name:
            tdw.write(f"{task} {dict_name[task]}\n")
            
            
def previous_version_to_do():
    file = os.path.exists("to_do.txt")
    if file == False:
        open("to_do.txt", "x")
    with open("to_do.txt", "r") as tdr:
        with open("to_do_pr_ver.txt", "w") as tdpvw:  
            while True:
                line = tdr.readline()
                if line == "":
                    break
                else:
                    tdpvw.write(line)
    with open("to_do_pr_ver.txt", "r") as tdpvr:
        for _line in tdpvr.readlines():
            _name, _due_date = _line.split()
            to_do_b4_changes[_name] = _due_date
    

def dont_save_changes():                  
    with open("to_do.txt", "w") as tdw:                
        for task in to_do_b4_changes:
            tdw.write(f"{task} {to_do_b4_changes[task]}\n")


def edit_task(name):
    try:
        new_to_do = {}
        while True:
            edit = int(input("Do you want to edit: \
                \n1. Name. \
                    \n2. Due Date. \
                        \n3. Exit.\n"))
            if edit == 1:        
                new_name = input("Enter the new name: ")
                value = to_do[name]
                new_to_do[new_name] = value
                print(f"Task: {name} updated to {new_name}")
                update_to_do = {**to_do, **new_to_do}
                update_to_do.pop(name)
                to_do.pop(name)
                print()
                #to_do = update_to_do
                #update_to_do.pop(name, None)
                #update_to_do_new = update_to_do
                #print(update_to_do)
                #remove_task(name)
                save_task(update_to_do)
                break
            elif edit == 2:
                while True:
                    new_due_date = input("Enter new due date in the format YYYY-MM-DD: ")
                    date_str = new_due_date
                    try:
                        user_date = datetime.strptime(date_str, "%Y-%m-%d")
                        new_due_date = user_date.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        print("Incorrect format. Please enter the date in the format YYYY-MM-DD.")
                if name in to_do:
                    to_do[name] = new_due_date
                    print(f"{name}'s due date updated to {new_due_date}")
                    save_task(to_do)
                break
            elif edit == 3:
                break
            else:
                print("Invalid input.")
    except ValueError:
        print("Invalid input entered, choose either 1 or 2.")
                
def sort_task():
    sorted_tasks = sorted(to_do.items(), key=lambda item: datetime.strptime(item[1], "%Y-%m-%d"))
    s = dict(sorted_tasks)
    for key in s:
        print(f"{key}  {s[key]}")


def mark_complete():
    complete = to_do.copy()
    if not complete:
        print("No tasks available.")
    else:
        for j in complete:
            mark = input(f"Have you completed {j}, (Y/N): ").strip().title()
            if mark == "Y" or mark == "Yes":
                complete[j] = [complete[j], "Completed"]
            elif mark == "N" or mark == "No":
                complete[j] = [complete[j], "Not Completed"]
            else:
                print("Invalid option. Choose Y or N")
        with open("completed.txt", "w") as cw:
            with open("uncompleted.txt", "w") as uw:
                for i in complete:
                    if complete[i][1] == "Completed":
                        cw.write(f"{i} {complete[i][0]} {complete[i][1]}\n")
                    elif complete[i][1] == "Not Completed":
                        uw.write(f"{i} {complete[i][0]} {complete[i][1]}\n")
        

def check_if_complete():
    try:
        check = int(input("Do you want to check: \
            \n1. Completed Tasks. \
                \n2. Uncompleted Tasks. \n"))
        if check == 1:
            complete_file = os.path.exists("completed.txt")
            if complete_file == False:
                print("No task marked as complete.")
            else:
                with open("completed.txt", "r") as cr:
                    check_complete_empty = cr.read()
                    if check_complete_empty == "":
                        print("No task marked as complete.")
                    else:
                        with open("completed.txt", "r") as cr:
                            for line_cr in cr.readlines():
                                name_, due_date_, complete_ = line_cr.split()
                                print(f"{name_} {due_date_} {complete_}")
        elif  check == 2:
            uncomplete_file = os.path.exists("uncompleted.txt")
            if uncomplete_file == False:
                print("No task marked as uncomplete.")
            else:
                with open("uncompleted.txt", "r") as ur:
                    check_uncomplete_empty = ur.read()
                    if check_uncomplete_empty == "":
                        print("No task marked as uncomplete.")
                    else:
                        with open("uncompleted.txt", "r") as ur:
                            for line_ur in ur.readlines():
                                name__, due_date__, uncompleted__ = line_ur.split()
                                print(f"{name__} {uncompleted__} has due date of {due_date__}")
        else:
            print("Invalid input. Choose 1 or 2")
    except ValueError:
        print("Invalid input. Choose 1 or 2")
        


while True:
    try:
        previous_version_to_do()
        load_to_do_file()
        menu = int(input("\n======MENU====== \
            \n1. Add task. \
                \n2. View task. \
                    \n3. Remove task. \
                        \n4. Sort task (by Due Date). \
                            \n5. Edit task. \
                                \n6. Mark Tasks Complete. \
                                    \n7. Check Task Status. \
                                        \n8. Quit.\n\n>>"))
        if menu == 1:
            name = input("Enter the task name: ")
            while True:
                due_date = input("Enter due date in the format YYYY-MM-DD: ")
                date_str = due_date
                try:
                    user_date = datetime.strptime(date_str, "%Y-%m-%d")
                    due_date = user_date.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Incorrect format. Please enter the date in the format YYYY-MM-DD.")
            add_task(name, due_date)
        
        elif menu == 2:
            view_task()
        
        elif menu == 3:
            rm_name = input("Enter the task to remove: ")
            remove_task(rm_name)
        
        elif menu == 4:
            if not to_do:
                print("No tasks to sort.")
            sort_task()
            
        elif menu == 5:
            if not to_do:
                print("No tasks to edit.")
            else:
                while True:
                    name = input("Enter task name: ")
                    if name in to_do:
                        edit_task(name)
                        break
                    else:
                        print(f"{name} not found")
        
        elif menu == 6:
            mark_complete()
            
        elif menu == 7:
            check_if_complete()
        
        elif menu == 8:
            if to_do == to_do_b4_changes:
                break
            else:
                while True:
                    save_changes = input("Would you like to save changes (Y/N): ").strip().title()
                    if save_changes == "Y" or save_changes == "Yes":
                        save_task(to_do)
                        print("Tasks changes saved succefully.")
                        break
                    elif save_changes == "N" or save_changes == "No":
                        dont_save_changes()
                        print("Tasks changes not saved.")
                        break
                    else:
                        print("Invalid option. Choose Y or N")
                break
        
        else:
            print("Invalid input entered, choose from the menu.")

    except ValueError:
        print("Invalid input entered, choose from the menu.....")
