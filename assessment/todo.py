import tkinter as tk
from tkinter import ttk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = ttk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        style = ttk.Style()
        style.configure("Add.TButton", background="green")
        style.configure("Delete.TButton", background="red")
        style.configure("Complete.TButton", background="blue")

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task, style="Add.TButton")
        self.add_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = ttk.Button(master, text="Delete Task", command=self.delete_task, style="Delete.TButton")
        self.delete_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.complete_button = ttk.Button(master, text="Mark as Complete", command=self.mark_complete, style="Complete.TButton")
        self.complete_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
