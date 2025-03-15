import tkinter as tk
import json
from tkinter import ttk, messagebox
from datetime import datetime

class TodoPage:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do Liste")
        self.master.configure(bg='#C8A2C8')
        self.master.geometry("650x300")

        self.tasks = []  # Liste zur Speicherung der Aufgaben
        self.completed_tasks = []  # Liste zur Speicherung der erledigten Aufgaben

        self.task_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Style für die Anwendung
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10), background='#C8A2C8')
        self.style.configure("TEntry", font=("Helvetica", 10))
        self.style.configure("TLabel", font=("Helvetica", 12), background='#C8A2C8')

        # Eingabefeld für neue Aufgaben
        self.entry = ttk.Entry(master, textvariable=self.task_var, width=40, style="TEntry")
        self.entry.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Eingabefeld für das Datum
        self.date_entry = ttk.Entry(master, textvariable=self.date_var, width=20, style="TEntry")
        self.date_entry.grid(row=0, column=2, pady=10, padx=10)
        self.date_var.set(datetime.now().strftime("%d-%m-%y"))

        # Button zum Hinzufügen einer neuen Aufgabe
        self.add_button = ttk.Button(master, text="➕ Neue Aufgabe hinzufügen", command=self.add_task, style="TButton")
        self.add_button.grid(row=0, column=3, pady=10, padx=10)

        # Liste zur Anzeige der Aufgaben
        self.task_listbox = tk.Listbox(master, width=70, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=4, pady=10, padx=10)

        # Buttons zum Bearbeiten, Löschen und Markieren von Aufgaben
        self.edit_button = ttk.Button(master, text="Bearbeiten", command=self.edit_task, style="TButton")
        self.edit_button.grid(row=2, column=0, pady=5, padx=5, sticky="ew")

        self.mark_done_button = ttk.Button(master, text="Als erledigt markieren", command=self.mark_done, style="TButton")
        self.mark_done_button.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        self.delete_button = ttk.Button(master, text="Löschen", command=self.delete_task, style="TButton")
        self.delete_button.grid(row=2, column=2, pady=5, padx=5, sticky="ew")

        # Button zum Aufrufen des Archivs
        self.archive_button = ttk.Button(master, text="erledigte anzeigen", command=self.show_archive, style="TButton")
        self.archive_button.grid(row=2, column=3, pady=5, padx=5, sticky="ew")

        # Laden der Aufgaben beim Starten
        self.load_tasks()

    def add_task(self):
        task = self.task_var.get().strip()
        date = self.date_var.get().strip()
        if task and date:
            self.tasks.append(f"{task} (Fällig am: {date})")
            self.update_task_listbox()
            self.task_var.set("")
            self.date_var.set(datetime.now().strftime("%d-%m-%y"))  # Reset auf heutiges Datum
            self.save_tasks()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = self.task_var.get().strip()
            new_date = self.date_var.get().strip()
            if new_task and new_date:
                self.tasks[selected_index[0]] = f"{new_task} (Fällig am: {new_date})"
                self.update_task_listbox()
                self.task_var.set("")
                self.date_var.set(datetime.now().strftime("%d-%m-%y"))
                self.save_tasks()
            else:
                messagebox.showwarning("Warnung", "Bitte geben Sie eine neue Aufgabe und ein Datum ein.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
            self.save_tasks()

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            self.completed_tasks.append(task)
            self.update_task_listbox()
            self.save_tasks()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open('klippy5/notes/todos.json', 'w') as file:
            json.dump({'tasks': self.tasks, 'completed_tasks': self.completed_tasks}, file)

    def load_tasks(self):
        try:
            with open('klippy5/notes/todos.json', 'r') as file:
                data = json.load(file)
                self.tasks = data.get('tasks', [])
                self.completed_tasks = data.get('completed_tasks', [])
                self.update_task_listbox()
        except FileNotFoundError:
            pass

    def show_archive(self):
        archive_window = tk.Toplevel(self.master)
        archive_window.title("Archiv")
        archive_window.configure(bg='#C8A2C8')

        archive_label = ttk.Label(archive_window, text="Erledigte Aufgaben:", style="TLabel")
        archive_label.pack(pady=10)

        completed_listbox = tk.Listbox(archive_window, width=70, height=10)
        completed_listbox.pack(pady=10, padx=10)

        for task in self.completed_tasks:
            completed_listbox.insert(tk.END, task)

        def delete_completed_task():
            selected_index = completed_listbox.curselection()
            if selected_index:
                self.completed_tasks.pop(selected_index[0])
                completed_listbox.delete(selected_index)
                self.save_tasks()

        delete_button = ttk.Button(archive_window, text="Löschen", command=delete_completed_task, style="TButton")
        delete_button.pack(pady=5)

        close_button = ttk.Button(archive_window, text="Schließen", command=archive_window.destroy, style="TButton")
        close_button.pack(pady=5)

