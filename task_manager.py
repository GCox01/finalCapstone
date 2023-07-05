# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]
#creates blank list for tasks
task_list = []

for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
#creates text files if not already in existence
if not os.path.exists("task_overview.txt"):
    with open("task_overview.txt", "w") as default_file:
        pass

if not os.path.exists("user_overview.txt"):
    with open("user_overview.txt", "w") as default_file:
        pass
#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password
#This block of code checks if the user enters in a correct username and password from the text file. 
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

def reg_user(r):
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")
    with open("user.txt", 'r') as new_file:
        lines = new_file.read()
        if new_username in lines:
            while new_username in lines:
                print ("This username already exists. Please try again.")
                new_username = input("New Username: " ) #ensures the username is different to one currently available

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        #adds user to file
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

def add_task(a):
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys(): #ensures user exists in file
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")
    with open("user.txt", 'r') as new_file:
        lines = new_file.read()
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True: #ensures the user enters in the appropriate date in the expected format
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
#Adds the new task to the task list
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all(va):
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling) 
    '''
    #Prints all the tasks currently available
    print("All tasks are: \n")
    for t, task in enumerate(task_list, start=1):
        print(f"{t} . {task['title']}\n")

    for t in task_list:
        disp_str = f"Task: \t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine(vm):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    print("Your tasks are:\n ")
    for t, task in enumerate(task_list, start=1):
        if task['username'] == curr_user: #Checks which tasks belong to the current user
            print(f"{t} . {task['title']}\n")
    #;ets the user choose what to do with their tasks
    user_choice = int(input("Please enter which task you would like, or enter -1 to exit: "))
    task_list_length = len(task_list)
    while user_choice!= -1: #Checks if the user wants to exit
        if user_choice in range(1, task_list_length + 1): #Ensures the task is in the range of the users choices
            task = task_list[user_choice - 1]
            if task['username'] == curr_user: #returns users task and asks what they would like to do
                disp_str = f"Task: \t\t {task['title']}\n"
                disp_str += f"Assigned to: \t {task['username']}\n"
                disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {task['description']}\n"
                print(disp_str)
                edit_task = int(input("Please enter 1 if you would like to edit your task, 2 to mark task complete, or 3 to exit: "))
                while edit_task!= 1 and edit_task!=2 and edit_task!=3: #ensures the user enters an appropriate choice
                    edit_task = int(input("You have not entered a valid option. Please enter 1, 2, or 3: "))
                if edit_task == 1:
                    if task['completed'] == False: #checks the task is not complete and that the user can change it
                        edit_choice = int(input("Please enter 1 to change the username, or 2 for due date: "))
                        while edit_choice != 1 and edit_choice!=2: #checks the users choice is in the list
                            edit_choice = int(input("Incorrect. Please enter 1 to change the username, or 2 for due date: "))
                        if edit_choice == 1: #lets the user change username
                            edit_username = input("Please enter the username you wish to use: ")
                            while edit_username not in username_password.keys():
                                print("User does not exist")
                                edit_username = input("Please enter the username you wish to use: ")
                            task['username'] = edit_username
                        else: #lets the user change the date
                            new_due_date = input("New due date of task (YYYY-MM-DD): ")
                            new_due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            task['due_date'] = new_due_date_time
                    else: #tells the user the task is complete
                        print("This task has been completed and cannot be changed.")
                elif edit_task == 2:
                    task['completed'] = True
                else:
                    user_choice = int(input("Please enter which task you would like, or enter -1 to exit back to menu: "))
            else:
                print ("This task is not for this user. Please try again.")
                user_choice = int(input("Please enter which task you would like, or enter -1 to exit back to menu: "))
        else:
            print ("You have not entered an appropriate number. Please try again.")
            user_choice = int(input("Please enter which task you would like, or enter -1 to exit back to menu: "))
    print ("Goodbye!")

#generates reports for the user
def gen_report(gr):
    num_tasks = len(task_list) #total number of tasks
    completed = 0 #total completed tasks
    uncompleted = 0 #total incomplete tasks
    overdue = 0 #total overdue tasks
    overdue_and_incomplete = 0 #total overdue and incomplete tasks
    curr_date = date.today() #gets todays date
    for task in task_list:#checks if task is complete or incomplete
        if task['completed'] == True:
            completed+=1 
        else:
            uncompleted+=1
        task_date_str = str(task['due_date']) #Takes due date and turns it into the correct format to check if the task is overdue
        task_date_str = task_date_str.replace(" 00:00:00", "")
        task_datetime = datetime.strptime(task_date_str, DATETIME_STRING_FORMAT)
        new_task_date = task_datetime.date()
        if new_task_date<curr_date: #checks if task due date is before todays date, if less than then it is overdue
            overdue+=1
        if task['completed'] == False and new_task_date<curr_date: #checks if task is overdue and incomplete
            overdue_and_incomplete+=1
    #calculates percentages   
    while True:
        try:     
            incomplete_per = (uncompleted/num_tasks)*100
            overdue_per = (overdue/num_tasks)*100
        except ValueError:
            print("No tasks available")
            break

    #Adds data to file and returns data in user friendly way. 
    with open('task_overview.txt', 'w') as user_file:
        user_file.write("\nThe total tasks are: " + str(num_tasks))
        user_file.write("\nThe total completed tasks are: " + str(completed))
        user_file.write("\nThe total uncompleted tasks are: " + str(uncompleted))
        user_file.write("\nThe total uncompleted and overdue tasks are: " + str(overdue_and_incomplete))
        user_file.write("\nThe total percentage of incomplete tasks are: " + str(incomplete_per))
        user_file.write("\nThe total percentage of overdue tasks are: " + str(overdue_per))
    with open('task_overview.txt', 'r') as user_file:
        for line in user_file:
            print(line)
    #gets total number of users
    total_users = 0
    with open("user.txt", 'r') as new_file:
        for line in new_file:
            total_users+=1

    task_total = len(task_list) #gets total tasks
    user_total = 0 #how many tasks are the users
    user_overdue = 0 #how many of the users tasks are overdue
    user_completed = 0 #how many of the users tasks are complete
    user_incomplete = 0 #how many of the users tasks are incomplete
    user_incomplete_overdue = 0 #how many of the users tasks are incomplete and overdue
    for task in task_list: 
        string_due_date = str(task['due_date'])
        string_due_date = string_due_date.replace(" 00:00:00", "")
        due_datetime = datetime.strptime(string_due_date, DATETIME_STRING_FORMAT)
        new_date = due_datetime.date() #gets date of task
        if task['username'] == curr_user:
            user_total+=1 #finds how many tasks the user has
            if task['completed'] == True:
                user_completed+=1 #how many user tasks are complete
            if task['completed'] == False:
                user_incomplete+=1 #how many user tasks are incomplete
            if new_date<curr_date:
                user_overdue+=1 #how many user tasks are overdue
            if task['completed'] == False and new_date<curr_date:
                user_incomplete_overdue+=1 #how many user tasks are overdue and incomplete
    #calculates percentages
    while True:
        try:
            user_per = (user_total/task_total)*100
            complete_user_per = (user_completed/user_total)*100
            incomplete_user_per = (user_incomplete/user_total)*100
            user_incomplete_overdue_per = (user_incomplete_overdue/user_total)*100
        except ValueError:
            print("User has no tasks assigned.")
            break
    with open('user_overview.txt', 'w') as user_file: #writes data to file and returns output to user
        user_file.write("The total tasks are: " + str(task_total))
        user_file.write("\n\n\nThe total number of users are: "+ str(total_users))
        user_file.write("\nThe total number of tasks to the current user are: " + str(user_total))
        user_file.write("\nThis user has a total task percentage of: " + str(user_per))
        user_file.write("\nThe percentage of completed tasks assigned to this user are: " + str(complete_user_per))
        user_file.write("\nThe percentage of incomplete tasks assigned to this user are: " + str(incomplete_user_per))
        user_file.write("\nThe percentage of overdue incomplete tasks assigned to this user are: " + str(user_incomplete_overdue_per))
    with open('user_overview.txt', 'r') as user_file:
        for line in user_file:
            print(line)


    
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()
#checks user selection and returns program selected
    if menu == 'r':
        reg_user(menu)

    elif menu == 'a':
        add_task(menu)

    elif menu == 'va':
        view_all(menu)
        
    elif menu == 'vm':
        view_mine(menu)
    
    elif menu == 'gr':
        gen_report(menu)
                
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
