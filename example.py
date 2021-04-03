import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="black", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()


############################
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def get_entry_text(self):
        print(self.text_box.get())

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="black", command=self.master.destroy)
        self.quit.pack(side="bottom")

        entry_frame = tk.Frame(root, borderwidth=5)
        entry_frame.pack()

        self.text_box=tk.Entry(entry_frame)
        self.text_box.pack()

        button = tk.Button(entry_frame, text='get entry', command=self.get_entry_text)
        button.pack(pady=10)

    def say_hi(self):
        print("hi there, everyone!")

  
        

root = tk.Tk()
root.geometry("300x300")
app = Application(master=root)
app.mainloop()