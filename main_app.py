import tkinter as tk
from tkinter import ttk
from time import strftime
from PIL import Image, ImageTk
from subsites.notes_page import NotesPage
from subsites.calendar_page import CalendarPage
from subsites.todo_page import TodoPage
from subsites.klippybot_page import KlippyBot
from subsites.timeout_page import TimeoutPage

# Funktion zur Aktualisierung von Datum und Uhrzeit
def update_time():
    current_time = strftime('%d-%m-%Y | %H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Funktion zur Anzeige der Notizenseite
def show_notes_page():
    NotesPage(tk.Toplevel(window))

# Funktion zur Anzeige der Kalenderseite
def show_calendar_page():
    CalendarPage(tk.Toplevel(window))

# Funktion zur Anzeige der To-Do-Seite
def show_todo_page():
    TodoPage(tk.Toplevel(window))

# Funktion zur Anzeige von Time Out
def show_timeout_page():
    TimeoutPage(tk.Toplevel(window))

# Funktion zum Aufrufen des Klippy Bots
def show_klippy_bot():
    KlippyBot(window)

# Hauptfenster
window = tk.Tk()
window.title("Klippy 5")
window.geometry("400x700")

# Canvas (Leinwand) erstellen und Hintergrundfarbe auf Schwarz setzen
canvas = tk.Canvas(window, width=400, height=700, bg='black')
canvas.pack(fill="both", expand=True)

# Bild oben in der Mitte einfügen und verkleinern
top_image = Image.open("klippy5/img/paperclip.png")
top_image = top_image.resize((225, 100), Image.LANCZOS)
top_image_tk = ImageTk.PhotoImage(top_image)
canvas.create_image(200, 90, image=top_image_tk, anchor='center')

# Fragezeichen-Emoji als Button hinzufügen
help_button = tk.Button(window, text="❓", command=show_klippy_bot, font=("Arial", 14), borderwidth=0, highlightthickness=0, relief="flat", cursor="hand2")
help_button.place(relx=0.95, rely=0.11, anchor='ne')

# Style für die Buttons definieren
style = ttk.Style()
style.configure("Accent.TButton", font=("Arial", 12), padding=0, borderwidth=0, relief="flat")
style.map("Accent.TButton", background=[('active', '#0056b3')])

# Funktion zur Platzierung der Buttons
def place_button(image_path, y_position, command):
    button_image = Image.open(image_path)
    button_image = button_image.resize((200, 50), Image.LANCZOS)
    button_image_tk = ImageTk.PhotoImage(button_image)
    button = tk.Button(window, image=button_image_tk, command=command, borderwidth=0, highlightthickness=0, relief="flat", cursor="hand2")
    button.image = button_image_tk  # Referenz speichern, um das Bild nicht zu verlieren
    button.place(relx=0.50, rely=y_position, anchor='center', width=200, height=50)

# Buttons für die verschiedenen Funktionen
button_info = [
    ("klippy5/img/button-notizen.png", show_notes_page),
    ("klippy5/img/button-kalender.png", show_calendar_page),
    ("klippy5/img/button-todo.png", show_todo_page),
    ("klippy5/img/button-timeout.png", show_timeout_page)
]

# Platzierung der Buttons
y_positions = [0.3, 0.4, 0.5, 0.6]  # Y-Positionen für die Buttons

for (image_path, command), y in zip(button_info, y_positions):
    place_button(image_path, y, command)

# Datum und Uhrzeit unten in der Mitte
time_bg_image = Image.open("klippy5/img/button-timeclock.png")
time_bg_image = time_bg_image.resize((200, 50), Image.LANCZOS)
time_bg_image_tk = ImageTk.PhotoImage(time_bg_image)
style.configure("Time.TLabel", font=("Arial", 12), background='black', foreground='white')
time_label = ttk.Label(window, text="", style="Time.TLabel", image=time_bg_image_tk, compound='center')
time_label.image = time_bg_image_tk  # Referenz speichern
time_label.place(relx=0.50, rely=1.0, anchor='s', y=-60)  # Unten in der Mitte

# Uhrzeit aktualisieren
update_time()

# Ausführen
window.mainloop()