import tkinter as tk
 
class Todo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("TO DO LIST")
        self.create_widgets()
 
    def create_widgets(self):
        self.task_input = tk.Entry(self, width=40)
        self.task_input.pack(pady=10)
        self.add_button = tk.Button(self, text="Add your task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.tasks_box = tk.Listbox(self, selectmode=tk.SINGLE)
        self.tasks_box.pack(pady=5)
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=5)
        self.edit_button = tk.Button(self.button_frame, text="Edit the task", command=self.edit_task) 
        self.edit_button.grid(row=0, column=0, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete the task", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)
    
    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks_box.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
 
    def edit_task(self):
        task_index = self.tasks_box.curselection()
        if task_index:
            new_task = self.task_input.get()
            if new_task:
                self.tasks_box.delete(task_index)
                self.tasks_box.insert(task_index[0], new_task)
                self.task_input.delete(0, tk.END)
 
    def delete_task(self):
        task_index = self.tasks_box.curselection()    
        if task_index:
            self.tasks_box.delete(task_index)
 
if __name__ == "__main__":
    app = Todo()
    app.mainloop()
