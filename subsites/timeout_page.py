import tkinter as tk
import webbrowser
import random
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk

class TimeoutPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Entspannung")
        self.parent.geometry("600x400")

        # Hintergrundbild mit Pillow laden
        image = Image.open("klippy5/img/relax.jpg")
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.parent, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Titel mit transparentem Hintergrund
        label_frame = tk.Frame(self.parent, bg='white', highlightbackground='black', highlightthickness=1, bd=0)
        label_frame.pack(pady=20, padx=20, fill='x')
        label = ttk.Label(label_frame, text="Wählen Sie ein Entspannungsangebot:", font=("Arial", 16, "bold"), background='white', foreground='black')
        label.pack(pady=10)

        # Style für die Buttons definieren
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 12), padding=10, background='white', foreground='black')
        style.map("Accent.TButton",
                  foreground=[('pressed', 'white'), ('active', 'blue')],
                  background=[('pressed', '!disabled', '#0056b3'), ('active', '#0056b3')])

        # Buttons für verschiedene Entspannungsangebote
        self.create_styled_button("🎮 Spiel spielen", self.play_game).pack(pady=10, fill='x', padx=220)
        self.create_styled_button("🎵 Musik hören", self.play_music).pack(pady=10, fill='x', padx=220)
        self.create_styled_button("📺 Video ansehen", self.watch_video).pack(pady=10, fill='x', padx=220)

    def create_styled_button(self, text, command):
        button = ttk.Button(self.parent, text=text, command=command, style="Accent.TButton")
        return button

    def play_game(self):
        # Ratespiel
        number_to_guess = random.randint(1, 50)
        guess = simpledialog.askinteger("Ratespiel", "Rate eine Zahl zwischen 1 und 50:")

        if guess == number_to_guess:
            messagebox.showinfo("Ratespiel", "Herzlichen Glückwunsch! Sie haben richtig geraten.")
        else:
            messagebox.showinfo("Ratespiel", f"Leider falsch! Die richtige Zahl war {number_to_guess}.")

    def play_music(self):
        # YouTube-Link im Standard-Webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=I3OJUwILelU")

    def watch_video(self):
        # YouTube-Link im Standard-Webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")