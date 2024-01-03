# import pdfminer library
from unittest import result
from pdfminer.high_level import extract_text

# import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# import field extractor
from extractors.name import extract_names
from extractors.education import extract_education
from extractors.phone import extract_phone_number
from extractors.email import extract_emails
from extractors.skills import extract_skills

# extract text from pdf
def extract_text_from_pdf(pdf_path):
    txt = extract_text(pdf_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def process(initial_filepath, root):
    from tkinter import filedialog as fd

    # Get the file path from the user via a file dialog (only pdf file)
    filepath = fd.askopenfilename(initialdir=initial_filepath, title='Select file', filetypes=(('pdf files', '*.pdf'),))
    
    text = extract_text_from_pdf(filepath)
    name_information = extract_names(text)
    education_information = extract_education(text)
    phone = extract_phone_number(text)

    # root.destroy()

    result_window = tk.Tk()
    result_window.title("Extracted Information")
    result_window.geometry("800x300")

    tk.Label(result_window, text="Extracted Information", font=("Arial", 20)).grid(row=0, column=1, pady=10)

    tk.Label(result_window, text="Name \t: ").grid(row=1, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=f"{name_information}").grid(row=1, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Education\t: ").grid(row=2, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=f"{education_information}").grid(row=2, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Phone\t: ").grid(row=3, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=f"{phone}").grid(row=3, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Email\t: ").grid(row=4, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=f"{extract_emails(text)}").grid(row=4, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Skills\t: ").grid(row=5, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=f"{extract_skills(text)}").grid(row=5, column=1, sticky="w", padx=10)
 
if __name__ == '__main__':
    # Create a window of 600x300 and center this on the screen.
    width = 600
    height = 300

    root = tk.Tk()
    root.title("CV Parser")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    # Create a file dialog button.
    button = ttk.Button(root, text='Click to Open CV File')
    button.config(command=lambda filepath='.': process(filepath, root))
    button.pack(fill=X)

    root.mainloop()