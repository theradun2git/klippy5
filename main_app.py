import tkinter as tk
from tkinter import ttk, messagebox
from time import strftime
from PIL import Image, ImageTk

# Funktion zur Aktualisierung von Datum und Uhrzeit
def update_time():
    current_time = strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Funktion zur Anzeige des Hinweisfensters
def show_in_progress():
    messagebox.showinfo("In Progress", "Diese Funktion ist in Arbeit.")

# Hauptfenster
window = tk.Tk()
window.title("Klippy 5")
window.geometry("500x768")

# Hintergrundbild laden und skalieren
original_image = Image.open("klippy5/img/background.jpg")
background_image = original_image.resize((1024, 768), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Canvas erstellen und Hintergrundbild hinzufügen
canvas = tk.Canvas(window, width=1024, height=768)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Bild oben in der Mitte laden und hinzufügen
top_image = Image.open("klippy5/img/paperclip.png")
top_image_resized = top_image.resize((150, 150), Image.LANCZOS)  # Bildgröße anpassen
top_photo = ImageTk.PhotoImage(top_image_resized)
canvas.create_image(250, 100, image=top_photo, anchor="center")  # Bild oben in der Mitte platzieren

# Style für die Buttons definieren
style = ttk.Style()
style.configure("Accent.TButton", font=("Helvetica", 12), foreground="#000000", background="#007BFF", padding=15)

# Funktion zur Platzierung der Buttons
def place_button(text, y_position):
    button = ttk.Button(window, text=text, style="Accent.TButton", command=show_in_progress)
    button.place(relx=0.50, rely=y_position, anchor='center', width=200, height=60)  # Button mittig platzieren und Größe festlegen

# Buttons für die verschiedenen Funktionen
button_texts = [
    "📝 Notizen",
    "📅 Kalender",
    "✅ To do",
    "🤖 Frag Klippy",
    "🎵 Work Life Balance"
]

# Platzierung der Buttons
y_positions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]  # Y-Positionen für die Buttons

for text, y in zip(button_texts, y_positions):
    place_button(text, y)

# Datum und Uhrzeit unten in der Mitte
style.configure("Time.TLabel", font=("Helvetica", 18, "bold"), foreground="#ffffff", background="#007BFF", padding=10, relief="ridge")

# Zeit-Label erstellen
time_label = ttk.Label(window, style="Time.TLabel")
time_label.place(relx=0.5, rely=1.0, anchor='s', y=-10)  # Unten in der Mitte

# Uhrzeit aktualisieren
update_time()

# Ausführen
window.mainloop()