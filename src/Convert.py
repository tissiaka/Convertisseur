from tkinter import *
from tkinter import ttk, filedialog
from fpdf import FPDF
import os
root = Tk()
root.title("Profscience offline PDF Convertisseur")
root.geometry('650x320')
frame = LabelFrame(root, text="Fichier à Convertir", font=(
    'ariel 15 bold'), bd=5, fg='red', labelanchor='n', relief=GROOVE)
frame.place(x=50, y=35)
open_file = Label(frame, text="Ouvrir Fichier:", font=('ariel 15 bold'))
open_file.grid(row=0, column=0, padx=15, pady=15, sticky='e')
format_label = Label(frame, text="Format:", font=('ariel 15 bold'))
format_label.grid(row=1, column=0, padx=15, pady=15, sticky='e')
info_label = Label(frame, font=('ariel 15 bold'))
info_label.grid(row=2, column=1, pady=15)
file = StringVar()
file_entry = Entry(frame, textvariable=file, font=(
    'ariel 11 bold'), bd=2, relief=RIDGE)
file_entry.grid(row=0, column=1, padx=15, pady=15)
file_path = " "


def repertoire():
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="select file", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
    file.set(file_path)


def convertir():
    global file_path, file

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("arial", size=10)
    text_file = open(file.get(), "r")
    for text in text_file:
        pdf.cell(200, 10, txt=text, ln=1, align='L')
    name = file.get().split('/')[-1]
    pdf.output(f"{name.split('.')[0]}.{format1.get()}")
    info_label.config(
        text=f"{name} converted to {name.split('.')[0]}.{format1.get()}")


repertoire_file = Button(frame, text="Dossier", font=(
    'ariel 15 bold'), bd=2, relief=RIDGE, bg='green3', command=repertoire)
repertoire_file.grid(row=0, column=2, padx=15, pady=15)
convertir_file = Button(frame, text="Convertir", font=(
    'ariel 15 bold'), bd=2, relief=RIDGE, bg='green3', command=convertir)
convertir_file.grid(row=1, column=2, padx=15, pady=15)
format1 = StringVar()
file_formats = ['PDF']
format_combo = ttk.Combobox(frame, textvariable=format1, font=(
    'ariel 15 bold'), width=12, state=DISABLED)
format_combo['values'] = file_formats
format_combo.current(0)
format_combo.grid(row=1, column=1, padx=15, pady=15)
root.mainloop()
