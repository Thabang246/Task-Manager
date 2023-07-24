#==== Task Manager ====#
# Create a program that can help manage tasks assigned to team members.
# This program will work with two text files : user.txt and tasks.txt.
# user.txt : stores the usernames and passwords all the users that have permission to use the program.
# tasks.txt : stores a list of all the tasks that the team is working on.


#==== Open file ====#
# Create a Dictionary to store and map data from the user.txt file.
# Use "with open" along with the "r " access modifier to read , and bypass closing the file manually.
user_data = {}  
with open("user.txt","r") as f_users :
    logins = f_users.readlines()
# Create a for loop to pull information from the user.txt file
# Index the information from user.txt as "data list" to the dictionary.
    for data in logins:
        datalist = data.strip("\n").split(", ")
        user_data[datalist[0]] = datalist[1]


#==== Login Section ====#
# This block of code will allow a user to login.
# Read usernames and passwords from the user.txt file.
# Use a while loop along with if statements to validate usernames and passwords.
# Create a Global variable to store the usernames of the users when they login.
loggedin_name = ""
username_input = None     
while True: 
    username_input = input("Please enter your username: ")
    if username_input in user_data: 
        print(f"Thank you {username_input}!")
        loggedin_name = username_input
        break
    else:
        print("Invalid username! ")

while True:
    password_input = input("Please enter your password: ")
    if password_input == user_data[username_input]: 
        print(f"Thank you {username_input}! \n ")
        break
    else:
	    print("Invalid password! ")


#==== Menu Section ====#
# Present a menu to the user, use triple quotations to format your menu.
# Make sure that the user input is coneverted to lower case.
# Create an if statement to validate that only, the applicable menu is shown for the appropriate user.
while True:
    if loggedin_name == "admin" :
        menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - View my task
ds - Display Statistics.
e  - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a  - Adding a task
va - View all tasks
vm - View my task
e  - Exit
: ''').lower()


#=== Registering a user ====#
# This block of code will register a new user to the user.txt file.
# Only the user with the username ‘admin’ is allowed to register users.
    if menu == 'r':
            new_user = input("\nPlease enter a username: ")
            new_passwd = input("Please enter a password: ")
            passwd_confirm = input("Please confirm your password: ")    
            
    # Use an if statement to validate the password confirmation.  

            while new_passwd != passwd_confirm :                        
                print("Incorrect Password ")
                passwd_confirm = input("Please confirm your password: ")
                    
            else:
                print(f"""\nPassword Confirmed! {new_user} has been registered!
Please find the Menu below to perfom futher actions.\n""") 

    # Open the file user.txt with the "r+" access modifier to read and apply changes to user.txt file.
            with open("user.txt","r+") as f_users :
                logins = f_users.readlines()
                f_users.write(f"\n{new_user}, {passwd_confirm}")


#==== Adding a task ====#
# This block of code will allow the user to add a new task to task.txt file.
# Remember to include the 'No' to indicate if the task is complete.
    elif menu == 'a':
        assigned_user = input("\nPlease enter the username you would like to assign a task to: ")
        task_title = input("Please enter the title of the task you would like to assign: ")
        task_description = input("Please enter a brief desciption of the task: ")
        task_due = input("Please enter the task due date: ")
        current_date = input("Please enter the current date: ")
        print(f"""\nTask: {task_title} - has sucessfully been assigned to: {assigned_user}!
Please find the Menu below to perfom futher actions.\n""")

# Open the file user.txt with the "r+"" access modifier to read and apply changes to user.txt file.
        with open("tasks.txt","r+") as f_users :
            logins = f_users.readlines()
            f_users.write(f"\n{assigned_user}, {task_title}, {task_description}, {task_due}, {current_date}, No ")


#==== View all tasks ====#
# In this block of code the program will allow the user to view each task and display the information.
# Open the file user.txt with the "r" access modifier and Split the line where there is a comma and space.
# Index and use triple quotations to format your print statement.
    elif menu == 'va':
        with open("tasks.txt","r") as task_files :
            for data in task_files :
                tasks_list = data.strip("\n").split(", ")
                print(f'''\nTask:\t\t\t\t {tasks_list[1]}
Assigned To:\t\t\t {tasks_list[0]}
Date Assigned:\t\t\t {tasks_list[3]}
Due Date:\t\t\t {tasks_list[4]}
Task Complete?\t\t\t {tasks_list[5]}
Task Description:\t\t {tasks_list[2]}\n''')


#==== View my task ====#
# This block of code will read and only display all the tasks that have been assigned to the user that is currently logged-in.
# Use an if statement to Index the username from the txt file, to the Global variable we created, to validate the user currently logged in.
    elif menu == 'vm':
        with open("tasks.txt","r") as task_files :
            task_flag = True
            for data in task_files :
                tasks_list = data.strip("\n").split(", ")
                if tasks_list[0] == loggedin_name:
                    task_flag = False
                    print(f'''\nTask:\t\t\t\t {tasks_list[1]}
Assigned To:\t\t\t {tasks_list[0]}
Date Assigned:\t\t\t {tasks_list[3]}
Due Date:\t\t\t {tasks_list[4]}
Task Complete?\t\t\t {tasks_list[5]}
Task Description:\t\t {tasks_list[2]}\n''')

            if task_flag:
                print("\nYou Currently have no tasks assigned to you. Please check again later.\n")

#==== Dispaly Statistics ====#
# Provide The admin user with a menu option that displays The total number of tasks and the total number of users.
# Create a variable that acts as a counter intialized to zero.
    elif menu == 'ds' :
        with open("tasks.txt","r") as task_files :
            num_tasks = 0
            for data in task_files :
                num_tasks += 1
            print(f"\nTotal number of tasks:\t{num_tasks}")

        with open("user.txt","r") as user_files :
            num_users = 0
            for data in user_files :
                num_users += 1
            print(f"Total number of users:\t{num_users}\n")            

#==== Exit Section ====#
# This block of code will allow the user to exit the menu.
# Create a default for any invalid entries the user might enter in the menu.
    elif menu == 'e':
        print('\nGoodbye!!!\n')
        exit()

    else:
        print("\nInvalid Entry! Please read the menu carefully and Try again\n")
