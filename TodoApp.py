import tkinter as tk
from tkinter import messagebox
import json

class Todo_App:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        """Adds a new task to your list"""
        self.tasks.append({"Task": task, "completed": False})
    
    def remove_task(self, index):
        """Removes a task from your list"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def get_tasks(self):
        """Returns the list of tasks"""
        return self.tasks
    
    def edit_task(self, index, new_task):
        """Edits an existing task in your list"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["Task"] = new_task

    def toggle_task_completion(self, index):
        """Marks a task completed or uncompleted"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()
        
    def save_tasks(self):
        """Saves tasks to a JSON file"""
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        """Loads tasks from a JSON file if it exists"""
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

def add_task():
    task = task_entry.get()
    if task:
        todo_app.create_task(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        todo_app.remove_task(selected_task)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in todo_app.get_tasks():
        display_text = task["Task"] + (" ✅" if task["completed"] else "")
        task_listbox.insert(tk.END, display_text)

def edit_task():
    try:
        selected_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            todo_app.edit_task(selected_index, new_task)
            update_task_list()
        else:
            messagebox.showwarning("Warning", "Enter a new task name")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit")

def toggle_completion():
    try:
        selected_index = task_listbox.curselection()[0]
        todo_app.toggle_task_completion(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed")

root = tk.Tk()
root.title("Todo App")

todo_app = Todo_App()

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", command=toggle_completion)
complete_button.pack(pady=5)

root.mainloop()