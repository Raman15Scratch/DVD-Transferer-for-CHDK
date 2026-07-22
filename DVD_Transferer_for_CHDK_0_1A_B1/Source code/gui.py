import tkinter as tk
from tkinter import filedialog, messagebox
import dvd_reader
import captions
import transfer


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DVD Transferer v0.1 BETA for CHDK 1.6.1")
        self.root.geometry("500x300")

        self.caption_file = None
        self.dvd_path = None

        self.label = tk.Label(self.root, text="Ready")
        self.label.pack(pady=10)

        tk.Button(self.root, text="Detect DVD", command=self.detect_dvd).pack(pady=5)
        tk.Button(self.root, text="Import Captions", command=self.import_captions).pack(pady=5)
        tk.Button(self.root, text="Start Transfer", command=self.start_transfer).pack(pady=5)
        self.version_label = tk.Label(
            self.root,
            text="v0.1_BETA",
            fg="gray"
        )
        self.version_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)

    def detect_dvd(self):
        self.dvd_path = dvd_reader.find_dvd()

        if self.dvd_path:
            self.label.config(text=f"DVD found!: {self.dvd_path}")
        else:
            messagebox.showerror("Error", "No DVD detected")

    def import_captions(self):
        self.caption_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if self.caption_file:
            self.label.config(text=f"Loaded captions: {self.caption_file}")

    def start_transfer(self):
        if not self.dvd_path:
            messagebox.showerror("Error", "No DVD detected")
            return

        caps = []

        if self.caption_file:
            caps = captions.load_captions(self.caption_file)

        self.label.config(text="Transferring...")

        transfer.fake_transfer(self.dvd_path, caps)

        self.label.config(text="Done!")

    def run(self):
        self.root.mainloop()
