# tkinter used to  create GUI
import tkinter as tk
#PyPDF2 used for parsing PDF files
import PyPDF2
#used for image retrieval for GUI
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# top of viewport for GUI
root = tk.Tk()
#Canvas dimensions
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
#Open image
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
#position logo
logo_label.grid(column=1, row=0)

# instructions bottom page
instructions = tk.Label(root, text="Select a PDF file to extract text", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)

#Function to open pdf file from button
def open_file():
    browse_text.set("loading...")
    #File open file fnction
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box and dimensions
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
#Button function and visuals
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="blue", fg="white", width=15, height=2)
browse_text.set("Browse")
#Button position in grid
browse_btn.grid(column=1, row=2)

#Browse button size values
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


#Bottom of GUI Viewport
root.mainloop()

