from customtkinter import *
import keyboard
from PIL import Image


class App:
    def __init__(self):
        # main
        self.root = CTk(fg_color='#e3dddc')
        self.root.geometry('875x440')
        self.root.maxsize(875, 440)
        self.root.minsize(875, 440)
        self.root.title('DeepBind 12/01/24')

        # RoundedSh
        self.shadow = CTkFrame(self.root, fg_color='#ebe7e8', corner_radius=40, width=800, height=400, border_width=5,
                               border_color='#ebe7e8')
        self.shadow.place(relx=0.5, rely=0.5, anchor='center')

        #  Título
        self.label_font = CTkFont(family='Times New Roman', size=80)
        self.sub_font = CTkFont(family='Times New Roman', size=20, weight='bold', slant='roman')
        self.label = CTkLabel(self.shadow, text='DeepBind', font=self.label_font, text_color='#000000')
        self.label.place(relx=0.5, rely=0.25, anchor='s')
        # Below
        self.img = Image.open('close-eye.png')
        self.sub_label = CTkLabel(self.shadow, text='', image=CTkImage(light_image=self.img, size=(50, 50)))
        self.sub_label.place(relx=0.5, rely=0.375, anchor='s')

        # Frames
        self.mainframe1 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe1.place(relx=0.1, rely=0.5, anchor='center')

        self.mainframe2 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe2.place(relx=0.2, rely=0.5, anchor='center')

        self.mainframe3 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe3.place(relx=0.3, rely=0.5, anchor='center')

        self.mainframe4 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe4.place(relx=0.4, rely=0.5, anchor='center')

        self.mainframe5 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe5.place(relx=0.5, rely=0.5, anchor='center')

        self.mainframe6 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe6.place(relx=0.6, rely=0.5, anchor='center')

        self.mainframe7 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe7.place(relx=0.7, rely=0.5, anchor='center')

        self.mainframe8 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe8.place(relx=0.8, rely=0.5, anchor='center')

        self.mainframe9 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe9.place(relx=0.9, rely=0.5, anchor='center')

        self.mainframe10 = CTkFrame(self.shadow, width=75, height=75, fg_color='#000000', corner_radius=30)
        self.mainframe10.place(relx=0.5, rely=0.8, anchor='center')

        # Nums
        self.num1 = CTkLabel(self.shadow, text='1', font=self.sub_font, text_color='#000000')
        self.num1.place(relx=0.106, rely=0.635, anchor='e')

        self.num2 = CTkLabel(self.shadow, text='2', font=self.sub_font, text_color='#000000')
        self.num2.place(relx=0.206, rely=0.635, anchor='e')

        self.num3 = CTkLabel(self.shadow, text='3', font=self.sub_font, text_color='#000000')
        self.num3.place(relx=0.306, rely=0.635, anchor='e')

        self.num4 = CTkLabel(self.shadow, text='4', font=self.sub_font, text_color='#000000')
        self.num4.place(relx=0.406, rely=0.635, anchor='e')

        self.num5 = CTkLabel(self.shadow, text='5', font=self.sub_font, text_color='#000000')
        self.num5.place(relx=0.506, rely=0.635, anchor='e')

        self.num6 = CTkLabel(self.shadow, text='6', font=self.sub_font, text_color='#000000')
        self.num6.place(relx=0.606, rely=0.635, anchor='e')

        self.num7 = CTkLabel(self.shadow, text='7', font=self.sub_font, text_color='#000000')
        self.num7.place(relx=0.706, rely=0.635, anchor='e')

        self.num8 = CTkLabel(self.shadow, text='8', font=self.sub_font, text_color='#000000')
        self.num8.place(relx=0.806, rely=0.635, anchor='e')

        self.num9 = CTkLabel(self.shadow, text='9', font=self.sub_font, text_color='#000000')
        self.num9.place(relx=0.906, rely=0.635, anchor='e')

        self.num0 = CTkLabel(self.shadow, text='0', font=self.sub_font, text_color='#000000')
        self.num0.place(relx=0.506, rely=0.935, anchor='e')

        # Caixas de Texto 1
        self.string_1 = StringVar()
        self.caixa_1 = CTkEntry(self.mainframe1, width=20, height=20, fg_color='#262626', textvariable=self.string_1,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_1.place(relx=0.5, rely=0.5, anchor='center')
        self.string_1.trace('w', lambda *args: self.valid(self.caixa_1))

        # Caixa de texto 2
        self.string_2 = StringVar()
        self.caixa_2 = CTkEntry(self.mainframe2, width=20, height=20, fg_color='#262626', textvariable=self.string_2,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_2.place(relx=0.5, rely=0.5, anchor='center')
        self.string_2.trace('w', lambda *args: self.valid(self.caixa_2))

        # Caixa de texto 3
        self.string_3 = StringVar()
        self.caixa_3 = CTkEntry(self.mainframe3, width=20, height=20, fg_color='#262626', textvariable=self.string_3,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_3.place(relx=0.5, rely=0.5, anchor='center')
        self.string_3.trace('w', lambda *args: self.valid(self.caixa_3))

        # Caixa de texto 4
        self.string_4 = StringVar()
        self.caixa_4 = CTkEntry(self.mainframe4, width=20, height=20, fg_color='#262626', textvariable=self.string_4,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_4.place(relx=0.5, rely=0.5, anchor='center')
        self.string_4.trace('w', lambda *args: self.valid(self.caixa_4))

        # Caixa de texto 5
        self.string_5 = StringVar()
        self.caixa_5 = CTkEntry(self.mainframe5, width=20, height=20, fg_color='#262626', textvariable=self.string_5,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_5.place(relx=0.5, rely=0.5, anchor='center')
        self.string_5.trace('w', lambda *args: self.valid(self.caixa_5))

        # Caixa de texto 6
        self.string_6 = StringVar()
        self.caixa_6 = CTkEntry(self.mainframe6, width=20, height=20, fg_color='#262626', textvariable=self.string_6,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_6.place(relx=0.5, rely=0.5, anchor='center')
        self.string_6.trace('w', lambda *args: self.valid(self.caixa_6))

        # Caixad de texto 7
        self.string_7 = StringVar()
        self.caixa_7 = CTkEntry(self.mainframe7, width=20, height=20, fg_color='#262626', textvariable=self.string_7,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_7.place(relx=0.5, rely=0.5, anchor='center')
        self.string_7.trace('w', lambda *args: self.valid(self.caixa_7))

        # Caixa de texto 8
        self.string_8 = StringVar()
        self.caixa_8 = CTkEntry(self.mainframe8, width=20, height=20, fg_color='#262626', textvariable=self.string_8,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_8.place(relx=0.5, rely=0.5, anchor='center')
        self.string_8.trace('w', lambda *args: self.valid(self.caixa_8))

        # Caixa de texto 9
        self.string_9 = StringVar()
        self.caixa_9 = CTkEntry(self.mainframe9, width=20, height=20, fg_color='#262626', textvariable=self.string_9,
                                corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_9.place(relx=0.5, rely=0.5, anchor='center')
        self.string_9.trace('w', lambda *args: self.valid(self.caixa_9))
        # Caixa de texto 0/10
        self.string_10 = StringVar()
        self.caixa_10 = CTkEntry(self.mainframe10, width=20, height=20, fg_color='#262626', textvariable=self.string_10,
                                 corner_radius=10, border_color='#262626', text_color='black')
        self.caixa_10.place(relx=0.5, rely=0.5, anchor='center')
        self.string_10.trace('w', lambda *args: self.valid(self.caixa_10))

        self.root.mainloop()
        return

    def valid(self, klangs, *args):
        if len(klangs.get().strip()) == 0:
            keyboard.unhook_all()

            lista = [self.caixa_10, self.caixa_1, self.caixa_2, self.caixa_3, self.caixa_4, self.caixa_5, self.caixa_6,
                     self.caixa_7, self.caixa_8, self.caixa_9]

            for i, v in enumerate(lista):
                if len(lista[i].get()) == 1:
                    keyboard.remap_key(v.get(), str(i))

        elif len(klangs.get()) >= 1:
            klangs.delete(1, END)
            match klangs:
                case self.caixa_1:
                    keyboard.remap_key(klangs.get(), '1')
                case self.caixa_2:
                    keyboard.remap_key(klangs.get(), '2')
                case self.caixa_3:
                    keyboard.remap_key(klangs.get(), '3')
                case self.caixa_4:
                    keyboard.remap_key(klangs.get(), '4')
                case self.caixa_5:
                    keyboard.remap_key(klangs.get(), '5')
                case self.caixa_6:
                    keyboard.remap_key(klangs.get(), '6')
                case self.caixa_7:
                    keyboard.remap_key(klangs.get(), '7')
                case self.caixa_8:
                    keyboard.remap_key(klangs.get(), '8')
                case self.caixa_9:
                    keyboard.remap_key(klangs.get(), '9')
                case self.caixa_10:
                    keyboard.remap_key(klangs.get(), '0')
        else:
            return args


if __name__ == '__main__':
    App()
