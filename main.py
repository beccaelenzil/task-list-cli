from task_list_cli.task_list import TaskList


options = {
    "1": "list tasks", 
    "2": "create task",
    "3": "select task", 
    "4": "update task", 
    "5": "delete task", 
    "6": "mark task complete",
    "7": "mark task incomplete",
    "8": "Delete All Tasks",
    "9": "list all options",
    "10": "Quit"
    }

def list_choices():
    print("What would you like to do?")
    print("**************************")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")

choice = None
valid_choices = options.keys()

task_list = TaskList()
play = True
list_choices()

while play==True:
    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5','6','7'] and task_list.selected_task == None:
        print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
        choice = "3"


    if choice=='1':
        print("Tasks:")
        print("**************************")
        for task in task_list.list_tasks():
            print(task)
    elif choice=='2':
        print("Great! Let's create a new task.")
        title=input("What is the title of your task? ")
        description=input("What is the description of your task? ")
        new_task = task_list.create_task(title=title, description=description)
        print("New task:", new_task)
    elif choice=='8':
        for task in task_list.list_tasks():
            task_list.get_task(id=task['id'])
            task_list.delete_task()
    elif choice=='9':
        list_choices()
    elif choice=='10':
        play=False


    choice = None
    print("**************************")

# print("*******")
# print("Select task with title 'learn flask' ")
# becca.get_task(title="learn flask")

# print("*******")
# print("Selected Task: ",becca.selected_task)


# print("*******")
# print("Delete Selected Task")

# becca.delete_task()

# print("*******")
# print("All tasks: ", becca.list_tasks())