import os
from datetime import datetime

to_do = {}
to_do_b4_changes = {}

# Adding tasks to the To Do dictionary.
# If the task already exists ask if due date needs to be changed.
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
  
      
# Check the tasks with their due dates. 
def view_task():
    load_to_do_file() # Retrieving tasks from the to_do.txt file and putting it into the to_do dictionary
    if not to_do:
        print("You have no tasks.")
    else:
        for key in to_do:
            print(f"TASK: {key}  DUE DATE: {to_do[key]}")


# Removing a tasks, if the task doesn't exist inform that the task wasn't fount.
# After the changes, save the tasks in the to_do dictionary.
def remove_task(name):
    if name in to_do:
        to_do.pop(name, None)
        print(f"Task:{name} removed.")
    else:
        print(f"Task:{name} not found")
    save_task(to_do)
        

# Reading from the to_do.txt file and then putting the tasks in the to_do dictionary.
def load_to_do_file():
    with open("to_do.txt", "r") as tdr:
        while True:
            line = tdr.readline()
            if line == "":
                break
            else:
                name, due_date = line.split()
                to_do[name] = due_date
        
        
# Tasks a parameter which is the dictionary name then writes what is in the dictionary to to_do.txt file.
def save_task(dict_name):
    with open("to_do.txt", "w") as tdw:                
        for task in dict_name:
            tdw.write(f"{task} {dict_name[task]}\n")
            
       
# Reads from to_do.txt file then write into to_do_pr_ver.txt file to keep track of the tasks b4 any changes.
# Then those tasks are placed into to_do_b4_changes dictionary to enable for comparison between to_do dictionary
# and to_do_b4_changes dictionary to see if changes were made.
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
    

# In case we don't want to save changes, we can go back to the previous state b4 changes.
def dont_save_changes():                  
    with open("to_do.txt", "w") as tdw:                
        for task in to_do_b4_changes:
            tdw.write(f"{task} {to_do_b4_changes[task]}\n")


# Checks if the date is in the right format.
def check_date_format():
    while True:
        due_date = input("Enter due date in the format YYYY-MM-DD: ")
        date_str = due_date
        try:
            user_date = datetime.strptime(date_str, "%Y-%m-%d")
            due_date = user_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Incorrect format. Please enter the date in the format YYYY-MM-DD.") 
    return due_date   
    

# Enables to edit the name of a task or due date of a task.
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
                save_task(update_to_do)
                break
            elif edit == 2:
                new_due_date = check_date_format()
                if name in to_do:
                    to_do[name] = new_due_date
                    print(f"{name}'s due date updated to {new_due_date}")
                    save_task(to_do)
                break
            elif edit == 3:
                break
            else:
                print("Invalid input entered, choose either 1, 2 or 3.")
    except ValueError:
        print("Invalid input.")
             

# Sorts tasks in order of their due dates.
def sort_task():
    sorted_tasks = sorted(to_do.items(), key=lambda item: datetime.strptime(item[1], "%Y-%m-%d"))
    sort = dict(sorted_tasks)
    for key in sort:
        print(f"{key}  {sort[key]}")


# Marking a task to be complete or incomplete.
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
            with open("incomplete.txt", "w") as iw:
                for i in complete:
                    if complete[i][1] == "Completed":
                        cw.write(f"{i} {complete[i][0]} {complete[i][1]}\n")
                    elif complete[i][1] == "Not Completed":
                        iw.write(f"{i} {complete[i][0]} {complete[i][1]}\n")


# Checks the states of tasks whether complete or incomplete.
def check_if_complete():
    while True:
        try:
            user_input = int(input("\nDo you want to check: \
                \n1. Completed Tasks. \
                    \n2. Incomplete Tasks. \
                        \n3. Exit. \n\n>>"))
            if user_input == 1:
                complete_file = os.path.exists("completed.txt")
                if not complete_file:
                    print("No task marked complete.")
                else:
                    with open("completed.txt", "r") as cr:
                        complete_content = cr.read()
                        if not complete_content.strip(): # Check if content is empty.
                            print("No task marked as complete.")
                        else:
                            lines = complete_content.splitlines()
                            for line_cr in lines:
                                name, due_date, complete = line_cr.split()
                                print(f"{name} {due_date} {complete}")
            elif user_input == 2:
                incomplete_file = os.path.exists("incomplete.txt")
                if not incomplete_file:
                    print("No task marked as incomplete.")
                else:
                    with open("incomplete.txt", "r") as ir:
                        incomplete_content = ir.read()
                        if not incomplete_content.strip(): # Check if the content is empty.
                            print("No task marked as incomplete.")
                        else:
                            lines = incomplete_content.splitlines()
                            for line_ir in lines:
                                name_, due_date_, incomplete_ = line_ir.split()
                                print(f"{name_} {due_date_} {incomplete_}")
            elif user_input == 3:
                break
            else:
                print("Invalid input. Choose 1, 2 or 3.") 
        
        except ValueError:
            print("Invalid input. Choose from the menu.")


if __name__ == "__main__":
    print("\n---This file contains the fucntions of To Do list.---\n")