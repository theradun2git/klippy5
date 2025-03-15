import tkinter as tk
import datetime
import json
import os
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class CalendarPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalender")
        self.master.geometry("450x768")
        self.master.configure(bg="#e0f7da")

        # Kalender-Widget erstellen
        self.calendar = Calendar(self.master, selectmode='day', year=datetime.datetime.now().year, 
                                 month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        self.calendar.pack(pady=10, padx=10, fill=tk.X)

        # Notizenbereich
        self.notes_label = ttk.Label(
            self.master, 
            text="Notizen:", 
            background="#e0f7da", 
            anchor="w",  # 'w' steht für 'west', was linksbündig ist
            font=("Helvetica", 12, "bold")
        )
        self.notes_label.pack(pady=10, padx=10, fill=tk.X)

        # Breite und Höhe des Notizenbereichs angepasst
        self.notes_text = tk.Text(self.master, height=5, width=20)
        self.notes_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        # Frame für Buttons
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(pady=10)

        # Buttons für Notizen speichern, laden und löschen
        self.save_button = ttk.Button(self.button_frame, text="Speichern", command=self.save_note)
        self.save_button.grid(row=0, column=0, padx=5)

        self.load_button = ttk.Button(self.button_frame, text="Laden", command=self.load_note)
        self.load_button.grid(row=0, column=1, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Löschen", command=self.delete_note)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Button für alle Notizen anzeigen
        self.show_all_button = ttk.Button(self.button_frame, text="Notizenübersicht", command=self.show_all_notes)
        self.show_all_button.grid(row=0, column=3, padx=5)

        # Notizen-Datei
        self.notes_file = "klippy5/notes/calendar_notes.json"
        self.notes_data = self.load_notes_data()

    def load_notes_data(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                return json.load(file)
        return {}

    def save_notes_data(self):
        with open(self.notes_file, "w") as file:
            json.dump(self.notes_data, file)

    def save_note(self):
        selected_date = self.calendar.get_date()
        note_text = self.notes_text.get("1.0", tk.END).strip()
        if note_text:
            self.notes_data[selected_date] = note_text
            self.save_notes_data()
            messagebox.showinfo("Gespeichert", f"Notiz für {selected_date} gespeichert.")
        else:
            messagebox.showwarning("Keine Notiz", "Bitte geben Sie eine Notiz ein.")

    def load_note(self):
        selected_date = self.calendar.get_date()
        note_text = self.notes_data.get(selected_date, "")
        self.notes_text.delete("1.0", tk.END)
        self.notes_text.insert(tk.END, note_text)

    def delete_note(self):
        selected_date = self.calendar.get_date()
        if selected_date in self.notes_data:
            del self.notes_data[selected_date]
            self.save_notes_data()
            self.notes_text.delete("1.0", tk.END)
            messagebox.showinfo("Gelöscht", f"Notiz für {selected_date} gelöscht.")
        else:
            messagebox.showwarning("Keine Notiz", "Es gibt keine Notiz für dieses Datum.")

    def show_all_notes(self):
        # Neues Fenster erstellen
        all_notes_window = tk.Toplevel(self.master)
        all_notes_window.title("Alle Notizen")
        all_notes_window.geometry("400x400")
        all_notes_window.configure(bg="#e0f7da")

        # Scrollbar hinzufügen
        scrollbar = ttk.Scrollbar(all_notes_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text-Widget für die Anzeige der Notizen
        notes_display = tk.Text(all_notes_window, yscrollcommand=scrollbar.set, wrap=tk.WORD)
        notes_display.pack(expand=True, fill=tk.BOTH)

        # Scrollbar mit Text-Widget verbinden
        scrollbar.config(command=notes_display.yview)

        # Alle Notizen mit Datum anzeigen
        for date, note in self.notes_data.items():
            notes_display.insert(tk.END, f"Datum: {date}\nNotiz: {note}\n\n")

        # Text-Widget nicht bearbeitbar machen
        notes_display.config(state=tk.DISABLED)
