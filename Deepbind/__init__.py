import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x200')
        self.root.title('App')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Hello world', background='white', font=('Brass Mono', 30))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='nesw')
        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)

        colors = ['red', 'blue', 'black']
        self.set_color_field = ttk.Combobox(self.mainframe, values=colors)
        self.set_color_field.grid(row=2, column=0)
        set_color_button = ttk.Button(self.mainframe, text='Set Color', command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)
        self.root.mainloop()
        return

    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        new_color = self.set_color_field.get()
        self.text.config(foreground=new_color)


if __name__ == '__main__':
    App()