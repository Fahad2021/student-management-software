from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Information Record")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Information Record",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="gray",fg="brown")
        title.pack(side=TOP,fill=X)

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.class_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()


        # manage frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=600)
        m_title=Label(Manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_class = Label(Manage_Frame, text="Class.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_class.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_class = Entry(Manage_Frame,textvariable=self.class_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_class.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contac = Label(Manage_Frame, text="Contac.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contac.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_contac = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contac.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="DOB.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address.", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address=Text(Manage_Frame,width=25,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        # Button frame
        button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        button_Frame.place(x=15, y=530, width=420)
        addbtn=Button(button_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(button_Frame,text="Update",width=10,command=self.update).grid(column=1,row=0,padx=10,pady=10)
        deletbtn=Button(button_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(button_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        # details frame
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Details_Frame.place(x=500, y=100, width=800, height=600)

        lbl_seach = Label(Details_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_seach.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state="readonly")
        combo_search['values'] = ("Roll_No", "Name", "Contac")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search=Entry(Details_Frame,textvariable=self.search_text,width=20,font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2,  pady=10,padx=20,sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Details_Frame, text="Show All", width=10,pady=5,command=self.fatch_data).grid(row=0, column=4, padx=10, pady=10)

#         table frame
        table_frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=520)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","class","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name.")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All information Required!!!")
        else:
             con=pymysql.connect(host="localhost",user="root",password="",database="stm")
             cur=con.cursor()
             cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                             self.name_var.get(),
                                                                                             self.class_var.get(),
                                                                                             self.gender_var.get(),
                                                                                             self.contact_var.get(),
                                                                                             self.dob_var.get(),
                                                                                             self.txt_Address.get('1.0',END)
                                                                                             ))
             con.commit()
             self.fatch_data()
             self.clear()
             con.close()
             messagebox.showinfo("Successfully","Record has been Inserted")
    def fatch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.class_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.class_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert("1.0",row[6])
    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,class=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (

                                                                                                  self.name_var.get(),
                                                                                                  self.class_var.get(),
                                                                                                  self.gender_var.get(),
                                                                                                  self.contact_var.get(),
                                                                                                  self.dob_var.get(),
                                                                                                  self.txt_Address.get('1.0', END),
                                                                                                  self.Roll_No_var.get(),
                                                                                                  ))
        con.commit()
        self.fatch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fatch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where"+str(self.search_by.get()) +" Like  '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()