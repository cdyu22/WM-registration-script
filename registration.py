import tkinter as tk

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

            # To delete listbox entries
        self.delete_btn = tk.Button(self, text="Delete Course", command=self.delete_selection) 
        self.list.pack() 
        self.delete_btn.pack(fill=tk.BOTH) 

            # To add entries
        entry_frame = tk.Frame(root, borderwidth=5)
        entry_frame.pack()

        self.text_box=tk.Entry(entry_frame)
        self.text_box.pack()

        button = tk.Button(entry_frame, text='Add CRN', command=self.insert_entry)
        button.pack(pady=10)

        # Quit Button
        self.quit = tk.Button(self, text="Quit", fg="black", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def insert_entry(self):
        Course = self.text_box.get()
        length = len(Course) # To check if it's 5

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
        listvar = self.list.get(0,"end")
        print(listvar)
        listvar = list(listvar)
        print(listvar)
        listvar = [int(item) for item in listvar]
        print(listvar)
        print("")
            
        self.text_box.delete(0, 'end')

    def delete_selection(self): 
        selection = self.list.curselection() 
        self.list.delete(selection)

root = tk.Tk()
root.geometry("300x400")
app = Application(master=root)
app.mainloop()