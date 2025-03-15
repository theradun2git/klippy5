import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class NotesPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Notizen")
        self.master.geometry("450x500")
        self.master.configure(bg='#FFFACD')
        self.notes = []
        self.current_note = None

        # Design anwenden
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 10), padding=5)
        style.configure('TLabel', font=('Helvetica', 110))

        # Notizen laden
        self.load_notes()

        # Ladebildschirm erstellen
        self.create_load_screen()

    def load_notes(self):
        """Lädt die Notizen aus den Dateien."""
        if not os.path.exists("klippy5/notes"):
            os.makedirs("klippy5/notes")
        self.notes = [f.replace('.txt', '') for f in os.listdir("klippy5/notes") if f.endswith('.txt')]

    def save_note_to_file(self, note_title, note_content):
        """Speichert eine Notiz in einer Datei."""
        with open(f"klippy5/notes/{note_title}.txt", "w", encoding="utf-8") as file:
            file.write(note_content)

    def load_note_from_file(self, note_title):
        """Lädt den Inhalt einer spezifischen Notiz aus einer Datei."""
        with open(f"klippy5/notes/{note_title}.txt", "r", encoding="utf-8") as file:
            return file.read()

    def create_load_screen(self):
        # Vorherige Widgets entfernen
        for widget in self.master.winfo_children():
            widget.destroy()

        # Liste der Notizen anzeigen
        self.notes_listbox = tk.Listbox(self.master, font=('Helvetica', 12), bg='#ffffff')
        self.notes_listbox.place(relx=0.5, rely=0.3, anchor='center', width=300, height=200)
        self.display_current_notes()

        # Buttons für Aktionen
        load_button = ttk.Button(self.master, text="Laden", command=self.load_note)
        load_button.place(relx=0.5, rely=0.6, anchor='center', width=200, height=40)

        new_button = ttk.Button(self.master, text="Neue Notiz", command=self.new_note)
        new_button.place(relx=0.5, rely=0.7, anchor='center', width=200, height=40)

        delete_button = ttk.Button(self.master, text="Löschen", command=self.delete_note)
        delete_button.place(relx=0.5, rely=0.8, anchor='center', width=200, height=40)

    def display_current_notes(self):
        """Zeigt alle aktuellen Notizen in der Listbox an."""
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note)

    def load_note(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            self.current_note = self.notes[selected_index]
            note_content = self.load_note_from_file(self.current_note)
            self.edit_note_screen(note_content)
        except IndexError:
            messagebox.showwarning("Warnung", "Bitte wählen Sie eine Notiz aus.")

    def new_note(self):
        self.current_note = None
        self.edit_note_screen("")

    def delete_note(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            note_to_delete = self.notes[selected_index]
            if messagebox.askyesno("Löschen", f"Möchten Sie die Notiz '{note_to_delete}' wirklich löschen?"):
                os.remove(f"klippy5/notes/{note_to_delete}.txt")
                del self.notes[selected_index]
                self.create_load_screen()
                messagebox.showinfo("Gelöscht", "Notiz wurde gelöscht.")
        except IndexError:
            messagebox.showwarning("Warnung", "Bitte wählen Sie eine Notiz aus.")

    def edit_note_screen(self, note_content):
        # Vorherige Widgets entfernen
        for widget in self.master.winfo_children():
            widget.destroy()

        # Fenster Titel aktualisieren
        self.master.title(f"Notizen - {self.current_note if self.current_note else 'Neue Notiz'}")

        # Textfeld für Notiz
        self.text_area = tk.Text(self.master, wrap='word', font=('Helvetica', 12), bg='#ffffff')
        self.text_area.place(relx=0.5, rely=0.4, anchor='center', width=400, height=300)
        self.text_area.insert(tk.END, note_content)

        # Bearbeitungsoptionen
        save_button = ttk.Button(self.master, text="Speichern", command=self.save_note)
        save_button.place(relx=0.5, rely=0.75, anchor='center', width=200, height=40)

        back_button = ttk.Button(self.master, text="Zurück", command=self.create_load_screen)
        back_button.place(relx=0.5, rely=0.85, anchor='center', width=200, height=40)

    def save_note(self):
        note_content = self.text_area.get("1.0", tk.END).strip()
        if note_content:
            if self.current_note:
                # Aktualisieren der bestehenden Notiz
                self.save_note_to_file(self.current_note, note_content)
            else:
                # Hinzufügen einer neuen Notiz
                note_title = simpledialog.askstring("Titel der Notiz", "Bitte geben Sie einen Titel für die Notiz ein:")
                if note_title:
                    self.notes.append(note_title)
                    self.save_note_to_file(note_title, note_content)
            messagebox.showinfo("Speichern", "Notiz wurde gespeichert.")
            self.create_load_screen()
        else:
            messagebox.showwarning("Warnung", "Notiz ist leer und wird nicht gespeichert.")

