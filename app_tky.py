from tkinter import Tk, Menu
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def OpenFile():
    name = askopenfilename(
            initialdir="C:/temp/",
            filetypes=(
                ("Excel File", "*.xlsx"), ("All Files", "*.*")),
            title="Choose a file."
    )

    try:
        # code for Spreadsheet analyzer ...
        with open(name, 'r') as UseFile:
            print(UseFile.read())
    except Exception as e:
        print("No file exists", e)


def app():
    root = Tk()
    root.title("Spreadsheet Analyzer")
    label = ttk.Label(
            root,
            text="Result will be here",
            foreground="black",
            font=("Helvetica", 11))
    label.pack(padx=100, pady=100)
    menu = Menu(root)
    root.config(menu=menu)

    file = Menu(menu)

    file.add_command(label='Open', command=OpenFile)
    file.add_command(label='Exit', command=lambda: exit())

    menu.add_cascade(label='File', menu=file)

    root.mainloop()


if __name__ == "__main__":
    app()