import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.invalid = None

        self.create_widgets()

    def create_widgets(self):
        # ListBox
        self.list = tk.Listbox(self)  

        # To add entries
        entry_frame = tk.Frame(root, borderwidth=5)
        entry_frame.pack()

        self.CRN = tk.Entry(entry_frame)
        self.CRN.pack()

        button = tk.Button(entry_frame, text='Add CRN', command=self.insert_entry)
        button.pack(pady=10)

        # To delete listbox entries
        self.delete_btn = tk.Button(self, text="Delete Course", command=self.delete_selection) 
        self.list.pack() 
        self.delete_btn.pack(fill=tk.BOTH) 

        # Start Button: To quit, command=self.master.destroy
        self.start = tk.Button(self, text="Start", fg="black", command=self.start)
        self.start.pack(side="bottom")

    def insert_entry(self):
        Course = self.CRN.get()
        length = len(Course) 

        integer = True
        try:
            int(Course)
        except:
            integer = False
        
        if (length == 5 and integer):
            self.list.insert('end', Course)
            if self.invalid != None:
                self.invalid.pack_forget()
        else:
            if self.invalid == None:
                self.invalid = tk.Label(self,text='Invalid CRN!')
                self.invalid.pack(side="top")


        # Clear entry box
        self.CRN.delete(0, 'end')

    def delete_selection(self): 
        selection = self.list.curselection() 
        self.list.delete(selection)

    def start(self):
        subprocess.call(['./',"example.ahk"])
        self.master.destroy()

root = tk.Tk()
root.title("W&M Registration Macro")
root.geometry("300x400")
app = Application(master=root)
app.mainloop()