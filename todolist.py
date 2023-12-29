from tkinter import *

def add_task():
    task = e2.get()
    print("Adding task:", task)

def delete_task():
    task = e3.get()
    print("Deleting task:", task)

def delete_all_tasks():
    print("Deleting all tasks")

parent = Tk()
parent.title("To Do List")

Label(parent, text='Enter the task').grid(row=0, column=0)
e1 = Entry(parent)
e1.grid(row=0, column=1)

Label(parent, text="Add Task").grid(row=1, column=0)
e2 = Entry(parent)
e2.grid(row=1, column=1)
add_task_button = Button(parent, text='Add Task', command=add_task)
add_task_button.grid(row=1, column=2)

Label(parent, text="Delete Task").grid(row=2, column=0)
e3 = Entry(parent)
e3.grid(row=2, column=1)
delete_task_button = Button(parent, text='Delete Task', command=delete_task)
delete_task_button.grid(row=2, column=2)

Label(parent, text="Delete all tasks").grid(row=3, column=0)
delete_all_button = Button(parent, text='Delete All Tasks', command=delete_all_tasks)
delete_all_button.grid(row=3, column=2)

exit_button = Button(parent, text='Exit', command=parent.destroy)
exit_button.grid(row=4, column=0)

parent.mainloop()
