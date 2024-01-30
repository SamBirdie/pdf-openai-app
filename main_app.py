import tkinter as tk
from tkinter import ttk
from ui import create_ui

def main():
    root = tk.Tk()
    root.title("OY AI Boosted Learning Materials AB - Learning Material Converter")
    root.geometry("1200x900")
    root.resizable(True, True)

    create_ui(root)

    root.mainloop()

if __name__ == "__main__":
    main()
