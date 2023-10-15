from tkinter import*
from PIL import Image,ImageTk 
from Employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import SalesClass
from billing import BillClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x700+0+0")
       self.root.title("Inventory Management System")
       self.root.config(bg="black")
       #===Title===
       self.icon_title=PhotoImage(file="images/logo1.png")
       title = Label(self.root,text="Inventory Management System",image = self.icon_title,compound = LEFT,font=("times new roman",40,"bold"),bg="#737373",fg="white",anchor='w',padx=10).place(x=0,y=0,relwidth=1,height=70)

       #===btn_logout===
       #btn_logout=Button(self.root,text="logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

       #===clock===
       self.lbl_clock=Label(self.root,text="Welcome to Inventery Management System\t\t date: DD-MM-YYYY\t\t Time: HH-MM-SS",font=("times new roman",15),bg="#4d636d",fg="white")
       self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

       #===left menu===
       self.menuLogo=Image.open("images/menu_im.png")
       self.menuLogo=self.menuLogo.resize((200,200),Image.LANCZOS)
       self.menuLogo=ImageTk.PhotoImage(self.menuLogo)
       
       Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       Leftmenu.place(x=0,y=102,width=200,height=565)

       lbl_menuLogo=Label(Leftmenu,image=self.menuLogo)
       lbl_menuLogo.pack(side=TOP,fill=X)

       self.icon_side=PhotoImage(file="images/side.png")
       lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="#009688",cursor="hand2").pack(side=TOP,fill=X)
     
       
       btn_supplier=Button(Leftmenu,text="Purchase",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,'bold'),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_category=Button(Leftmenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,'bold'),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_product=Button(Leftmenu,text="Inventory",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,'bold'),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_billing=Button(Leftmenu,text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,'bold'),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_sales=Button(Leftmenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,'bold'),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       

       #===content====

       self.lbl_supplier=Label(self.root,text="Total Purchase\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_supplier.place(x=300,y=120,height=150,width=300)
      
       self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_category.place(x=650,y=120,height=150,width=300)
      
       self.lbl_product=Label(self.root,text="Total Inventory\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_product.place(x=1000,y=120,height=150,width=300)
      
       self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_sales.place(x=300,y=300,height=150,width=300)
      
       #self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
       #self.lbl_sales.place(x=650,y=300,height=150,width=300)
       
       self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
       #self.lbl_sales.place(x=650,y=300,height=150,width=300)
      
       #===footer===
       lbl_footer=Label(self.root,text="Inventory Management System",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
       self.update_content()
#==============================================================
    def employee(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win) 

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)  
        
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_win=BillClass(self.new_win)
        

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            cur.execute("SELECT SUM(qty) FROM product")
            total_qty = cur.fetchone()[0]  # Fetch the sum of the 'quantity' column
            self.lbl_product.config(text=f'Total Quantity \n[ {total_qty} ]')   

            cur.execute("select *from supplier")  
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Purchase \n[ {str(len(supplier))} ]')

            cur.execute("select *from category ")  
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')

            cur.execute("select * from employee ")  
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'total employees\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total sales[{str(bill)}]')
            
            time_=time.strftime("%H:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"welcome to Inventery Management System\t\t date: {str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            

            pass
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.root)  

    def logout(self):
        self.root.destroy()
        os.system("python login.py")   

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
