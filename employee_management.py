import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.id} - {self.name} - {self.position} - ${self.salary}"

class EmployeeManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Employee Management System")
        self.geometry("500x300")

        self.employees = []

        self.create_widgets()

    def create_widgets(self):
        self.id_label = tk.Label(self, text="ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.position_label = tk.Label(self, text="Position:")
        self.position_label.grid(row=2, column=0, padx=5, pady=5)
        self.position_entry = tk.Entry(self)
        self.position_entry.grid(row=2, column=1, padx=5, pady=5)

        self.salary_label = tk.Label(self, text="Salary:")
        self.salary_label.grid(row=3, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(self)
        self.salary_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(self, text="Remove Employee", command=self.remove_employee)
        self.remove_button.grid(row=4, column=1, padx=5, pady=5)

        self.display_button = tk.Button(self, text="Display Employees", command=self.display_employees)
        self.display_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_employee(self):
        try:
            id = int(self.id_entry.get())
            name = self.name_entry.get()
            position = self.position_entry.get()
            salary = float(self.salary_entry.get())

            self.employees.append(Employee(id, name, position, salary))
            messagebox.showinfo("Success", "Employee added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid data.")

    def remove_employee(self):
        try:
            id = int(self.id_entry.get())
            for index, employee in enumerate(self.employees):
                if employee.id == id:
                    self.employees.pop(index)
                    messagebox.showinfo("Success", "Employee removed successfully.")
                    break
            else:
                messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid ID.")

    def display_employees(self):
        display_window = tk.Toplevel(self)
        display_window.title("Employee List")
        display_window.geometry("400x300")

        text_area = tk.Text(display_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)

        for employee in self.employees:
            text_area.insert(tk.END, str(employee) + "\n")

if __name__ == "__main__":
    app = EmployeeManagementApp()
    app.mainloop()

