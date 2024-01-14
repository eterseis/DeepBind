from customtkinter import *
import keyboard


class App:
    def __init__(self):
        #  main
        self.root = CTk(fg_color='#111111')
        self.root.geometry('960x440')
        self.root.maxsize(960, 440)
        self.root.minsize(960, 440)
        self.root.title('DeepBind 6/01/24')
        # customtkinter.set_appearance_mode('dark')
        #  Título
        self.label_font = CTkFont(family='Comic Sans MS', size=80, weight='bold')
        self.label = CTkLabel(self.root, text='DeepBind', font=self.label_font, text_color='#FFFFFF')
        self.label.place(relx=0.5, rely=0.25, anchor='s')
        # Sub-Título
        self.sub_font = CTkFont(family='Comic Sans MS', size=20, weight='bold', slant='roman')
        self.sub_label = CTkLabel(self.root, text='APP FOR BINDING', font=self.sub_font, text_color='#FFFFFF')
        self.sub_label.place(relx=0.5, rely=0.3, anchor='s')
        # Caixas
        self.caixas = []
        for i in range(10):
            x = 0.1 + i * 0.1
            y = 0.5
            caixa = CTkEntry(self.root, width=20, height=20, fg_color='#3C3745')
            caixa.place(relx=x, rely=y, anchor='center')
            self.caixas.append(caixa)

        # Nums
        self.nums = []
        for i in range(10):
            x = 0.1 + i * 0.1
            y = 0.625
            num = CTkLabel(self.root, text=str(i + 1), font=self.sub_font, text_color='#FFFFFF')
            num.place(relx=x, rely=y, anchor='e')
            self.nums.append(num)

        # Validação
        def valid():
            for caixa in self.caixas:
                text = caixa.get()
                if len(text) == 0:
                    keyboard.unhook_all()
                elif len(text) == 1:
                    keyboard.remap_key(text, str(caixa.index + 1))
                else:
                    caixa.delete(1, END)

        for caixa in self.caixas:
            caixa.trace('w', valid)

        self.root.mainloop()
        return


if __name__ == '__main__':
    App()
