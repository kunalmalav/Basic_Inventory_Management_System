from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
from datetime import datetime

class SalesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sales")
        self.root.config(bg="black")
        self.root.focus_force()

        self.bill_list = []
        self.var_month = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 30), bg="#184a45", fg="white", bd=2, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)

        # Month Selection
        lbl_month = Label(self.root, text="Select Month", font=("times new roman", 15), bg="white")
        lbl_month.place(x=50, y=100)

        month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_combo = ttk.Combobox(self.root, textvariable=self.var_month, values=month_options, state="readonly", font=("times new roman", 15))
        month_combo.place(x=200, y=100)
        month_combo.set(self.get_current_month())

        #btn_filter = Button(self.root, text="Filter", command=self.filter_bills, font=("times new roman", 15, "bold"), bg="#2196f3", fg="black", cursor="hand2")
        #btn_filter.place(x=360, y=100, width=120, height=28)

        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2")
        btn_search.place(x=490, y=100, width=120, height=28)

        # Bill List
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease>", self.get_data)

        # Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)

        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange")
        lbl_title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # Image
        self.bill_photo = Image.open("images/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((450, 300), Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image = Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=110)

    def get_current_month(self):
        return datetime.now().strftime("%B")

    def show(self):
        self.bill_list.clear()
        self.Sales_List.delete(0, END)
        for file_name in os.listdir('bill'):
            if file_name.endswith('.txt'):
                self.Sales_List.insert(END, file_name)
                self.bill_list.append(file_name[:-4])

    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        if index_:
            file_name = self.Sales_List.get(index_)
            self.bill_area.delete('1.0', END)
            file_path = os.path.join('bill', file_name)
            try:
                with open(file_path, 'r') as fp:
                    for line in fp:
                        self.bill_area.insert(END, line)
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.", parent=self.root)

    def filter_bills(self):
        selected_month = self.var_month.get()
        if not selected_month:
            return
        self.Sales_List.delete(0, END)
        for file_name in os.listdir('bill'):
            if file_name.endswith('.txt') and selected_month in file_name:
                self.Sales_List.insert(END, file_name)

    def search(self):
        self.var_month.set(self.get_current_month())
        self.show()
        self.bill_area.delete('1.0', END)

if __name__ == "__main__":
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()
