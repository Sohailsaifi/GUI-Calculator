from tkinter import *
import math

scrn = 0

class calc(Tk):

    def dele(self):
        length = len(self.screen.get())
        self.screen.delete(length -2, 'end')

    def click(self, event):

        text = event.widget.cget("text")
        # print(text)
        if text == "=":
            if self.scrn.get().isdigit():
                val = int(self.scrn.get())
            else:
                val = eval(self.screen.get())
                self.scrn.set(val)
                self.screen.update()

        elif text == "AC":
                self.scrn.set("")

        else:
            self.scrn.set(self.scrn.get() + text)
            screen = self.update()

    def __init__(self):
        super().__init__()
        self.maxsize(360,460)
        self.title("Calcuator")
        # self.wm_iconbitmap("Cal.ico")

    def screene(self):

        self.scrn = StringVar()
        self.focus_set()
        self.screen = Entry(textvariable = self.scrn, font = "lucida 20 bold")
        self.screen.grid(row=0, column=0, columnspan=175, padx = 30, pady=60)
        self.config(bg = "grey")


    def buttonee(self):
        Button(text = "7", font = "2").grid(row = 1, column  = 0, ipadx = 20, ipady = 20)
        self.bind("<Button-1>", self.click)
        Button(text = "8", font = "2", bg = "white").grid(row = 1, column  = 1, ipadx = 20, ipady = 20)
        Button(text = "9", font = "2", bg = "white").grid(row = 1, column  = 2, ipadx = 20, ipady = 20)
        Button(text = "4", font = "2", bg = "white").grid(row = 2, column  = 0, ipadx = 20, ipady = 20)
        Button(text = "5", font = "2", bg = "white").grid(row= 2, column  = 1, ipadx = 20, ipady = 20)
        Button(text = "6", font = "2", bg = "white").grid(row = 2, column  = 2, ipadx = 20, ipady = 20)
        Button(text = "1", font = "2",bg = "white").grid(row = 3, column  = 0, ipadx = 20, ipady = 20)
        Button(text = "2", font = "2", bg = "white").grid(row = 3, column  = 1, ipadx = 20, ipady = 20)
        Button(text = "3", font = "2", bg = "white").grid(row = 3, column  = 2, ipadx = 20, ipady = 20)
        Button(text="0", font="2", bg="white").grid(row=4, column=1, ipadx=21, ipady=20)
        Button(text = "+", font = "2", bg = "light blue").grid(row = 1, column = 4, ipadx = 20, ipady = 20)
        Button(text="-", font="2", bg = "light blue").grid(row=2, column=4, ipadx=22, ipady=20)
        Button(text="*", font="2", bg = "light blue").grid(row=3, column=4, ipadx=22, ipady=20)
        Button(text="/", font="2", bg = "light blue").grid(row=4, column=4, ipadx=23, ipady=20)
        Button(text="AC", font="2", bg = "light yellow").grid(row=1, column=5, ipadx=13, ipady=20)
        Button(text="C", font="2", bg = "light yellow", command = lambda: self.dele()).grid(row=2, column=5, ipadx=20, ipady=20)
        Button(text="=", font="2", bg = "light yellow").grid(row=3, column=5, ipadx=20, ipady=60, rowspan = 10, columnspan=5)
        self.bind("<Button-1>", self.click)



if __name__ == '__main__':
    window = calc()
    window.screene()
    window.buttonee()
    window.mainloop()