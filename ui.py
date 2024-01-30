import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from openai_helper import extract_text_from_pdf, rewrite_text, generate_images
import requests

file_path = ''
file_label = ''
image_label = ''
chosen_learner_type = ''

def open_file():
    global file_path, file_label
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    if file_path:
        file_label.config(text=f"Selected file: {file_path}")
        update_go_button()

def start_process():
    print("Processing...")
    pdf_text = extract_text_from_pdf(file_path)
    rewritten = rewrite_text(pdf_text, chosen_learner_type)
    image_url = generate_images()

    rewritten_text.config(state='normal')
    rewritten_text.delete(1.0, tk.END)
    rewritten_text.insert(tk.END, f"Rewritten text: {rewritten}\n\n")

    display_image_from_url(image_url)

    rewritten_text.config(state='disabled')

def display_image_from_url(image_url):
    global image_label
    # Download image from the URL
    image = Image.open(requests.get(image_url, stream=True).raw)

    # Resize the image if needed
    image = image.resize((300, 300), Image.BICUBIC)

    # Convert image to PhotoImage format
    tk_image = ImageTk.PhotoImage(image)

    # Display image on the Tkinter window
    image_label.config(image=tk_image)
    image_label.image = tk_image

def select_learner_type(button, learner_type):
    global chosen_learner_type
    chosen_learner_type = learner_type
    for btn in buttons:
        if btn != button:
            btn.state(['!selected'])
    button.state(['selected'])
    update_go_button()

def update_go_button():
    if file_path and chosen_learner_type:
        go_button.config(text=f"Convert Material for Learning Style: {chosen_learner_type}", state='active')
    else:
        go_button.config(text="Select File and Learning Style First", state='disabled')

def create_ui(root):
    global file_label, image_label

    style = ttk.Style()
    style.theme_use("clam")

    root.configure(bg="#f0f0f0")
    
    file_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
    file_frame.grid(row=0, column=0, pady=10, sticky="ew")

    file_button = ttk.Button(file_frame, text="Select PDF", command=open_file, style='TButton')
    file_button.grid(row=0, column=0, padx=(0, 10))

    file_label = ttk.Label(file_frame, text="No file selected", anchor="w", style='TLabel')
    file_label.grid(row=0, column=1, sticky="ew")

    learner_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
    learner_frame.grid(row=1, column=0, pady=10, sticky="ew")

    learner_label = ttk.Label(learner_frame, text="Select Learning Style:", style='TLabel')
    learner_label.grid(row=0, column=0, padx=(0, 10))

    learner_types = ['Auditory', 'Visual', 'Kinesthetic']
    global buttons
    buttons = []

    for i, learner_type in enumerate(learner_types):
        button = ttk.Checkbutton(learner_frame, text=learner_type, style='TCheckbutton', padding=(10, 5))
        button.grid(row=0, column=i+1, padx=(0, 10))
        button.config(command=lambda button=button, chosen_learner_type=learner_type: select_learner_type(button, chosen_learner_type))
        buttons.append(button)

    global go_button
    go_button = ttk.Button(root, text="Select File and Learning Style First", command=start_process, style='TButton', padding=(10, 5), state='disabled')
    go_button.grid(row=2, column=0, pady=10)

    global rewritten_text
    rewritten_text = tk.Text(root, wrap='word', height=20, width=80, state='disabled', font=('Helvetica', 12))
    rewritten_text.grid(row=3, column=0, pady=10, padx=10)

    image_label = ttk.Label(root, text="Generated Image", style='TLabel')
    image_label.grid(row=4, column=0, pady=10)
