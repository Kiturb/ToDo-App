import sys
import pickle


def List():  # function that lists all to-do tasks
    # If there are no tasks
    if not LoadTsk:
        print("No todos for today! :)")
        # If tasks are present, display the tasks
    else:
        for task in LoadTsk:
            Index = str(LoadTsk.index(task) + 1)
            if task[1]:  # When task is completed
                print(Index + " - [X] " + task[0])
            else:  # When task is not completed
                print(Index + " - [ ] " + task[0])


def Add():  # function that adds a new task in to-do list
    try:
        Description = sys.argv[2]  # Checks for task description
        LoadTsk.append([Description, False])  # Adds task to the list and saving to file
        pickle.dump(LoadTsk, open(FileName, 'wb'))  # Rewrites file
    except IndexError:
        print("Unable to add: no task provided")  # In case of no description provided


def Remove():  # function that removes a task in to-do list
    try:
        Number = sys.argv[2]  # points at second task
    except IndexError:
        print("Unable to remove: no index provided")
        exit()
    try:
        LoadTsk.pop(int(Number) - 1)  # Removes second task from list
        pickle.dump(LoadTsk, open(FileName, 'wb'))  # Rewrites file
    except IndexError:
        print("Unable to remove: index is out of bound")
    except ValueError:
        print("Unable to remove: index is not a number")


def Complete():  # function that checks a task
    try:
        Number = sys.argv[2]  # Task number to be checked
    except IndexError:
        print("Unable to remove: no index provided")
        exit()
    try:
        Number = int(Number) - 1
        LoadTsk[Number][1] = True
        pickle.dump(LoadTsk, open(FileName, 'wb'))
    except IndexError:
        print("Unable to remove: index is out of bound")
    except ValueError:
        print("Unable to remove: index is not a number")


try:
    FileName = "tasks.txt"
    # Open file
    TasksFile = open(FileName, 'rb')
    # Load the tasks and their Done status:[['Task Description',status(True/False)],.....]
    LoadTsk = pickle.load(TasksFile)
except EOFError:
    LoadTsk = []

if len(sys.argv) == 1:  # when application is run without any arguments
    # displays usage info.
    print("""Command Line Todo application
    =============================

    Command-line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes a task
        -c   Completes a task
    """)
else:
    switch = {"-a": Add, "-l": List, "-r": Remove, "-c": Complete}
    switch.get(sys.argv[1], "Unsupported argument")()
