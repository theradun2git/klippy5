import tkinter as tk
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk

class KlippyBot:
    def __init__(self, master):
        self.master = master
        self.create_bot_window()

    def create_bot_window(self):
        self.bot_window = tk.Toplevel(self.master)
        self.bot_window.title("Klippy Bot")
        self.bot_window.geometry("500x650")
        self.bot_window.configure(bg="black")

        top_frame = tk.Frame(self.bot_window, bg="black")
        top_frame.pack(pady=10)

        self.label = tk.Label(top_frame, text="Hallo, ich bin Klippy \n Wie kann ich helfen?", bg="black", fg="white", font=("Helvetica", 16, "bold"))
        self.label.pack(side="right", padx=10)

        top_image = Image.open("klippy5/img/paperclip.png")
        top_image = top_image.resize((225, 100), Image.LANCZOS)
        top_image_tk = ImageTk.PhotoImage(top_image)
        image_label = tk.Label(top_frame, image=top_image_tk, bg="black")
        image_label.image = top_image_tk
        image_label.pack(side="left", padx=10)

        self.entry = ttk.Entry(self.bot_window, width=50)
        self.entry.pack(pady=10)

        button_frame = tk.Frame(self.bot_window, bg="black")
        button_frame.pack(pady=5, fill="x")

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        buttons = [
            ("Suche im Internet", self.search_internet),
            ("Öffnungszeiten", self.opening_hours),
            ("Kontakt", self.call),
            ("Vorlagen", self.show_templates),
            ("Leeren", self.clear_output)
        ]

        for i, (text, command) in enumerate(buttons):
            button = ttk.Button(button_frame, text=text, command=command)
            button.grid(row=i, column=1, sticky="ew", padx=10, pady=5)

        self.output_text = tk.Text(self.bot_window, bg="black", fg="white", font=("Helvetica", 12), wrap="word", height=10)
        self.output_text.pack(pady=10, fill="both", expand=True)

    def search_internet(self):
        query = self.entry.get()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.display_output("Ich habe im Internet nach Ihrer Anfrage gesucht.")
        else:
            self.display_output("Bitte geben Sie einen Suchbegriff ein.")

    def opening_hours(self):
        opening_hours_text = "Unsere Öffnungszeiten sind von\nMontag bis Freitag, von 9 bis 18 Uhr.\nAm Wochenende haben wir geschlossen"
        self.display_output(opening_hours_text)

    def call(self):
        self.display_output("Allgemeine Nummer: +41 433 20 39 oder Direktnummer: +41 433 20 59")

    def show_templates(self):
        templates_text = "Vorlage 1: Beispieltext für eine E-Mail\nVorlage 2: Beispieltext für einen Brief"
        self.display_output(templates_text)

    def display_output(self, text):
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)


