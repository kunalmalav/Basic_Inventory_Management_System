from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox    #importing library
import sqlite3




class supplierClass():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x500+220+130")
        self.root.title("Purchase")
        self.root.config(bg="black")
        self.root.focus_force()

        #all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
       

        lbl_search=Label(self.root,text="Invoice No", bg = "white",
        font=("goudy old style",15,"bold"))
        lbl_search.place(x=610,y=60)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=750,y=60,width=140)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="black",cursor="hand2").place(x=900,y=58,width=80,height=28)
        
        #title
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=900,height=30)
       #labels
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=60)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow")
        txt_supplier_invoice.place(x=160,y=60,width=180)
       
        #txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow")
      #  txt_contact.place(x=750,y=150,width=180)
        
        

        #row 2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=100)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=160,y=100,width=180)
      
        
        #row 3

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=140)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow")
        txt_contact.place(x=160,y=140,width=180)
        
       #row 4

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=180)
        
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=160,y=180,width=430,height=105)
         #button
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="black",cursor="hand2").place(x=160,y=340,width=80,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="black",cursor="hand2").place(x=260,y=340,width=80,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="black",cursor="hand2").place(x=360,y=340,width=80,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="black",cursor="hand2").place(x=460,y=340,width=80,height=35)


        #employee details

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=610,y=120,width=380,height=350)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(emp_frame,column=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)


        self.SupplierTable.heading("invoice",text="Invoice No")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        
        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=90)
        self.SupplierTable.column("contact",width=90)
        self.SupplierTable.column("desc",width=90)
        
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)    #buttonrelease is a type of event,when we release button after clicking then it will call fn 'get_data'

        #self.show()
     #=============================================================================================
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')   #connection for our database
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
                #parent means as a messagebox of root
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()   #to get result of querry
                if row!=None:
                    messagebox.showerror("Error","Invoice No. already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                               self.var_sup_invoice.get(),
                                               self.var_name.get(),      
                                               self.var_contact.get(),
                                               
                                               self.txt_desc.get('1.0',END),
                                               
        ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()           
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    #str(ex) will catch error in try and will show it

    def show(self):
        con=sqlite3.connect(database=r'ims.db')   #connection for our database
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()  #to fetch all records
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)   #here values are passed




        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    #str(ex) will catch error in try and will show it


    def get_data(self,ev):    #ev is an event
        f=self.SupplierTable.focus()  #we want to focus record of tree view which we clicked
        content=(self.SupplierTable.item(f))     #to get the content upon which we focused,then we passed it in a tupple
        row=content['values']       #filtering values,what values will be there in that particular row will come in 'row' variable
       # print(row)    #row a type of list
        self.var_sup_invoice.set(row[0])    #this time we are using variables to set the data
        self.var_name.set(row[1])      
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')   #connection for our database
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
                #parent means as a messagebox of root
            else:
                cur.execute("Select * from Supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()   #to get result of querry
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No. ",parent=self.root)
                else:
                    cur.execute("Update Supplier set name=?,contact=?,desc=? where invoice=?",(
                                               
                                               self.var_name.get(),      
                                               self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_sup_invoice.get(),

        ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()           
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    #str(ex) will catch error in try and will show it
    

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')   #connection for our database
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
                #parent means as a messagebox of root
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()   #to get result of querry
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)


                else:
                    op=messagebox.askyesno("Conferm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        
                        self.clear()




        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    #str(ex) will catch error in try and will show it
    

    def clear(self):
        self.var_sup_invoice.set(""),     #this time we are using variables to set the data
        self.var_name.set(""),      
        self.var_contact.set(""),
        self.txt_desc.delete('1.0',END),
        
        self.var_searchtxt.set("")
        
        self.show()
    


    def search(self):
        con=sqlite3.connect(database=r'ims.db')   #connection for our database
        cur=con.cursor()
        try:
           
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),)) 
                rows=cur.fetchone()  #to fetch all records
                if rows!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('',END,values=row)   #here values are passed


                else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    #str(ex) will catch error in try and will show it




if __name__=="__main__":
    root=Tk()
    object=supplierClass(root)
    root.mainloop()

