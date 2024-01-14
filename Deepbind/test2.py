import customtkinter
from customtkinter import *


class App:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("500x500")
        self.root.title('DeepBind')
        customtkinter.set_appearance_mode('light')
        self.mainframe = CTkFrame(self.root, fg_color='#fffefe', border_width=0, border_color='#5e2e33')
        self.mainframe.place(relx=0.5, rely=0.5, anchor='center')

        self.title_font = CTkFont(family='JetBrains Mono', size=40, weight='bold')
        self.geral_font = CTkFont(family='JetBrains Mono', size=40, slant='italic')
        self.label = CTkLabel(self.root, text='Deep-Bind', font=self.title_font, text_color='#605a54')

        self.label.pack(padx=5, pady=10)
        self.switch = CTkSwitch(self.mainframe, text='False', font=self.geral_font, command=self.toggle,
                                switch_width=40, switch_height=20, fg_color='#111111', progress_color='red',
                                button_color='black', button_hover_color='black')
        self.switch.place(relx=0.48, rely=0.5, anchor='center')

        self.root.mainloop()
        return

    def toggle(self):
        if self.switch.get() == 1:
            self.switch.configure(text='True')
        else:
            self.switch.configure(text='False')


if __name__ == '__main__':
    App()