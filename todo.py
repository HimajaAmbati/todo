tasks=[]

def addtask():
    task=input("Enter task:")
    tasks.append(task)
    print(f"{task} added..") 

def deletetask():
    listtask()
    try:
        tasktodelete=int(input("Enter the number to delete:"))
        if tasktodelete< len(tasks) and tasktodelete>=0:
            tasks.pop(tasktodelete)
            print(f"Task {tasktodelete} has been removed.")
        else:
            print(f"Task {tasktodelete} was not found")
    except:
        print("Invalid Input")

def listtask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")


if __name__=="__main__":
    print("Welcome to the TO-DO app:)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Quit")

        choice=input("Enter your choice:")
        if(choice=="1"):
            addtask()
        elif (choice=="2"):
            deletetask()
        elif(choice=="3"):
            listtask()
        elif(choice=="4"):
            break
        else:
            print("Invalid Input.Please try again.")
    print("Goodbyeee!! Have a good day")


