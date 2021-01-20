# TODO Application

A simple TODO application designed to help keep track of your day-to-day tasks by categorizing task into 4 separate  columns namely 'todo', 'doing', 'review' and 'done'.



## Requirements

- Basic Git and/or Github.



## Installing and Execute

- First install python IDE on your local system

- Then run  `ToDo.py` file in the terminal 

```terminal
-> python ToDo.py
```

- Or run in an IDE
- Give arguments to perform certain task as explained later.



## Description

### Features

The application has four features:

- List tasks
- Add a task
- Remove a task
- Checks for completion of a task

### Libraries Used 

Two libraries used:

```python
import sys
import pickle
```

with command-line interface

### Program Working

#### Loading file

first the file is opened using

```python
FileName="tasks.txt"
TasksFile = open(FileName, 'rb')
```

then data is loaded and mapped to a variable

```python
LoadTsk = pickle.load(TasksFile)
```



Incase of an exception for EOF, it is caught and the variable is declared null

```python
except EOFError:
    LoadTsk = []
```



#### Checking Argument

Incase the application is run without any argument, a list is displayed and user chooses an option amongst them

```terminal
Command Line Todo application
=============================
Command-line arguments:
	-l   Lists all the tasks
	-a   Adds a new task
    	-r   Removes a task
    	-c   Completes a task
```

else the application reads the argument and acts accordingly as shown in above list using a switch statement

```python
switch={"-a": Add, "-l": List, "-r": Remove, "-c": Complete}
switch.get(sys.argv[1], "Unsupported argument")()
```



#### Calling Functions

Depending on the given argument one of the functions is executed 

- #### List Function:

  This function lists all the to-do tasks. 

  ```python
  def List(): #function that lists all to-do tasks
      #If there are no tasks
      if not LoadTsk: 
          print("No todos for today! :)") 
      #If tasks are present, display the tasks
      else :
          for task in LoadTsk:
              Index = str(LoadTsk.index(task)+ 1) 
              if task[1]: # When task is completed
                  print(Index + " - [X] " + task[0])
              else: # When task is not completed 
                  print(Index + " - [ ] " + task[0])
  ```

  If there are no tasks a message is prompted else the list is displayed  with "- [ X ]" and "- [ ]" preceding the done and undone tasks respectively.

- #### Add Function:

  This function adds a new task to our to-do list.

  ```python
  def Add(): #function that adds a new task in to-do list
  	try:
          Description = sys.argv[2]   # Checks for task description
          LoadTsk.append([Description,False]) # Adds task to the list and saving to file
          pickle.dump(LoadTsk, open(filename, 'wb')) # Rewrites file
      except IndexError:
          print("Unable to add: no task provided")    #In case of no description provided
  
  ```

  If the description for the task is not provided a message is prompted else the task is written to the list

  

- #### Remove Function

  This function removes a task in the to-do list

  ```python
  def Remove():   #function that removes a task in to-do list
      try:
          Number = sys.argv[2] #points at second task
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
  ```

  The function checks for out of bound error and displays a message if the is an exception else removes the task on the specified number.

  

- #### Complete Function

  This function checks a task by changing false to true

  ```python
  def Complete(): #function that checks a task 
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
  ```

  The function checks for out of bound error and displays a message if the is an exception else checks the task on the specified number.