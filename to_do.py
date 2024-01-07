import functions as f

# Read the content from to_do.txt file and then write it into to_do_pr_ver.txt file
# Then read the content from to_do_pr_ver.txt file and then write it into to_do_b4_changes dictionary
f.previous_version_to_do()
# Read the content from to_do.txt file and then write it into to_do dictionary
f.load_to_do_file()

while True:
    try:
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
            name = input("Enter the task name(or q to quit): ").title()
            if name == "Q":
                break
            due_date = f.check_date_format()
            f.add_task(name, due_date)
        
        elif menu == 2:
            f.view_task()
        
        elif menu == 3:
            rm_name = input("Enter the task to remove: ")
            f.remove_task(rm_name)
        
        elif menu == 4:
            if not f.to_do:
                print("No tasks to sort.")
            f.sort_task()
            
        elif menu == 5:
            if not f.to_do:
                print("No tasks to edit.")
            else:
                while True:
                    name = input("Enter task name: ")
                    if name in f.to_do:
                        f.edit_task(name)
                        break
                    else:
                        print(f"{name} not found")
        
        elif menu == 6:
            f.mark_complete()
            
        elif menu == 7:
            f.check_if_complete()
        
        elif menu == 8:
            if f.to_do == f.to_do_b4_changes:
                break
            else:
                while True:
                    save_changes = input("Would you like to save changes (Y/N): ").strip().title()
                    if save_changes == "Y" or save_changes == "Yes":
                        f.save_task(f.to_do)
                        print("Tasks changes saved succefully.")
                        break
                    elif save_changes == "N" or save_changes == "No":
                        f.dont_save_changes()
                        print("Tasks changes not saved.")
                        break
                    else:
                        print("Invalid option. Choose Y or N")
                break
        
        else:
            print("Invalid input entered, choose from the menu.")

    except ValueError:
        print("Invalid input entered, choose from the menu.....")
