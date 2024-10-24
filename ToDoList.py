from tabulate import tabulate  # Importing the tabulate function from the tabulate module

def main():
    tasks_list = []  # Initializing an empty list to store tasks
    while True:  # Infinite loop to keep the program running until the user decides to exit
        print("choice")  # Printing a choice message
        choice = [
            [1, "To Add task"],  # Option to add a task
            [2, "To display task"],  # Option to display tasks
            [3, "To mark task done"],  # Option to mark a task as done
            [4, "exit..."]  # Option to exit the program
        ]
        header = ["S.no", "Functions"]  # Headers for the tabulated choice display
        print(tabulate(choice, headers=header, tablefmt="grid"))  # Printing the choices in a grid format using tabulate
        ch = input("enter your choice :")  # Asking the user to enter their choice
        if ch == "1":  # If the user chooses to add a task
            print()
            tasks = int(input("How many tasks do you want to add: "))  # Asking the user for the number of tasks to add
            for i in range(tasks):  # Looping through the number of tasks to add
                task = input("Enter the task: ")  # Asking the user to enter the task
                tasks_list.append({"task": task, "done": False})  # Adding the task to the list with "done" status set to False
                print("Task added!")  # Confirming the task has been added
        elif ch == '2':  # If the user chooses to display tasks
            print("\nTasks:")
            for index, task in enumerate(tasks_list):  # Looping through the tasks list
                status = "Done" if task["done"] else "Not Done"  # Checking if the task is done or not
                print(f"{index + 1}. {task['task']} - {status}")  # Printing the task number, task description, and status
        elif ch == '3':  # If the user chooses to mark a task as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1  # Asking the user for the task number to mark as done
            if 0 <= task_index < len(tasks_list):  # Checking if the entered task number is valid
                tasks_list[task_index]["done"] = True  # Marking the task as done
                print("Task marked as done!")  # Confirming the task has been marked as done
            else:
                print("Invalid task number.")  # Informing the user if the entered task number is invalid
        elif ch == '4':  # If the user chooses to exit
            print("Exiting the To-Do List.")  # Printing an exit message
            break  # Exiting the loop to end the program
        else:
            print("Invalid choice. Please try again.")  # Informing the user if they entered an invalid choice

if __name__ == "__main__":  # Checking if the script is being run directly
    main()  # Calling the main function to start the program
